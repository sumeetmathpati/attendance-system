from django.forms import ModelChoiceField, EmailField, Form, DateField, DateTimeField
from .models import Class


# class TakeAttendance(forms.Form):
#     email = forms.EmailField()

#     class Meta():
#         model = Class
#         fields = ['title']


class TakeAttendance(Form):

    # email = EmailField(readonly = True).attrs['readonly']
    class_name = ModelChoiceField(queryset=Class.objects.all(), to_field_name="title")
    from_date = DateTimeField()
    to_date = DateTimeField( ) 

