"""
This package contains most frequently used subclasses of
:class:`dict_validator.fields.RegexpField`

 - :class:`EmailField`
 - :class:`PhoneField`
 - :class:`UrlField`
 - :class:`NameField`
 - :class:`SlugField`
.
"""

from .email_field import EmailField
from .phone_field import PhoneField
from .url_field import UrlField
from .name_field import NameField
from .slug_field import SlugField

__all__ = ["EmailField", "PhoneField", "UrlField", "NameField", "SlugField"]
