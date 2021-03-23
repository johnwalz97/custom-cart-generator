import json
import os

import shopify

from backend.libs.helpers import create_shopify_session, lambda_http_handler
from backend.shops import create_shop, get_shop, update_shop


@lambda_http_handler
def app_installed(**kwargs):
    shopify_session = create_shopify_session(kwargs['shop'])
    shopify.ShopifyResource.activate_session(shopify_session)

    access_token = shopify_session.request_token(kwargs)

    existing_shop = get_shop(kwargs['shop'])
    if existing_shop:
        update_shop({**existing_shop, 'token': access_token})
    else:
        create_shop(kwargs['shop'], access_token)

    session = create_shopify_session(kwargs['shop'], access_token)
    shopify.ShopifyResource.activate_session(session)

    # webhook = shopify.Webhook()
    # webhook.topic = 'app/uninstalled'
    # webhook.address = os.environ['APP_ENDPOINT'] + '/app_uninstalled'
    # webhook.save()

    redirect_url = 'http://localhost:5000/' if 'IS_OFFLINE' in os.environ else os.environ['APP_ENDPOINT']

    return {'statusCode': 301, 'headers': {'Location': redirect_url}}


@lambda_http_handler
def get_permission_url(shop_url, **_):
    permission_scopes = [
        'write_products',
        'read_products',
        'read_discounts',
        'read_price_rules',
        'write_price_rules',
        'write_discounts',
        'read_script_tags',
        'write_script_tags',
    ]

    shopify_session = create_shopify_session(shop_url)

    base_url = 'http://localhost:5001/dev' if 'IS_OFFLINE' in os.environ else os.environ['APP_ENDPOINT']
    permission_url = shopify_session.create_permission_url(
        permission_scopes,
        base_url + '/app_installed',
    )

    return {'statusCode': 200, 'body': json.dumps({'permission_url': permission_url})}
