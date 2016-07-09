""" dict_validator.helpers """

from .dict_field_decorator import dict_field_decorator


@dict_field_decorator
def validate(schema, value):
    """
    Validate value again a given schema.

    :param schema: a class representing the structure to be used for validation
    :param value: a dict
    :yield: (path, erro_msg),
        e.g (["parent", "child"], "Error message")
    """
    return schema.validate(value)


@dict_field_decorator
def describe(schema):
    """
    Describe a given schema.

    :param schema: a class representing the structure to be documented
    :yield: (path, {...description...}),
        e.g (["parent", "child"], {"required": False})
    """
    return schema.describe()


@dict_field_decorator
def serialize(schema, value):
    """
    Serialize a value before sending it over the wire.

    :param schema: a class representing the structure to be used for
        serialization
    :param value: a dict with Python specific data types
    :return: a dict ready to be sent over the wire
    """
    return schema.serialize(value)


@dict_field_decorator
def deserialize(schema, value):
    """
    Deserialize a value after sending it over the wire.

    :param schema: a class representing the structure to be used for
        deserialization
    :param value: a dict sent over the wire
    :return: a dict with Python specific data types
    """
    return schema.deserialize(value)
