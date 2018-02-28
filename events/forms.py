from django.forms import ModelForm

from .models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['approved']
