from django.core.validators import validate_email


class EmailValidateSerializerMixin(object):
    def validate_email(self, value):
        validate_email(value)
        return value
