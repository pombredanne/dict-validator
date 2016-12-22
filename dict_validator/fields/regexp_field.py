""" dict_validator.fields.regexp_field """

import re

from ..field import Field


class RegexpField(Field):
    """
    Accept the input that matches a given regular expression.

    :param regexp: string value specifying the regular expression
    """

    def __init__(self, regexp, metavar=None, *args, **kwargs):
        super(RegexpField, self).__init__(*args, **kwargs)
        self._regexp = re.compile(regexp, re.UNICODE)
        if metavar is None:
            self._metavar = ""
        else:
            self._metavar = metavar + " "

    def _validate(self, value):
        if not self._regexp.match(value):
            return u"Value \"{}\" did not match {}regexp".format(value,
                                                                 self._metavar)

    def _describe(self):
        return {
            "pattern": self._regexp.pattern
        }

    @property
    def _type(self):
        return "Regexp"
