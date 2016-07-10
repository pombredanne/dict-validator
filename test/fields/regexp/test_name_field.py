import unittest

from dict_validator.fields.regexp import NameField


class NameFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb Van Dorum")),
            [])

    def test_nok_lowercase(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb van Dorum")),
            [([], u'Value "Caleb van Dorum" did not match name regexp')])

    def test_nok_numbers(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb V01an Dorum")),
            [([], u'Value "Caleb V01an Dorum" did not match name regexp')])
