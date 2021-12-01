from django.shortcuts import render

from .forms import OrderForm


def main_page(request):
    return render(request, template_name='main.html')


def flight_details(request):
    form = OrderForm()
    ship_images = [ship.image.url for ship in form.fields['ship'].queryset]
    ship_field = zip(form['ship'], ship_images)
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
    return render(
        request,
        template_name='ship.html',
        context={
            'space_form': form,
            'ship_field': ship_field
        }
    )
