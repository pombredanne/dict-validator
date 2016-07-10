""" dict_validator.fields.regexp.slug_field """

from ..regexp_field import RegexpField


class SlugField(RegexpField):
    """
    Lower case alphanumerics delimited with dashes.
    """

    def __init__(self, *args, **kwargs):
        super(SlugField, self).__init__(
            r"^[a-z0-9]+(-[a-z0-9]+)*$",
            "slug", *args, **kwargs)
