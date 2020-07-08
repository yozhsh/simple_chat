from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.mixins import EmailValidateSerializerMixin
from .validators import login_data_validate


class UserLogin(serializers.ModelSerializer, EmailValidateSerializerMixin):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        login_data_validate(attrs)
        return attrs

