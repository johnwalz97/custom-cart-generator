import os
from functools import partial, wraps
import json

from botocore.exceptions import ClientError
import shopify


def create_shopify_session(shop_url, shop_token=None):
    shopify.Session.setup(
        api_key=os.environ['SHOPIFY_API_KEY'],
        secret=os.environ['SHOPIFY_API_SECRET'],
    )

    if shop_token:
        return shopify.Session(
            shop_url,
            os.environ['SHOPIFY_API_VERSION'],
            shop_token,
        )

    return shopify.Session(shop_url, os.environ['SHOPIFY_API_VERSION'])


def lambda_http_handler(handler=None, require_auth=False):
    if handler is None:
        return partial(lambda_http_handler, require_auth=require_auth)

    @wraps(handler)
    def wrapper(event, _):
        try:
            request_data = {}
            if 'queryStringParameters' in event and event['queryStringParameters']:
                request_data = {**request_data, **event['queryStringParameters']}
            if 'body' in event and event['body']:
                request_data = {**request_data, **event['body']}

            handler_res = handler(**request_data)

            if "headers" in handler_res:
                handler_res["headers"]["Access-Control-Allow-Origin"] = "*"
            else:
                handler_res["headers"] = {"Access-Control-Allow-Origin": "*"}

            return handler_res
        except ClientError as err:
            print(err)
            err_msg = err.response["Error"]["Message"]

            return {
                "statusCode": 422,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps(err_msg),
            }
        except Exception as err:
            print(err)
            return {
                "statusCode": 500,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps("Internal Server Error"),
            }

    return wrapper
