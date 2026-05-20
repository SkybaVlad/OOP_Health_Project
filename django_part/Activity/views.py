from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def activity_overview(request: HttpRequest) -> HttpResponse:
    return render(request, "activity/activity_overview.html")
