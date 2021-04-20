from functools import partial, wraps
import json


def http_handler(handler=None, require_auth=False):
    if handler is None:
        return partial(http_handler, require_auth=require_auth)

    @wraps(handler)
    def wrapper(event, _):
        try:
            request_data = {}
            if 'queryStringParameters' in event and event['queryStringParameters']:
                request_data = event['queryStringParameters']
            if 'body' in event and event['body']:
                request_data = {**request_data, **json.loads(event['body'])}

            handler_res = handler(request_data)

            if "headers" in handler_res:
                handler_res["headers"]["Access-Control-Allow-Origin"] = "*"
            else:
                handler_res["headers"] = {"Access-Control-Allow-Origin": "*"}

            return handler_res
        except Exception as err:
            print(err)
            return {
                "statusCode": 500,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps("Internal Server Error"),
            }

    return wrapper
