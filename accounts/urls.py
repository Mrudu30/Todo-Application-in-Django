from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.login_view, name="login_account"),
    path("signup/", v.signup_view, name="signup_account"),
    path("logout/", v.logout_view, name="logout_account"),
]
