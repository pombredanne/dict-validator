""" dict_validator.field """

from abc import ABCMeta, abstractmethod, abstractproperty


class Field(object):
    """
    The "leaf" primitive data type in a schema.
    E.g. string, integer, float, etc.
    """

    __metaclass__ = ABCMeta

    def __init__(self, description=None, required=True):
        self._description = description
        self._required = required

    def _describe(self):
        """ Return a payload that would describe the field. """

    @abstractproperty
    def _type(self):
        """
        :return: a human readable string representing a type to be mentioned
                 in the describe method. By default it is a class name.
        :rtype: str
        """

    @abstractmethod
    def _validate(self, value):
        """
        Validate the incoming value, return error message or yield several
        error messages if there are errors.
        """

    # pylint: disable=no-self-use
    def serialize(self, value):
        """
        :return: a payload ready to be sent over the wire
        """
        return value

    # pylint: disable=no-self-use
    def deserialize(self, value):
        """
        :param value: a payload sent over the wire
        :return: a payload with Python specific data types
        """
        return value

    @property
    def required(self):
        """ True if the field has to be present in the incoming dict """
        return self._required

    def describe(self):
        """
        :yield: (path, {...description...}),
            e.g (["parent", "child"], {"required": False})
        """
        description = self._describe() or {}
        description["type"] = self._type
        if not self._required:
            description["required"] = False
        if self._description:
            description["description"] = self._description
        yield ([], description)

    def validate(self, value):
        """
        :param value: a payload
        :yield: (path, erro_msg),
            e.g (["parent", "child"], "Error message")
        """
        result = self._validate(value)

        if result is None:
            return
        elif isinstance(result, basestring):
            yield ([], result)
        else:
            for chunk in result:
                if isinstance(chunk, (list, tuple)):
                    yield chunk
                else:
                    yield([], chunk)
