from django import forms
from . models import *

class Bas_form(forms.ModelForm):
    class Meta:
        model=TASK
        fields='__all__'