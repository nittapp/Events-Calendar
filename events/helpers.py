from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware


def is_admin(request, **kwargs):
    # TODO Change this to actual authentication function
    return False


def admin_route(view):
    def wrapper(*args, **kwargs):
        if is_admin(*args, **kwargs):
            return view(*args, **kwargs)
        return redirect("events:events_list")

    return wrapper
