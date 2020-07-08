from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError


def _is_account_exist(user):
    if not user:
        raise ValidationError(detail={
            'non_field_errors': ['Account does not exist']
        })


def _check_password(user, raw_password: str):
    if not user.check_password(raw_password):
        raise ValidationError(detail={
            'password': ['Password is incorrect']
        })


def login_data_validate(attrs):
    email, password = attrs.get('email'), attrs.get('password')
    user_model = get_user_model()
    user = user_model.objects.filter(username=email).first()

    _is_account_exist(user)
    _check_password(user, password)

    # add user_instance manually
    attrs['user_instance'] = user
    return attrs


__all__ = ('login_data_validate',)