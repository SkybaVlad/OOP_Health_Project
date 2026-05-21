from django.urls import path
from . import views

urlpatterns = [
    path("", views.daily_tracking, name="daily_tracking"),
]
