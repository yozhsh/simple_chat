from django.urls import path
from .views import RegistrationProfile

app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationProfile.as_view(), name='registration'),
]