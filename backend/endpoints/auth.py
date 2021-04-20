import os
import urllib.parse
import urllib.request

from backend.libs.aws_lambda import http_handler


@http_handler
def get_access_token(request_data):
    query_params = {
        'client_id': os.environ['SHOPIFY_API_KEY'],
        'client_secret': os.environ['SHOPIFY_API_SECRET'],
        'code': request_data['code'],
    }
    url = "https://%s/admin/oauth/access_token?" % request_data['shop']

    request = urllib.request.Request(url, urllib.parse.urlencode(query_params).encode("utf-8"))
    response = urllib.request.urlopen(request)

    return {'statusCode': 200, 'body': response.read().decode("utf-8")}
