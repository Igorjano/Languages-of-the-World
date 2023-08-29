from django.contrib import admin
from el_mundo.models import *


class CountriesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Capital', {'fields': ['capital']}),
        ('Population', {'fields': ['population']}),
        ('Coordinates', {'fields': ['lat', 'long']}),
        ('Currency', {'fields': ['currency']})
    ]
    list_display = ['name', 'capital', 'population', 'lat', 'long', 'currency']
    list_filter = ['currency']
    search_fields = ['name']


class CurrencyAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['name']}),
                ('Sign', {'fields': ['sign']})
                ]
    list_display = ['name', 'sign']
    list_filter = ['name']
    search_fields = ['sign']


class LanguagesAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['name']}),
                ('Sign', {'fields': ['sign']})
                ]
    list_display = ['name', 'sign']


class LanguagesByCountriesAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['country']}),
                ('Language', {'fields': ['language']})
                ]
    list_display = ['country', 'language']
    list_filter = ['language']
    search_fields = ['language']


admin.site.register(Countries, CountriesAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(LanguagesByCountries, LanguagesByCountriesAdmin)
