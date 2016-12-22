import unittest

from dict_validator.fields import NumberField


class NumberFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sorted(NumberField().validate(11)), [])
        self.assertEqual(sorted(NumberField().validate(11.0)), [])
        self.assertEqual(sorted(NumberField().validate(-11)), [])

    def test_nok(self):
        self.assertEqual(
            [([], "Not a valid number")],
            sorted(NumberField().validate("11"))
        )

    def test_float_not_allowed(self):
        self.assertEqual(sorted(NumberField().validate(11)), [])
        self.assertEqual(sorted(NumberField().validate(-11)), [])
        self.assertEqual(
            [([], "Not a valid number")],
            sorted(NumberField(can_be_float=False).validate(11.0))
        )

    def test_too_small(self):
        self.assertEqual(
            [([], "Too small")],
            sorted(NumberField(min=12).validate(11))
        )

    def test_too_large(self):
        self.assertEqual(
            [([], "Too large")],
            sorted(NumberField(max=9).validate(11))
        )

    def test_describe(self):
        self.assertEqual(
            [([], {'can_be_float': True, 'max': None, 'min': None,
                   'type': 'Number'})],
            sorted(NumberField().describe())
        )
