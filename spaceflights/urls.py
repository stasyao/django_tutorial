from django.urls import path

from .views import flight_details, main_page


urlpatterns = [
    path('', main_page, name='main_page'),
    path('flight/', flight_details, name='flight_details'),
]
