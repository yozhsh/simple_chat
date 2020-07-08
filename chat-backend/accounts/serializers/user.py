from rest_framework import serializers
from django.contrib.auth import get_user_model


class User(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = get_user_model()
        fields = ['id', 'email']

    def get_email(self, user):
        return user.username
