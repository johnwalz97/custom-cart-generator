import base64
from functools import wraps
import hashlib
import hmac

from flask import abort, session, redirect, url_for, request
import shopify

import config
from models import Shop


def shopify_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'shopify_token' not in session:
            shop_url = request.args.get('shop')
            shopify.Session.setup(
                api_key=config.SHOPIFY_API_KEY,
                secret=config.SHOPIFY_SHARED_SECRET
            )
            try:
                shopify.Session.validate_params(request.args)
            except Exception:
                return redirect(url_for('install', **request.args))

            try:
                shop = Shop.get(Shop.shop == shop_url)
            except Exception:
                return redirect(url_for('install', **request.args))

            session['shopify_token'] = shop.token
            session['shopify_url'] = shop_url
            session['shopify_id'] = shop.id

        else:
            try:
                shop = Shop.get(Shop.shop == session['shopify_url'])
            except Exception:
                session.pop('shopify_token')
                session.pop('shopify_url')
                session.pop('shopify_id')

                return redirect(url_for('install', **request.args))

        return f(*args, **kwargs)

    return decorated_function


def shopify_webhook_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        encoded_hmac = request.headers.get('X-Shopify-Hmac-Sha256')
        decoded_hmac = base64.b64decode(encoded_hmac).hex()
        data = request.get_data()

        if not verify_hmac(data, decoded_hmac):
            print(f"HMAC could not be verified: \n\thmac {decoded_hmac}\n\tdata {data}")
            abort(401)

        return f(*args, **kwargs)

    return decorated_function


def verify_hmac(data, original_hmac):
    new_hmac = hmac.new(
        config.SHOPIFY_SHARED_SECRET.encode('utf-8'),
        data,
        hashlib.sha256,
    )

    return new_hmac.hexdigest() == original_hmac
