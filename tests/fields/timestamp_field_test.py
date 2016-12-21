import datetime
import unittest

from dict_validator.fields import TimestampField


class TimestampFieldTest(unittest.TestCase):

    def _ok(self, time_format, value):
        self.assertEqual(
            sorted(TimestampField(time_format).validate(value)),
            [])

    def _nok(self, time_format, value):
        self.assertEqual(
            sorted(TimestampField(time_format).validate(value)),
            [([], '"WRONG VALUE" is not a valid {}'.format(time_format.name))])

    def test_ok_datetime(self):
        self._ok(TimestampField.DateTime, '2016-07-10 13:06:04.698084')

    def test_ok_date(self):
        self._ok(TimestampField.Date, '2016-07-10')

    def test_ok_time(self):
        self._ok(TimestampField.Time, '13:06:04.698084')

    def test_nok_datetime(self):
        self._nok(TimestampField.DateTime, 'WRONG VALUE')

    def test_nok_date(self):
        self._nok(TimestampField.Date, 'WRONG VALUE')

    def test_nok_time(self):
        self._nok(TimestampField.Date, 'WRONG VALUE')

    def test_serialization(self):
        self.assertIsInstance(
            TimestampField().serialize(datetime.datetime.utcnow()),
            str)

    def test_deserialization(self):
        self.assertIsInstance(
            TimestampField().deserialize("2016-07-10 13:06:04.698084"),
            datetime.datetime)

    def test_description(self):
        self.assertEqual(
            list(TimestampField().describe()),
            [([], {'type': 'datetime'})])
