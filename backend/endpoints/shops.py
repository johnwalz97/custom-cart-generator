import json
import uuid

from backend.config import DynamoIndexEnum, ResourceTypeEnum
from backend.libs.aws_dynamodb import get_item, update_item, write_item
from backend.libs.aws_lambda import http_handler


def get_shop(uri):
    shop = get_item(
        query={"resource_type": ResourceTypeEnum.Shop.value},
        index=DynamoIndexEnum.ResourceType.value,
        query_filter={"uri": uri},
    )
    return shop


@http_handler
def get(request_data):
    return {"statusCode": 200, "body": json.dumps(get_shop(request_data["uri"]))}


@http_handler
def patch(request_data):
    shop = get_shop(request_data["uri"])
    updates = {
        key: value
        for key, value in request_data["updates"].items()
        if shop[key] != value
    }

    update_item({"resource_id": shop["resource_id"]}, updates)

    return {"statusCode": 200, "body": json.dumps({**shop, **updates})}


@http_handler
def post(request_data):
    new_shop = {
        "resource_id": uuid.uuid4().hex,
        "resource_type": ResourceTypeEnum.Shop.value,
        **request_data,
    }

    write_item(new_shop)

    return {"statusCode": 200, "body": json.dumps(new_shop)}
