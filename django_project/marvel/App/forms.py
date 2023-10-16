from django import forms
from . models import *


class bas_form(forms.ModelForm):
    class Meta:
        model=bas_db
        fields='__all__'