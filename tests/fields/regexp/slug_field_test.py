import unittest

from dict_validator.fields.regexp import SlugField


class SlugFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sorted(SlugField().validate("sample-slug-01")),
            [])

    def test_nok(self):
        self.assertEqual(
            sorted(SlugField().validate("Sample Not Slug")),
            [([], u'Value "Sample Not Slug" did not match slug regexp')])
