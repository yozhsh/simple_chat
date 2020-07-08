from rest_framework import serializers
from accounts.models.user_profile import Profile as ProfileModel
from .user import User as UserSerializer


class Profile(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = ProfileModel
        fields = ['id', 'user', 'visible_name', 'user_own_id']
