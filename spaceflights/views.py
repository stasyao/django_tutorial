from django.shortcuts import render

from .forms import OrderForm


def main_page(request):
    return render(request, template_name='main.html')


def flight_details(request):
    form = OrderForm()
    return render(
        request,
        template_name='ship.html',
        context={'space_form': form}
    )
