from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware

header_prefix = "HTTP_" # The prefix used when placing headers into the WSGI environ

def parse_headers(request):
    headers = request.META
    return {
        'is_admin': headers.get(header_prefix + "X_NITT_APP_IS_ADMIN", None) == "true",
        'name': headers.get(header_prefix + "X_NITT_APP_NAME", ""),
        'user_name': headers.get(header_prefix + "X_NITT_APP_USERNAME", "")
    }


def is_admin(request, **kwargs):
    return parse_headers(request)['is_admin']


def admin_route(view):
    def wrapper(*args, **kwargs):
        if is_admin(*args, **kwargs):
            return view(*args, **kwargs)
        return redirect("events:events_list")

    return wrapper
