import unittest

from dict_validator.fields import ChoiceField


class ChoiceFieldTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sorted(ChoiceField([1, 2, 3]).validate(1)), [])

    def test_nok(self):
        self.assertEqual(sorted(ChoiceField([1, 2, 3]).validate(4)),
                         [([], 'Value "4" is not among the choices')])

    def test_description(self):
        self.assertEqual(
            list(ChoiceField([1, 2, 3]).describe()),
            [([], {'choices': [1, 2, 3], 'type': 'Choice'})])
