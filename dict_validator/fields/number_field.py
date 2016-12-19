""" dict_validator.fields.number_field """

from ..field import Field


class NumberField(Field):
    """
    Match integers, floats and longs

    :param min: the smallest number allowed
    :param max: the largest number allowed
    :param can_be_float: True if the number can contain a dot
    """

    # pylint: disable=redefined-builtin
    def __init__(self, min=None, max=None, can_be_float=True, *args, **kwargs):
        super(NumberField, self).__init__(*args, **kwargs)
        self._min = min
        self._max = max
        self._can_be_float = can_be_float

    def _validate(self, value):
        allowed_types = (int, long)
        if self._can_be_float:
            allowed_types += (float,)

        if not isinstance(value, allowed_types):
            return "Not a valid number"

        if self._min is not None and value < self._min:
            return "Too small"

        if self._max is not None and value > self._max:
            return "Too large"

    def _describe(self):
        return {
            "min": self._min,
            "max": self._max,
            "can_be_float": self._can_be_float
        }
