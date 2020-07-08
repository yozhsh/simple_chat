from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import UserLogin
from accounts.serializers import Profile as ProfileSerializer
from accounts.utils import get_tokens_for_user


class LoginUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLogin

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user_instance')
        tokens = get_tokens_for_user(user)
        profile_data = ProfileSerializer(instance=user.profile)
        headers = self.get_success_headers(serializer.data)
        _profile_data = profile_data.data.copy()
        del _profile_data['user']
        response_data = {
            'profile': {**_profile_data, **profile_data.data.get('user')},
            'tokens': dict(**tokens)
        }
        return Response(response_data, status=status.HTTP_200_OK, headers=headers)


