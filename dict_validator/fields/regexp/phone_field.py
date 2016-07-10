""" dict_validator.fields.regexp.phone_field """

from ..regexp_field import RegexpField


class PhoneField(RegexpField):
    """
    Make sure that the input is a valid phone number.

    Valid phone: +35833442332, +3435 35 3434
    Invalid phone: 03040000033
    """

    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(
            r"^\+[0-9]{1,4}[ 0-9]+$", "phone",
            *args, **kwargs)

    def deserialize(self, value):
        return value.replace(" ", "")
