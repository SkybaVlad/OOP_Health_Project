from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView


def registration(request: HttpRequest) -> HttpResponse:

    # this view should provide page for entering user credentials

    return render(request, "accounts/registration.html")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")


class LoginCLass(FormView):
    template_name = "accounts/login.html"


def logout(request: HttpRequest) -> HttpResponse:

    # this view should redirect user to REGISTER page

    return render(request, "accounts/logout.html")


def main_view(request: HttpRequest) -> HttpResponseRedirect:
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    return redirect(reverse(viewname="login"))
