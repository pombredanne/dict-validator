# dict-validator

Validator for structural data in Python. Understands dicts, lists, primitives.

Supports extension with custom types.

## Builtin types (imports)

    from dict_validator import describe, validate, serialize, deserialize
    from dict_validator import Field
    from dict_validator import ListField, DictField

    from dict_validator.fields import BooleanField
    from dict_validator.fields import ChoiceField
    from dict_validator.fields import NumberField
    from dict_validator.fields import RegexpField
    from dict_validator.fields import StringField
    from dict_validator.fields import TimestampField

    from dict_validator.fields.regexp import EmailField
    from dict_validator.fields.regexp import NameField
    from dict_validator.fields.regexp import PhoneField
    from dict_validator.fields.regexp import SlugField
    from dict_validator.fields.regexp import UrlField

## Usage

    class Schema:
        child = StringField()

    print list(validate(Schema, {"child": "foobar"}))
    >>> []
    print list(validate(Schema, {"child": 11}))
    >>> [(['child'], 'Not a string')]
