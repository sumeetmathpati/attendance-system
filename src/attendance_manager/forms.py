from django.forms import ModelChoiceField, EmailField, Form, DateField, DateTimeField, DateTimeInput
from .models import Class
from datetime import datetime


# class TakeAttendance(forms.Form):
#     email = forms.EmailField()

#     class Meta():
#         model = Class
#         fields = ['title']

class MyDateInput(DateTimeInput):
    input_type = 'datetime-local'


class TakeAttendance(Form):

    # email = EmailField(readonly = True).attrs['readonly']
    class_name = ModelChoiceField(queryset=Class.objects.all(), to_field_name="title")
    from_date= DateTimeField(widget=MyDateInput)
    to_date = DateTimeField(widget=MyDateInput)
