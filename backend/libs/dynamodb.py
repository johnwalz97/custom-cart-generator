import os

import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


if 'IS_OFFLINE' in os.environ:
    DYNAMODB_CLIENT = boto3.client("dynamodb", endpoint='http://localhost:8000')
    os.environ['DYNAMODB_TABLE'] = 'ccg'
else:
    DYNAMODB_CLIENT = boto3.client("dynamodb")

DYNAMODB_RESERVED_WORDS = ["comment", "name", "status"]


def _build_expression(query):
    parts = []

    for key, value in query.items():
        alias_key = "#alias_%s" % key if key in DYNAMODB_RESERVED_WORDS else key

        if isinstance(value, tuple):
            parts.append(value[0](alias_key, key))
        else:
            parts.append("%s = :%s" % (alias_key, key))

    parts = " AND ".join(parts)

    return parts


def _build_expression_names(query):
    names = {}

    if query:
        for key in query:
            if key in DYNAMODB_RESERVED_WORDS:
                names["#alias_%s" % key] = key

    return names


def _build_expression_values(query):
    values = {}

    for key, value in query.items():
        if isinstance(value, tuple) and isinstance(value[1], list):
            for i, val in enumerate(value[1]):
                values[":%s%s" % (key, i)] = val
        elif isinstance(value, tuple):
            values[":%s" % key] = value[1]
        else:
            values[":%s" % key] = value

    return _marshall_data(values)


def _build_projection_expression(data):
    projection_expression = []

    for key in data:
        if key in DYNAMODB_RESERVED_WORDS:
            projection_expression.append("#alias_%s" % key)
        else:
            projection_expression.append(key)

    return ",".join(projection_expression)


def _build_update_expression(data):
    keys = []
    data = _marshall_data(data)

    for key in data:
        if key in DYNAMODB_RESERVED_WORDS:
            key_alias = "#alias_%s" % key
        else:
            key_alias = key
        keys.append("%s = :%s" % (key_alias, key))

    keys = "SET %s" % ", ".join(keys)

    return keys


def _build_update_expression_values(data):
    values = {":%s" % key: value for key, value in data.items()}
    return _marshall_data(values)


def _marshall_data(data):
    if isinstance(data, list):
        return list(map(_marshall_data, data))
    if isinstance(data, dict):
        serializer = TypeSerializer()
        return {k: serializer.serialize(v) for k, v in data.items()}

    print("Unable to marshall data of type %s", type(data))

    return data


def _unmarshall_data(data):
    if isinstance(data, list):
        return list(map(_unmarshall_data, data))
    if isinstance(data, dict):
        deserializer = TypeDeserializer()
        return {k: deserializer.deserialize(v) for k, v in data.items()}

    print("Unable to unmarshall data of type %s", type(data))

    return data


def delete_item(key):
    DYNAMODB_CLIENT.delete_item(
        TableName=os.environ["DYNAMODB_TABLE"], Key=_marshall_data(key),
    )


def get_item(query, index=None, query_filter=None, table=None):
    if index:
        res = get_many(query, index, query_filter=query_filter, table=table)

        if len(res) > 0:
            return res[0]

        return {}

    args = {
        "Key": _marshall_data(query),
        "TableName": table or os.environ.get("DYNAMODB_TABLE"),
    }
    response = DYNAMODB_CLIENT.get_item(**args)

    return _unmarshall_data(response["Item"])


def get_many(query, index=None, query_filter=None, attributes=None, table=None):
    expression = _build_expression(query)
    expression_values = _build_expression_values(query)
    args = {
        "TableName": table or os.environ.get("DYNAMODB_TABLE"),
        "KeyConditionExpression": expression,
        "ExpressionAttributeValues": expression_values,
    }

    if index:
        args["IndexName"] = index

    if query_filter:
        filter_expression = _build_expression(query_filter)
        filter_values = _build_expression_values(query_filter)
        args["FilterExpression"] = filter_expression
        args["ExpressionAttributeValues"] = {
            **args["ExpressionAttributeValues"],
            **filter_values,
        }

    if attributes:
        args["ProjectionExpression"] = _build_projection_expression(attributes)

    expression_names = {
        **_build_expression_names(query),
        **_build_expression_names(query_filter),
        **_build_expression_names(attributes),
    }
    if expression_names:
        args["ExpressionAttributeNames"] = expression_names

    data = []
    page_key = None
    query_finished = False

    while not query_finished:
        if page_key:
            args["ExclusiveStartKey"] = page_key

        res = DYNAMODB_CLIENT.query(**args)
        data.extend(res["Items"])

        if "LastEvaluatedKey" in res:
            page_key = res["LastEvaluatedKey"]
        else:
            query_finished = True

    return _unmarshall_data(data)


def update_item(query, data, table=None):
    args = {
        "TableName": table or os.environ.get("DYNAMODB_TABLE"),
        "Key": _marshall_data(query),
        "UpdateExpression": _build_update_expression(data),
        "ExpressionAttributeValues": _build_update_expression_values(data),
    }

    expression_names = _build_expression_names(data)

    if expression_names:
        args["ExpressionAttributeNames"] = expression_names

    return DYNAMODB_CLIENT.update_item(**args)


def write_item(data):
    DYNAMODB_CLIENT.put_item(
        TableName=os.environ["DYNAMODB_TABLE"],
        Item=_marshall_data(data),
        ConditionExpression="attribute_not_exists(id)",
    )
