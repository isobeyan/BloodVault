from django.core import validators
from django import forms
from .models import Member


class MemberReg(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'group': forms.TextInput(attrs={'class': 'form-control'}),
        }