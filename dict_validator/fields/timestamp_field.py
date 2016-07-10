""" dict_validator.fields.timestamp_field """

import datetime

from ..field import Field


class TimestampField(Field):
    """
    UTC timestamp. Could be a datetime, a date or time. By default it is
    datetime.

    The timestamp has to be formatted according to:
    https://en.wikipedia.org/wiki/ISO_8601

    The incoming string is deserialized into datetime object.
    The outgoing datetime object is serialized into a string.

    :param time_format: one of
        [TimestampField.DateTime, TimestampField.Date, TimestampField.Time]
    """

    # pylint: disable=missing-docstring, no-init, too-few-public-methods

    class DateTime(object):
        value = "%Y-%m-%d %H:%M:%S.%f"
        name = "datetime"

    class Date(object):
        value = "%Y-%m-%d"
        name = "date"

    class Time(object):
        value = "%H:%M:%S.%f"
        name = "time"

    def __init__(self, time_format=DateTime, *args, **kwargs):
        super(TimestampField, self).__init__(*args, **kwargs)
        self._format = time_format

    def _validate(self, value):
        try:
            datetime.datetime.strptime(value, self._format.value)
        except ValueError:
            return "\"{}\" is not a valid {}".format(value, self._format.name)

    def deserialize(self, value):
        return datetime.datetime.strptime(value, self._format.value)

    def serialize(self, value):
        return datetime.datetime.strftime(value, self._format.value)

    def _describe(self):
        return {
            "type": self._format.name
        }
