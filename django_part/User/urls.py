from django.urls import path
from . import views
from django.template.loaders.filesystem import Loader

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
]
