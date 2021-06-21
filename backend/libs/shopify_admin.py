import os
import shopify


def activate_session(shop_uri, access_token):
    shopify.Session.setup(
        api_key=os.environ['SHOPIFY_API_KEY'],
        secret=os.environ['SHOPIFY_API_SECRET'],
    )

    shopify.ShopifyResource.activate_session(
        shopify.Session(
            shop_uri,
            os.environ['SHOPIFY_API_VERSION'],
            access_token,
        )
    )


def _get_many(obj, shop_uri, access_token):
    activate_session(shop_uri, access_token)

    return [
        item.to_dict()
        for page in shopify.PaginatedIterator(obj.find())
        for item in page
    ]


def get_product(product_id, shop_uri, access_token):
    activate_session(shop_uri, access_token)

    return shopify.Product.find(product_id).to_dict()


def get_products(shop_uri, access_token):
    return _get_many(shopify.Product, shop_uri, access_token)


def get_discount(discount_id, shop_uri, access_token):
    activate_session(shop_uri, access_token)

    return shopify.PriceRule.find(discount_id).to_dict()


def get_discounts(shop_uri, access_token):
    return _get_many(shopify.PriceRule, shop_uri, access_token)
