from django.contrib import admin
from .models import Car
# Register your models here.

from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def show_photo(self, object):
        return format_html(f"<img src='{object.car_photo.url}' width=40>")

    show_photo.short_description = "Car Photo" 
    list_display = ("id","show_photo","car_title", "city","model","year","color","body_style","fuel_type","is_featured")
    list_display_links = ("id","car_title","show_photo")
    list_editable  = ("is_featured",)
    search_fields = ("car_title","city","model")
    list_filter  = ("city","model","body_style","fuel_type")

admin.site.register(Car, CarAdmin)
