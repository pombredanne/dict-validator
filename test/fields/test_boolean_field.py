import unittest

from dict_validator.fields import BooleanField


class BooleanFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sorted(BooleanField().validate(True)), [])
        self.assertEqual(sorted(BooleanField().validate(False)), [])

    def test_nok(self):
        self.assertEqual(sorted(BooleanField().validate(11)),
                         [([], "Not a boolean")])
