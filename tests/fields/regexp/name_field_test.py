import unittest

from dict_validator.fields.regexp import NameField


class NameFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb Van Dorum")),
            [])

    def test_nok_wrong_ascii_chars(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb V@n Dorum")),
            [([], 'Value "Caleb V@n Dorum" did not match name regexp')])

    def test_nok_lowercase(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb van Dorum")),
            [([], 'One of the name parts is lowercase')])

    def test_nok_numbers(self):
        self.assertEqual(
            sorted(NameField().validate("Caleb V01an Dorum")),
            [([], "Name can't contain digits")])
