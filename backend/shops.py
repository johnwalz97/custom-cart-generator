from uuid import uuid4

from backend.libs.dynamodb import get_item, update_item, write_item


def create_shop(shop_url, access_token):
    resource_id = uuid4().hex
    return write_item({
        'resource_id': resource_id,
        'shop': '',
        'shop_url': shop_url,
        'access_token': access_token
    })


def get_shop(shop_url):
    return get_item({''})


def update_shop(shop):
    return {}
