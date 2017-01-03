from dict_validator import Field


class WildcardDictField(Field):
    """
    Match a dict with any dict with any key/value pairs.

    >>> from dict_validator import validate, describe

    >>> class Schema:
    ...     field = WildcardDictField()

    >>> list(validate(Schema, {"field": {}}))
    []

    >>> list(validate(Schema, {"field": 11}))
    [(['field'], 'Not a dict')]

    >>> list(describe(Schema))
    [([], {'type': 'Dict'}), (['field'], {'type': 'WildcardDict'})]

    """

    @property
    def _type(self):
        return "WildcardDict"

    def _validate(self, value):
        if not isinstance(value, dict):
            return "Not a dict"
