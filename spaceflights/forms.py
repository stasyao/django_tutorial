import datetime

from django import forms
from django.core.validators import MinValueValidator
from django.forms.widgets import DateInput, RadioSelect

from .models import Order


def get_min_date():
    """Возвращает текущую дату, увеличенную на 4 недели."""
    return datetime.date.today() + datetime.timedelta(weeks=4)


class OrderForm(forms.ModelForm):
    flight_date = forms.DateField(
        label='Когда летим',
        validators=[MinValueValidator(get_min_date), ],
        widget=DateInput(
            attrs={
                'type': 'date',
                'min': get_min_date
            }
        )
    )

    currency = forms.ChoiceField(
        choices = (
            ('RUB', 'Российский рубль'),
            ('USD', 'Доллар США')
        ),
        label='Валюта платежа'
    )

    class Meta:
        model = Order
        fields = ['ship', 'flight_date', 'currency']
        widgets = {'ship': RadioSelect}
        labels = {'ship': 'На чем летим'}

    def clean(self):
        flight_date = self.cleaned_data['flight_date']
        ship = self.cleaned_data['ship']
        existing_orders = Order.objects.filter(flight_date=flight_date,
                                               ship=ship).count()
        if existing_orders >= ship.capacity:
            raise forms.ValidationError(
                'К сожалению, на эту дату мест нет. '
                'Пожалуйста, выберите другую дату или другой корабль.'
            )
