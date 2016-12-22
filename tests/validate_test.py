import unittest

from dict_validator import validate, Field, ListField, DictField


class String(Field):

    @property
    def _type(self):
        return "NOT IMPORTANT VALUE"

    def _validate(self, value):
        if not isinstance(value, basestring):
            return "Not a string"


class ValidateTest(unittest.TestCase):

    def _val(self, description, structure, expectation):
        self.assertEqual(list(validate(description, structure)), expectation)

    def test_plain_field(self):

        class Schema:
            string = String()

        self._val(Schema, {"string": "bar"}, [])
        self._val(Schema, {"string": 1}, [(['string'], 'Not a string')])

    def test_nested_structure(self):

        class Child:
            other_field = String()

        class Parent:
            child = DictField(Child)

        self._val(
            Parent,
            structure={
                "child": {"other_field": "new_value"}
            },
            expectation=[])

        self._val(
            Parent,
            structure={
                "child": {"other_field": 1}
            },
            expectation=[
                (['child', 'other_field'], 'Not a string')
            ])

    def test_list_of_fields(self):

        class Schema:
            field = ListField(String())

        self._val(Schema, {"field": ["string"]}, [])
        self._val(Schema, {"field": [1]}, [(['field', 0], 'Not a string')])

    def test_list_of_nested_structures(self):

        class Child:
            other_field = String()

        class Parent:
            child = ListField(DictField(Child))

        self._val(
            Parent,
            structure={
                "child": [{"other_field": "new_value"}]
            },
            expectation=[])

        self._val(
            Parent,
            structure={
                "child": [{"other_field": 1}]
            },
            expectation=[
                (['child', 0, 'other_field'], 'Not a string')
            ])

    def test_optional_field(self):

        class Schema:
            string = String(required=False)

        self._val(Schema, {"string": "bar"}, [])
        self._val(Schema, {"string": 1}, [(['string'], 'Not a string')])
        self._val(Schema, {}, [])

    def test_missing_field(self):

        class Schema:
            string = String()
            other_field = String(required=False)

        self._val(Schema, {},
                  [([], 'Key "string" is missing')])

    def test_unknown_field(self):

        class Schema:
            string = String()

        self._val(Schema, {"string": "FOO", "bar": "BAR"},
                  [([], "Unkown fields: bar")])

    def test_not_a_dict(self):

        class Schema:
            string = String()

        self._val(Schema, "NOT A DICT", [([], 'Not a dict')])

    def test_yield_error(self):

        class SuperField(Field):

            @property
            def _type(self):
                return "SuperField"

            def _validate(self, value):
                yield "Error"

        class Schema:
            string = SuperField(required=False)

        self._val(Schema, {"string": "bar"}, [(['string'], 'Error')])

    def test_not_a_list(self):

        class Schema:
            child = ListField(String())

        self._val(Schema, {"child": "NOT A LIST"}, [(['child'], 'Not a list')])
