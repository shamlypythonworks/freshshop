from django import forms
from . models import *

class registertbleForm(forms.ModelForm):
    paswd = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = registertble
        fields = ('fullname', 'email', 'paswd','repaswd')