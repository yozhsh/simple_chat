from django.urls import path
from .views import RegistrationProfile, LoginUser

app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationProfile.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login')
]