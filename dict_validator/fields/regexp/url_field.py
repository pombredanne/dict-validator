""" dict_validator.fields.regexp.url_field """

import re

from ..regexp_field import RegexpField


PROTOCOL = r"(https?:\/\/)?"
DOMAIN = r"([\da-z\.-]+\.)+[a-z]{2,8}"
PATH = r"(\/[\/\w \.-]*)?"
QUERY = r"(\?[\/\w= \.-_&]*)?"
HASH = r"(#[\/\w= \.-_&#]*)?"


class UrlField(RegexpField):
    """
    Simple pattern to match http or https URL.
    """

    def __init__(self, protocol=None, domain=None, path=None, *args, **kwargs):
        if protocol:
            protocol = re.escape(protocol + "://")
        else:
            protocol = PROTOCOL
        if domain:
            domain = re.escape(domain)
        else:
            domain = DOMAIN
        if path:
            path = "/" + re.escape(path.lstrip("/"))
        else:
            path = PATH
        pattern = r"^{protocol}{domain}{path}{query}{hash}$".format(
            protocol=protocol, domain=domain, path=path, query=QUERY,
            hash=HASH)
        super(UrlField, self).__init__(pattern, "url", *args, **kwargs)
