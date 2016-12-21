import unittest

from dict_validator.objectifier import dict_to_object, object_to_dict


class ObjectifierTest(unittest.TestCase):

    DICT = {
        "parent": {
            "name": "Sam",
            "children": [
                {
                    "name": "Bill",
                    "grandchildren": [
                        {"name": "John"}
                    ]
                }
            ]
        }
    }

    def test_dict_to_object(self):
        value = dict_to_object(self.DICT)

        # the object is dynamic
        # pylint: disable=no-member

        self.assertEqual("Sam",
                         value.parent.name)
        self.assertEqual("Bill",
                         value.parent.children[0].name)
        self.assertEqual("John",
                         value.parent.children[0].grandchildren[0].name)

    def test_object_to_dict(self):
        self.assertEqual(self.DICT, object_to_dict(dict_to_object(self.DICT)))
