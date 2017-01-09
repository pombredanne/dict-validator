"""
The package aims to simplify payload validation using schemas represented by
by regular Python classes.

In the heart of the library there are just a few top level concepts.

To begin with a Schema is nothing else but a collection of fields
that boils down to a definition of the following shape:

.. code:: python

    class Schema:
        field1 = SampleField()
        field2 = OtherField()

Where each field is a subclass of a :class:`Field` with zero or more
constructor parameters.

Note, you may extend an "object" but it is truly optional.

Once a schema is defined it is possible to employ one of the functions to
process the payload and/or schema:

 - :func:`validate` - to check the payload
 - :func:`describe` - to present the schema in a serializable format
 - :func:`serialize` - to transform the payload with Python specific types
   into something that could be sent over the wire
 - :func:`deserialize` - reverse of :func:`serialize`

Apart from that there are two helper functions that do not really rely on
schema:

 - :func:`dict_to_object` - to deeply transform a dict into an object to use
   **a.b[0].c** instead of **a["b"][0]["c"]**
 - :func:`object_to_dict` - reverse of :func:`dict_to_object`

Most common Field subclasses can be found in :mod:`dict_validator.fields`.

"""

from .helpers import validate, describe, serialize, deserialize
from .field import Field
from .list_field import ListField
from .dict_field import DictField
from .objectifier import dict_to_object, object_to_dict

__all__ = ["validate", "describe", "serialize", "deserialize", "Field",
           "DictField", "ListField", "dict_to_object", "object_to_dict"]
