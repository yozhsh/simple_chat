from django.urls import reverse
from accounts.models import Profile
import pytest


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
def make_user_request(client, user_data):
    def _create():
        return client.post(path=reverse('accounts:registration'), data=user_data())
    return _create

@pytest.mark.django_db
def test_registration(client, user_data, make_user_request):
    data = user_data()
    response = make_user_request()
    assert response.status_code == 201


@pytest.mark.django_db
def test_is_user_exist_after_registration(user_data, make_user_request):
    data = user_data()
    make_user_request()
    profile = Profile.objects.filter(user__username=data['email']).first()
    assert profile.visible_name == data['visible_name']


@pytest.mark.django_db
def test_identity_user(user_data, make_user_request):
    data = user_data()
    make_user_request() # first time create user
    response = make_user_request() # in response you will be get BadRequest
    assert response.status_code == 400


@pytest.mark.django_db
def test_password_not_in_response(user_data, make_user_request):
    data = user_data()
    response = make_user_request()
    assert response.json()['email']


