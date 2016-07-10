""" dict_validator.fields.regexp.name_field """

from ..regexp_field import RegexpField


class NameField(RegexpField):
    """
    Human name e.g. John Smith

    TODO: add Unicode support
    """

    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(
            r"^[A-Z][a-z]+( [A-Z][a-z]+)*$",
            "name", *args, **kwargs)
