import folium
# from el_mundo.models import *

m = folium.Map(location=[49.0, 32.0],
               zoom_start=5,
               max_zoom=6,
               min_zoom=3,
               zoom_control=True,
               tiles='cartodb positron'
               )

folium.Marker(location=[33, 65], popup='Afganistan').add_to(m)

# countries = Countries.objects.all()
# for i in range(len(countries) - 1):
#     folium.Marker(location=[countries[i].lat, countries[i].long], popup=countries[i].name).add_to(m)
#     print(f'{countries[i].name} was added to the map')

m.save('map.html')
