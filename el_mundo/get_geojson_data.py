import requests
import json


def main():
    file_name = 'fixtures/geojson_data.json'
    url = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json'
    response = requests.get(url)
    geojson_data = response.json()

    with open(file_name, 'w') as json_file:
        json.dump(geojson_data, json_file, indent=4)


if __name__ == '__main__':
    main()
