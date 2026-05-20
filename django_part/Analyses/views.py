from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def get_analysis(request: HttpRequest) -> HttpResponse:
    return render(request, "analyses.html")
