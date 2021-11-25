from django import forms
from django.forms.widgets import RadioSelect

from .models import Spaceship


class OrderForm(forms.Form):
    ship = forms.ModelChoiceField(
        queryset=Spaceship.objects,
        label='На чем летим',
        widget=RadioSelect
    )
