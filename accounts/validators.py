from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

'''
Base validation template:

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

'''

def valid_phone(value):
    if value[0]!=0:
        raise ValidationError(
            _('%(value)s a valid phone number.  Please input a valid phone number.'),
            params={'value': value},
        )
