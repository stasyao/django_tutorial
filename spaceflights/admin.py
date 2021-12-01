from django.contrib import admin
from django.utils.html import format_html

from spaceflights.models import Order, Spaceship



@admin.register(Spaceship)
class SpaceShipAdmin(admin.ModelAdmin):
    list_display = [
        'picture_preview', 'owner', 'name', 'flight_price', 'capacity'
    ]
    readonly_fields = ['picture_preview', ]

    @admin.display(description='Превью')
    def picture_preview(self, obj):
        return format_html(
            '<img src="{}"'
            'style="object-fit: cover; width:200px; height:150px;" />',
            obj.image.url
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['ship', 'passenger', 'flight_date']
