from accounts.models import Profile
import pytest
from .fixtures import registrate_user, user_data


@pytest.mark.django_db
def test_registration(registrate_user):
    response = registrate_user()
    assert response.status_code == 201


@pytest.mark.django_db
def test_is_user_exist_after_registration(user_data, registrate_user):
    data = user_data()
    registrate_user()
    profile = Profile.objects.filter(user__username=data['email']).first()
    assert profile.visible_name == data['visible_name']


@pytest.mark.django_db
def test_identity_user(user_data, registrate_user):
    data = user_data()
    registrate_user() # first time create user
    response = registrate_user() # in response you will be get BadRequest
    assert response.status_code == 400


@pytest.mark.django_db
def test_password_not_in_response(registrate_user):
    response = registrate_user()
    assert response.json()['email']


