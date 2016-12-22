import unittest

from dict_validator import describe, Field, ListField, DictField


class String(Field):

    @property
    def _type(self):
        return "String"

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
            [([], {'type': 'Dict'}),
             (['child'], {'description': 'Dict child', 'type': 'Dict'}),
             (['child', 'items'],
              {'description': 'A collection of important items',
               'type': 'List'}),
             (['child', 'items', '{N}'], {'description': 'String item',
                                          'type': 'String'}),
             (['plain_field'],
              {'description': 'Pure string', 'required': False,
               'type': 'String'})])
