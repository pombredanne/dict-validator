import unittest

from dict_validator import serialize, deserialize, Field, ListField, DictField


class String(Field):

    def _validate(self, value):
        pass

    def serialize(self, value):
        return "SERIALIZED {}".format(super(String, self).serialize(value))

    def deserialize(self, value):
        return "DESERIALIZED {}".format(super(String, self).deserialize(value))


class Child:
    items = ListField(String("String item"),
                      description="A collection of important items")


class Parent:
    child = DictField(Child, description="Dict child")
    plain_field = String(description="Pure string", required=False)


class SerializationTest(unittest.TestCase):

    def test_serialize(self):
        self.assertEqual(
            serialize(Parent, {
                "child": {
                    "items": ["OUTGOING"]
                },
                "plain_field": "OUTGOING"
            }),
            {
                "child": {
                    "items": ["SERIALIZED OUTGOING"]
                },
                "plain_field": "SERIALIZED OUTGOING"
            })

    def test_deserialize(self):
        self.assertEqual(
            deserialize(Parent, {
                "child": {
                    "items": ["INCOMING"]
                },
                "plain_field": "INCOMING"
            }),
            {
                "child": {
                    "items": ["DESERIALIZED INCOMING"]
                },
                "plain_field": "DESERIALIZED INCOMING"
            })
