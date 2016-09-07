import unittest

from dict_validator.fields import NumberField


class NumberFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sorted(NumberField().validate(11)), [])
        self.assertEqual(sorted(NumberField().validate(11.0)), [])
        self.assertEqual(sorted(NumberField().validate(-11)), [])

    def test_nok(self):
        self.assertEqual(sorted(NumberField().validate("11")),
                         [([], "Not a number")])
