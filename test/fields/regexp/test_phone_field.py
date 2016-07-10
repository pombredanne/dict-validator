import unittest

from dict_validator.fields.regexp import PhoneField


class PhoneFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sorted(PhoneField().validate("+358 55 000 444")),
            [])

    def test_nok(self):
        self.assertEqual(
            sorted(PhoneField().validate("000003232323")),
            [([], u'Value "000003232323" did not match phone regexp')])

    def test_deserialize(self):
        self.assertEqual(
            PhoneField().deserialize("+358 55 000 444"),
            "+35855000444")
