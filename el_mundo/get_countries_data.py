import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests


def main():
    file_name = 'fixtures/countries_data_with_description.json'
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    data = response.json()
    os.makedirs('../static/images/flags', exist_ok=True)

    countries_data = []

    with ThreadPoolExecutor(max_workers=200) as executor:
        for country in data:
            future = executor.submit(clean_data, country)
            countries_data.append(future.result())
            print(f'{future.result()} was added')
            countries_data = sorted(countries_data, key=lambda name: name['name'])

        for country in countries_data:
            future = executor.submit(get_country_description, country['name'])
            country.update({'description': future.result()})
            print(f"{country['name']} description was added")

        for country in countries_data:
            executor.submit(get_country_flag, country['name'], country['flag'])

    with open(file_name, 'w') as json_file:
        json.dump(countries_data, json_file, indent=4)


def get_image_data(url):
    retries = 0
    max_retries = 10
    while retries < max_retries:
        response = requests.get(url)
        if response.ok:
            image_data = response.content
            return image_data
        else:
            retries += 1
    else:
        raise Exception(f"Received invalid response from url: {url}")


def get_country_flag(name, url):
    image_data = get_image_data(url)
    image_name = f'{name}.jpeg'
    path = os.path.join('../static/images/flags', image_name)
    with open(path, 'wb') as image_file:
        image_file.write(image_data)
        print(f'{name} was downloaded')


def get_country_description(name):
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{name}'
    response = requests.get(url)
    data = response.json()
    description = data['extract']

    return description


def clean_data(data):
    new_data = {}
    new_data['name'] = data['name']['common']
    new_data['description'] = ''
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
