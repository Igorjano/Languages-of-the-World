from el_mundo.models import *
import json


Countries.objects.all().delete()
Currency.objects.all().delete()
Languages.objects.all().delete()
LanguagesByCountries.objects.all().delete()


def fill_languages_by_countries(data):
    for country in data:
        country_name = Countries.objects.get(name=country['name'])
        print('COUNTRY NAME:', country_name.name)
        language = list(country['languages'].values())
        print('LANGUAGE', language)
        if len(language) > 1:
            for lang in language:
                lang_name = Languages.objects.get(name=lang)
                new_country = LanguagesByCountries(country_id=country_name.id,
                                                   language_id=lang_name.id)
                new_country.save()
                print(f'{new_country} was saved')
        else:
            lang = language[0]
            print(F'LANG', lang)
            lang_name = Languages.objects.get(name=lang)
            print(f'LANG NAME', lang_name)
            new_country = LanguagesByCountries(country_id=country_name.id,
                                               language_id=lang_name.id)
            new_country.save()
            print(f'{new_country} was saved')


def fill_countries(data):
    for country in data:
        if country['currencies'] != 'NULL':
            currency_sign = country['currencies'].keys()
            currency_sign = list(currency_sign)[0]
            currency = Currency.objects.get(sign=currency_sign)
            new_country = Countries(name=country['name'],
                                    description=country['description'],
                                    capital=country['capital'][0],
                                    population=country['population'],
                                    lat=country['lat'],
                                    long=country['long'],
                                    currency_id=currency.id)
            new_country.save()


def fill_languages(data):
    for language in data:
        for sign, name in language.items():
            new_language = Languages(name=name,
                                     sign=sign)
            new_language.save()


def fill_currency(data):
    for currency in data:
        for name, sign in currency.items():
            new_currency = Currency(name=name,
                                    sign=sign)
            new_currency.save()


def prepare_continent_data(country, area, continents):
    print(country)
    if len(country[area]) > 1:
        country[area].split()
    if country[area] not in continents:
        continents.append(country[area])


def prepare_language_data(country, area, languages):
    if len(country[area]) > 1:
        for sign, name in country[area].items():
            if {sign: name} not in languages:
                languages.append({sign: name})
    elif country[area] not in languages:
        languages.append(country[area])

    return languages


def prepare_currency_data(country, area, currencies):
    currency_sign = country[area].keys()
    currency_sign = list(currency_sign)[0]
    currency_name = country[area][currency_sign]['name']
    if {currency_name: currency_sign} not in currencies:
        currencies.append({currency_name: currency_sign})

    return currencies


def prepare_data(data, area):
    new_data = []
    for country in data:
        if country[area]:
            if area == 'currencies':
                prepare_currency_data(country, area, new_data)
            if area == 'languages':
                prepare_language_data(country, area, new_data)
            if area == 'continent':
                prepare_continent_data(country, area, new_data)

    return new_data


file = 'el_mundo/fixtures/countries_data.json'

with open(file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

currencies = prepare_data(data, 'currencies')
languages = prepare_data(data, 'languages')
# continents = prepare_data(data, 'continent')

fill_currency(currencies)
fill_languages(languages)
fill_countries(data)
fill_languages_by_countries(data)

