""" dict_validator.dict_field """

from .field import Field


class DictField(Field):
    """
    A dict of values.

    :param schema: class to be used for validation/serialization of the
        incoming values
    """

    def __init__(self, schema, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)
        self._schema = schema

    # pylint: disable=missing-docstring
    def _get_fields(self):
        for key in dir(self._schema):
            if key.startswith("__"):
                continue
            subschema = getattr(self._schema, key)
            if not isinstance(subschema, Field):
                continue
            yield key, subschema

    def _validate(self, value):
        if not isinstance(value, dict):
            yield ([], "Not a dict")
            return
        value = dict(value)
        for key, subschema in self._get_fields():
            if key not in value:
                if getattr(subschema, "required", True):
                    yield ([], "Key \"{}\" is missing".format(key))
                # For some mysterious reason coverage module just ignores
                # the next line even though it is executed
                continue  # pragma: no cover
            subvalue = value.pop(key)
            for (child_path, error) in subschema.validate(subvalue):
                yield ([key] + child_path, error)
        if value:
            yield ([], "Unkown fields: {}".format(", ".join(value.keys())))

    def describe(self):
        for result in super(DictField, self).describe():
            yield result
        for key, subschema in self._get_fields():
            for (child_path, description) in subschema.describe():
                yield ([key] + child_path, description)

    def serialize(self, value):
        ret_val = {}
        for key, val in value.iteritems():
            ret_val[key] = getattr(self._schema, key).serialize(val)
        return ret_val

    def deserialize(self, value):
        ret_val = {}
        for key, val in value.iteritems():
            ret_val[key] = getattr(self._schema, key).deserialize(val)
        return ret_val
