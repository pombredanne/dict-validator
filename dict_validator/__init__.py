"""
The package aims to simplify schema declaration and validation customization
by using regular Python classes to define data structures.

In the heart of the library there are just a few top level concepts.

To begin with a Schema definition is supposed to look as a collection of
fields that looks as follows:

.. code:: python

    class Schema:
        field1 = SampleField()
        field2 = OtherField()

Where each field is a subclass of a :class:`Field` with zero or more
constructor parameters.

Note, you may extend an "object" but it is truly optional.

Once a schema is defined it is possible to employ one of the functions to
process the payload and/or schema:

 - :func:`validate`
 - :func:`describe`
 - :func:`serialize`
 - :func:`deserialize`

Apart from that there are two helper functions that do not really rely on
schema:

 - :func:`dict_to_object`
 - :func:`object_to_dict`
"""

from .helpers import validate, describe, serialize, deserialize
from .field import Field
from .list_field import ListField
from .dict_field import DictField
from .objectifier import dict_to_object, object_to_dict

__all__ = ["validate", "describe", "serialize", "deserialize", "Field",
           "DictField", "ListField", "dict_to_object", "object_to_dict"]
