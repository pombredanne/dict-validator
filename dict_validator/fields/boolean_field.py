""" dict_validator.fields.boolean_field """

from ..field import Field


class BooleanField(Field):
    """
    Match a boolean.
    """

    @property
    def _type(self):
        return "Boolean"

    def _validate(self, value):
        if not isinstance(value, bool):
            return "Not a boolean"
