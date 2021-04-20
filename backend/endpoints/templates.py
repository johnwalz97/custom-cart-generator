import json
import uuid

from backend.config import DynamoIndexEnum, ResourceTypeEnum
from backend.libs.aws_dynamodb import get_item, get_many, update_item, write_item
from backend.libs.aws_lambda import http_handler


@http_handler
def get(_):
    templates = get_many(
        {'resource_type': ResourceTypeEnum.Template.value},
        index=DynamoIndexEnum.ResourceType.value,
    )

    return {'statusCode': 200, 'body': json.dumps(templates)}


@http_handler
def patch(request_data):
    template = get_item({'resource_id': request_data["template_id"]})
    updates = {
        key: value
        for key, value in request_data['updates'].items()
        if template[key] != value
    }

    update_item({'resource_id': request_data['template_id']}, updates)

    return {'statusCode': 200, 'body': json.dumps({**template, **updates})}


@http_handler
def post(request_data):
    new_template = {'resource_id': uuid.uuid4().hex, **request_data}

    write_item(new_template)

    return {'statusCode': 200, 'body': json.dumps(new_template)}
