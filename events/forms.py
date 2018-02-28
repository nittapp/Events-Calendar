from django.forms import ModelForm, DateTimeField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from bootstrap3_datetime.widgets import DateTimePicker

from .models import *


class CustomDateTimePicker(DateTimePicker):
    def __init__(self, *args, **kwargs):
        super(CustomDateTimePicker, self).__init__(*args, **kwargs)

    def _format_value(self, value):
        return value


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['approved']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Submit'))

    dt_options = {
        "format": "YYYY-MM-DD HH:mm",
        "pickSeconds": False
    }
    start = DateTimeField(widget=CustomDateTimePicker(options=dt_options))
    end = DateTimeField(widget=CustomDateTimePicker(options=dt_options))
