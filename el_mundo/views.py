from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from geojson import Feature, FeatureCollection

from el_mundo.models import *




def login(request):
    return render(request, 'login.html')


def view_homepage(request):
    return render(request, 'world_map.html')


def country_info(request, country_name):
    country = Countries.objects.get(name=country_name)
    language = Languages.objects.filter(languagesbycountries__country=country)
    curr = country.currency
    # currency_list = [cur.name for cur in currencies]
    languages_list = [lang.name for lang in language]
    context = {'country': country,
               # 'currency_list': currency_list,
                'curr': curr,
               'languages_list': languages_list}
    return render(request, 'country_info.html', context=context)


def countries(request):
    countries = Countries.objects.all()
    count_countries = Countries.objects.count()
    context = {'countries': countries,
               'count_countries': count_countries}
    return render(request, 'countries.html', context=context)


def currency(request):
    currency = Currency.objects.all()
    context = {'currency': currency}
    return render(request, 'currency.html', context=context)


def languages(request):
    languages = Languages.objects.all()
    context = {'languages': languages}
    return render(request, 'languages.html', context=context)


def all_data(request):
    countries = Countries.objects.all()
    languages = Languages.objects.all()
    currency = Currency.objects.all()
    context = {'countries': countries,
               'languages': languages,
               'currency': currency}
    return render(request, 'all_data.html', context=context)

