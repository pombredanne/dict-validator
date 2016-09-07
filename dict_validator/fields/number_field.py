""" dict_validator.fields.number_field """

from ..field import Field


class NumberField(Field):
    """
    Match integers, floats and longs
    """

    def _validate(self, value):
        if not isinstance(value, (int, float, long)):
            return "Not a number"
