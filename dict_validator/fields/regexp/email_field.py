""" dict_validator.fields.regexp.email_field """

import re

from ..regexp_field import RegexpField


class EmailField(RegexpField):
    """
    Make sure that the input is a valid email.

    :param domain: string representing a desired domain name. e.g. "gmail.com"
        if not present matches any domain name
    """

    def __init__(self, domain=None, *args, **kwargs):
        if domain:
            domain = re.escape(domain)
        else:
            domain = r"(?:[a-zA-Z0-9-]+\.)+[a-z]{2,}"
        super(EmailField, self).__init__(
            r"^[a-zA-Z0-9._%+-]+@{}$".format(domain),
            "email", *args, **kwargs)

    def deserialize(self, value):
        # Make sure that the domain name is always in lower case
        parts = value.split("@", 1)
        return "@".join([parts[0], parts[1].lower()])
