import datetime

from django import forms
from django.core.validators import MinValueValidator
from django.forms.widgets import DateInput, RadioSelect

from .models import Spaceship


def get_min_date():
    """Возвращает текущую дату, увеличенную на 4 недели."""
    return datetime.date.today() + datetime.timedelta(weeks=4)


class OrderForm(forms.Form):
    ship = forms.ModelChoiceField(
        queryset=Spaceship.objects,
        label='На чем летим',
        widget=RadioSelect
    )
    flight_date = forms.DateField(
        label='Когда летим',
        # установили валидатор минимальной даты на бэкенде
        # внимание: даже если валидатор один, он должен передаваться в списке
        validators=[MinValueValidator(get_min_date)],
        widget=DateInput(
            attrs={
                # переопределили атрибут `type` тега инпут, чтобы 
                # вместо поля для ввода текста отображался календарь
                'type': 'date',
                # установили валидатор минимальной даты на фронтенде
                # при каждом рендеринге страницы атрибут min тега input 
                # будет меняться в зависимости от текущей даты
                'min': get_min_date
            }
        )
    )
