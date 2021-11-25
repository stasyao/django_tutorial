from django.contrib import admin

from spaceflights.models import Order, Spaceship


@admin.register(Spaceship)
class SpaceShipAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'flight_price', 'capacity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['ship', 'passenger', 'flight_date']
