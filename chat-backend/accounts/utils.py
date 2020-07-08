from secrets import token_hex
from rest_framework_simplejwt.tokens import RefreshToken


def get_private_user_id():
    return token_hex(16)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }