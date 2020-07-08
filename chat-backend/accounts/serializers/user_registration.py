from accounts.mixins import EmailValidateSerializerMixin
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Profile


class UserRegistration(serializers.ModelSerializer, EmailValidateSerializerMixin):
    visible_name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'visible_name']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user_model = self.Meta.model
        if user_model.objects.filter(username=self.validated_data.get('email')).exists():
            raise serializers.ValidationError(
                detail={'email': [f"Email {self.validated_data.get('email')} is exist please choose another"]}
            )
        user = user_model(
            username=self.validated_data.get('email'),
        )
        user.set_password(self.validated_data.get('password'))
        user.save()
        visible_name = self.validated_data.get('visible_name')
        if visible_name:
            profile = Profile.objects.filter(user=user).first()
            profile.visible_name = visible_name
            profile.save()
        return user
