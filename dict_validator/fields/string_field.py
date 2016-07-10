""" dict_validator.fields.string_field """

from ..field import Field


class StringField(Field):
    """
    Match any input of string type.
    """

    def _validate(self, value):
        if not isinstance(value, basestring):
            return "Not a string"
