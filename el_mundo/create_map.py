import folium

from el_mundo.models import *


# Add GeoJSON layer with dynamic popups
def style_function(feature):
    return {
        "fillColor": "transparent",
        "color": "black",
        "weight": 0,
        "fillOpacity": 0.5,
    }


def highlight_function(feature):
    return {
        "fillColor": "lightblue",
        "color": "red",
        "weight": 0,
        "fillOpacity": 0.7,
        "dashArray": 0,
    }

file_name = 'fixtures/geojson_data.json'
with open(file_name, 'r') as json_file:
    geojson_data = json.load(json_file)


m = folium.Map(location=[49.0, 32.0],
               zoom_start=5,
               max_zoom=6,
               min_zoom=3,
               zoom_control=True,
               tiles='cartodb positron'
               )

# Filter out Russia from the GeoJSON data
filtered_data = {
    "type": "FeatureCollection",
    "features": [
        f for f in geojson_data["features"]
        if f["properties"]["name"] != "Russia"
    ]
}

countries = Countries.objects.all()
popups_dict = {}
for country in countries:
    population_str = '{:,}'.format(country.population).replace(',', '.')
    languages_by_country = Languages.objects.filter(languagesbycountries__country=country)

    lang_str = f"<ul>" + "".join(f"<li>{lang.name}</li>" for lang in languages_by_country) + "</ul>"

    popup_html = f"<a href='http://127.0.0.1:8000/el_mundo/country/{country.name}'><b>{country.name}</b></a><br><br>" \
                 f"<b>Population:<b> {population_str}<br><br>" \
                 f"<b>Language:<b><br>" \
                 f"{lang_str}"

    popups_dict[country.name] = popup_html

for feature in geojson_data["features"]:
    country_name = feature["properties"]["name"]
    if country_name in popups_dict:
        feature["properties"]["popup_html"] = popups_dict[country_name]
    else:
        feature["properties"]["popup_html"] = f"<b>{country_name}</b><br>No data"

folium.GeoJson(
    filtered_data,
    style_function=style_function,
    highlight_function=highlight_function,
    popup=folium.GeoJsonPopup(
        fields=["popup_html"],
        localize=True,
        labels=False,
        parse_html=True
    )
).add_to(m)

m.save('templates/map.html')
