from django import forms
from .models import usersignup,notes

class signupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'