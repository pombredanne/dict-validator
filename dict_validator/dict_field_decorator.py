import types

from functools import wraps

from .dict_field import DictField


# pylint: disable=missing-docstring
def dict_field_decorator(handler):

    # pylint: disable=missing-docstring
    @wraps(handler)
    def wrapper(schema, *args, **kwargs):
        if isinstance(schema, types.ClassType):
            schema = DictField(description=schema.__doc__, schema=schema)
        return handler(schema, *args, **kwargs)

    return wrapper
