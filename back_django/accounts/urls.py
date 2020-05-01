from django.urls import path

from accounts.views import SignupAPI, LoginAPI

urlpatterns = [
    path("api/register", SignupAPI.as_view()),
    path("api/login", LoginAPI.as_view()),
]
