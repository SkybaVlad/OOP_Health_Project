from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def base_view(request: HttpRequest) -> HttpResponse:

    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))

    return redirect(reverse("login"))
