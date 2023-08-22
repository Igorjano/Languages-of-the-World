import requests
from concurrent.futures import ThreadPoolExecutor
import json
import time


def main():
    start = time.time()
    file_name = 'fixtures/countries_data.json'
    url = 'https://restcountries.com/v3.1/all'

    response = requests.get(url)
    data = response.json()

    countries_data = []
    with ThreadPoolExecutor(max_workers=200) as executor:
        for country in data:
            future = executor.submit(clean_data, country)
            countries_data.append(future.result())
            countries_data = sorted(countries_data, key=lambda name: name['name'])

    with open(file_name, 'w') as json_file:
        json.dump(countries_data, json_file, indent=4)

    end = time.time() - start

    print(end)


def get_country_description(name):
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{name}'
    response = requests.get(url)
    data = response.json()
    description = data['extract']

    return description


def clean_data(data):
    new_data = {}
    new_data['name'] = data['name']['common']
    new_data['description'] = get_country_description(new_data['name'])
    new_data['capital'] = data.get('capital', 'NULL')
    new_data['continent'] = data['continents']
    new_data['flag'] = data['flags']['png']
    new_data['population'] = data['population']
    new_data['languages'] = data.get('languages', 'NULL')
    new_data['currencies'] = data.get('currencies', 'NULL')
    new_data['lat'] = data['latlng'][0]
    new_data['long'] = data['latlng'][1]
    new_data['timezones'] = data['timezones']
    new_data['currencies'] = data.get('currencies', 'NULL')

    return new_data


if __name__ == '__main__':
    main()
