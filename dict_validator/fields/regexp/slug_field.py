from dict_validator.fields import RegexpField


class SlugField(RegexpField):
    """
    Lower case alphanumerics delimited with dashes.

    >>> from dict_validator import validate

    >>> class Schema:
    ...     field = SlugField()

    >>> list(validate(Schema, {"field": 'title-of-web-page'}))
    []
    """

    def __init__(self, *args, **kwargs):
        super(SlugField, self).__init__(
            r"^[a-z0-9]+(-[a-z0-9]+)*$",
            "slug", *args, **kwargs)
