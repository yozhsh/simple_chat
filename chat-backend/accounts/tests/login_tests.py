from django.urls import reverse
from .fixtures import user_data, registrate_user, login_user
import pytest


@pytest.mark.django_db
def test_login(registrate_user, login_user):
    registrate_user()
    response = login_user()
    assert response.status_code == 200


