import json
import os

import shopify

from backend.libs.helpers import create_shopify_session, lambda_http_handler
from backend.shops import create_shop, get_shop, update_shop


@lambda_http_handler(require_auth=True)
def app_installed(**kwargs):
    shop_url = kwargs['shop']
    shop_token = kwargs['token']

    existing_shop = get_shop(shop_url)
    if existing_shop:
        update_shop({**existing_shop, 'token': shop_token})
    else:
        create_shop(shop_url, shop_token)

    session = create_shopify_session(shop_url, shop_token)
    shopify.ShopifyResource.activate_session(session)

    webhook = shopify.Webhook()
    webhook.topic = 'app/uninstalled'
    webhook.address = 'https://customcartz.us/app_uninstalled'
    webhook.format = 'json'
    webhook.save()

    return {'statusCode': 200}


@lambda_http_handler
def get_permission_url(**kwargs):
    shop_url = kwargs['shop']

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
    permission_url = shopify_session.create_permission_url(permission_scopes, os.environ['APP_ENDPOINT'])

    return {'statusCode': 200, 'body': json.dumps({'permission_url': permission_url})}
