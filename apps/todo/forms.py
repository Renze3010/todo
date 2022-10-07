from django import forms
from django.conf import settings

from .models import Todo

class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'

# creating a form
class TodoForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = Todo
  
        # specify fields to be used
        fields = [
            "name",
            "description",
            "deadline"
        ]

    deadline = forms.DateField(widget=MyDateInput())

