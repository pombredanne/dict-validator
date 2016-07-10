""" dict_validator.fields.regexp.name_field """

import re

from ..regexp_field import RegexpField


class NameField(RegexpField):
    """
    Human name e.g. John Smith
    """

    def __init__(self, lowercase_allowed=False, *args, **kwargs):
        super(NameField, self).__init__(
            r"^\w+( \w+)*$",
            "name", *args, **kwargs)
        self._lowercase_allowed = lowercase_allowed

    def _validate(self, value):
        ret_val = super(NameField, self)._validate(value)
        if ret_val:
            return ret_val
        if not self._lowercase_allowed:
            for word in value.split():
                if unicode(word[0]).islower():
                    return "One of the name parts is lowercase"
        if re.search(r"[0-9_]+", value):
            return "Name can't contain digits"
