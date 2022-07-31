from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def show_photo(self, object):
        return format_html(f"<img src='{object.photo.url}' width=40>")

    show_photo.short_description = "Photo" 
    list_display = ("id","show_photo","first_name","designation", "created_date")
    list_display_links = ("first_name","id","show_photo")
    search_fields = ("first_name","designation")
    list_filter = ("designation",)

admin.site.register(Team, TeamAdmin)