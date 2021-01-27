from django.forms import ModelForm
from django import forms
from .models import Category,Invitations
class OrderForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class InvitaitonForm(forms.ModelForm):
    class Meta:
        model=Invitations
        fields='__all__'

