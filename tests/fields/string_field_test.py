import unittest

from dict_validator.fields import StringField


class StringFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sorted(StringField().validate("FOO")), [])

    def test_nok(self):
        self.assertEqual(sorted(StringField().validate(11)),
                         [([], "Not a string")])

    def test_description(self):
        self.assertEqual(
            list(StringField().describe()),
            [([], {'type': 'String'})])
