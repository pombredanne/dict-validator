""" dict_validator.fields.boolean_field """

from ..field import Field


class BooleanField(Field):
    """
    Match a boolean.
    """

    def _validate(self, value):
        if not isinstance(value, bool):
            return "Not a boolean"
