import unittest

from dict_validator.fields import RegexpField


class RegexpFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sorted(RegexpField(r"^[ab]{2}$").validate("aa")),
            [])

    def test_nok(self):
        self.assertEqual(
            sorted(RegexpField(r"^[ab]{2}$").validate("cc")),
            [([], 'Value "cc" did not match regexp')])

    def test_description(self):
        self.assertEqual(
            list(RegexpField(r"^[ab]{2}$").describe()),
            [([], {'pattern': r'^[ab]{2}$'})])
