import json

from backend.endpoints.shops import get_shop
from backend.libs.aws_lambda import http_handler
from backend.libs.shopify_admin import get_discounts, get_discount


@http_handler
def get(request_data):
    shop = get_shop(request_data["shop"])

    if request_data["id"]:
        res = get_discount(int(request_data["id"]), shop["uri"], shop["access_token"])
    else:
        res = get_discounts(shop["uri"], shop["access_token"])

    return {'statusCode': 200, 'body': json.dumps(res)}
