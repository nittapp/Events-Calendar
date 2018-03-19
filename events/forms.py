from django.forms import Form, ModelForm, ModelChoiceField

from .models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['approved']

class CategoryDeleteForm(Form):
    category = ModelChoiceField(queryset=Category.objects.all(), required=True)