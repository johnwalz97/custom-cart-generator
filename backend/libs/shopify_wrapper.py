import os
import shopify


def get_session(shop):
    shopify.Session.setup(
        api_key=os.environ['SHOPIFY_API_KEY'],
        secret=os.environ['SHOPIFY_API_SECRET'],
    )

    return shopify.Session(shop, os.environ['SHOPIFY_API_VERSION'])


def get_authenticated_session(shop_url, shop_token):
    shopify.Session.setup(
        api_key=os.environ['SHOPIFY_API_KEY'],
        secret=os.environ['SHOPIFY_API_SECRET'],
    )

    session = shopify.Session(
        shop_url,
        os.environ['SHOPIFY_API_VERSION'],
        shop_token,
    )
    shopify.ShopifyResource.activate_session(session)


def get_products():
    pass
