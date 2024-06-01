from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from el_mundo.forms import *
from el_mundo.models import *


def view_homepage(request):
    return render(request, 'world_map.html')


def country_info(request, country_name):
    country = Countries.objects.get(name=country_name)
    language = Languages.objects.filter(languagesbycountries__country=country)
    curr = country.currency
    languages_list = [lang.name for lang in language]
    context = {'country': country,
               'curr': curr,
               'languages_list': languages_list}
    return render(request, 'country_info.html', context=context)


def countries_form_view(request):
    initial_value = Languages.objects.order_by('name').first()
    form = LanguagesForm(initial={'languages': initial_value})

    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            selected_language = form.cleaned_data['languages']
            countires = Countries.objects.filter(languagesbycountries__language=selected_language)
            context = {'countries': countires,
                       'language': selected_language,
                       'selected_language': selected_language}
            return render(request, 'countries.html', context=context)
        else:
            form = LanguagesForm
            context = {'form': form}
            return render(request, 'countries.html',  context=context)

    return render(request, 'countries.html', {'form': form})


def all_data(request):
    countries = Countries.objects.all()
    languages = Languages.objects.all().order_by('name')
    currency = Currency.objects.all().order_by('name')
    context = {'countries': countries,
               'languages': languages,
               'currency': currency}
    return render(request, 'all_data.html', context=context)


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context=context)


def sign_out(request):
    logout(request)
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context=context)

