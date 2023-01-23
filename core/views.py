from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:

    context = {
        "django_message": "Hello from Django!",
        "vue_message": "This message has been passed to a Vue component from a Django view.",
        "initial_value": 1000
    }

    return render(request, "index.html", context)