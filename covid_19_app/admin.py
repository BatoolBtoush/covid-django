from django.contrib import admin
from .models import CountryData

# Register your models here.


@admin.register(CountryData)
class CountryDataAdmin(admin.ModelAdmin):
    list_display = ("country", "date")
    list_filter = ("country", "date")
    search_fields = ("country", "date")
