from django.urls import path

from accounts.apis import (
    UserListAPI,
    SignupAPI,
    LoginAPI,
    PasswordResetAPI,
    FindAccountAPI,
)

urlpatterns = [
    path("api/user", UserListAPI.as_view()),
    path("api/login", LoginAPI.as_view()),
    path("api/signup", SignupAPI.as_view()),
    path("api/findaccount", FindAccountAPI.as_view()),
    path("api/passwordreset/<int:pk>", PasswordResetAPI.as_view()),
]
