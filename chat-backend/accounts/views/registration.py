from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from accounts.serializers import UserRegistration


class RegistrationProfile(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserRegistration
