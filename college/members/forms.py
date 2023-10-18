from django import forms
from .models import *

class bas_form(forms.Form):
    name=forms.ModelChoiceField(queryset=batch.objects.all())
#     class meta:
#         model=student
#         fields='__all__'