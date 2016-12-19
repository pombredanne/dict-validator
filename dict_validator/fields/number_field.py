""" dict_validator.fields.number_field """

from ..field import Field


class NumberField(Field):
    """
    Match integers, floats and longs
    """

    def __init__(self, min=None, max=None, can_be_float=True):
        self._min = min
        self._max = max
        self._can_be_float = can_be_float

    def _validate(self, value):
        allowed_types = (int, long)
        if self._can_be_float:
            allowed_types += (float,)

        if not isinstance(value, allowed_types):
            return "Not a number"

    def _describe(self):
        return {
            "min": self._min,
            "max": self._max,
            "can_be_float": self._can_be_float
        }