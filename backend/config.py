from enum import Enum


class DynamoIndexEnum(Enum):
    ResourceType = 'resource_type'


class ResourceTypeEnum(Enum):
    Shop = 'shop'
    Template = 'template'
