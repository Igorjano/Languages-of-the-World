import folium

from el_mundo.models import *


m = folium.Map(location=[49.0, 32.0],
               zoom_start=5,
               max_zoom=6,
               min_zoom=3,
               zoom_control=True,
               tiles='cartodb positron'
               )


countries = Countries.objects.all()
for i in range(len(countries) - 1):

    countries[i].population = '{:,}'.format(countries[i].population)
    languages_by_country = Languages.objects.filter(languagesbycountries__country=countries[i])

    lang_str = f"<ul>"
    for lang in languages_by_country:
        lang_str += f"<li>{lang.name}</li>"
    lang_str += "</ul>"

    popup_html = f"<a href='http://127.0.0.1:8000/el_mundo/country/{countries[i].name}'><b>{countries[i].name}</b></a><br><br>"\
                 f"<b>Population:<b> {countries[i].population}<br><br>"\
                 f"<b>Language:<b><br>"\
                 f"{lang_str}"

    print(lang_str)

    if countries[i].name == 'Russia':
        continue
    marker = folium.CircleMarker(location=(countries[i].lat, countries[i].long),
                                 color='#696969',
                                 fill_color='#006400',
                                 radius=5,
                                 fill_opacity=0.8,
                                 popup=folium.Popup(popup_html),
                                 parse_html=True).add_to(m)


m.save('templates/map.html')







