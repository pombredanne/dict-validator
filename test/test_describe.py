import unittest

from dict_validator import describe, Field, ListField, DictField


class String(Field):

    def _validate(self, value):
        pass


class DescribeTest(unittest.TestCase):

    def test_description(self):

        class Child:
            items = ListField(String("String item"),
                              description="A collection of important items")

        class Parent:
            ignored_field = "Nothing"
            child = DictField(Child, description="Dict child")
            plain_field = String(description="Pure string", required=False)

        self.assertEqual(
            sorted(describe(Parent)),
            [(['child'], {'description': 'Dict child'}),
             (['child', 'items'],
              {'description': 'A collection of important items'}),
             (['child', 'items', '{N}'], {'description': 'String item'}),
             (['plain_field'],
              {'description': 'Pure string', 'required': False})])
