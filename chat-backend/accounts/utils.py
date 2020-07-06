from secrets import token_hex


def get_private_user_id():
    return token_hex(16)