import pytest
from django.urls import reverse


@pytest.fixture
def user_data():
    def _get_data():
        return {
            'email': 'user@test.com',
            'password': 'qwerty',
            'visible_name': 'just_test_user'
        }
    return _get_data


@pytest.fixture
def registrate_user(client, user_data):
    def _create():
        return client.post(path=reverse('accounts:registration'), data=user_data())
    return _create


@pytest.fixture
def login_user(client, user_data):
    def _login():
        return client.post(path=reverse('accounts:login'), data=user_data())
    return _login