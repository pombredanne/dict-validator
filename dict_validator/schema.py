import types

from .dict_field import DictField


class Schema(object):

    def __init__(self, **kwargs):
        pass

    @classmethod
    def deserialize(cls, payload):
        dict_schema = DictField(description=cls.__doc__, schema=cls)
        return dict_schema.deserialize(payload)

    def serialize(self):
        cls = self.__class__
        dict_schema = DictField(description=cls.__doc__, schema=cls)
        return dict_schema.serialize(self)

    @classmethod
    def describe(cls):
        dict_schema = DictField(description=cls.__doc__, schema=cls)
        return dict_schema.describe()
