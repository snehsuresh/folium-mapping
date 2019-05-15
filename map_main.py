import folium
import pandas
#help(folium.Map to view more parameters and arguments)
data = pandas.read_csv("Volcanoes.txt");

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

htmlpop = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


map = folium.Map(location=[34.586, -117.868],zoom_start=8, tiles="OpenStreetMap" )


def color(elevation):
        if elevation <= 1000:
            chosen_color = 'green'
        elif 1000<= elevation <3000:
            chosen_color = 'orange'
        else:
            chosen_color = 'red'
        return chosen_color



#feature group creates a class for all the elements, if we had used map.add_child instead of fg.add_child, it would create 62 layers as there are 62 volcanoes!
fgv = folium.FeatureGroup("Volcanoes")

for lat,lon,elev,name in zip(latitude, longitude, elevation,name):    #when you iterate through 2 lists, use zip fun
    #iframe = folium.IFrame(html = htmlpop % (name, name, elev), width =200, height=100)
    #fgv.add_child(folium.CircleMarker(location=[lat,lon], popup=folium.Popup(iframe), fill_color = color(elev), color = 'grey',fill_opacity=0.7))
    #popup only takes strings
    iframe = folium.IFrame(html=htmlpop % (name, name, elev), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))



fgp = folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':
'green' if x['properties']['POP2005'] < 10000000 else
'orange' if 10000000 <= x['properties']['POP2005'] <20000000
else 'red'}))




map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())        #always put layer control after adding feature group if there is one

map.save("map_googlesearch.html")

#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""

#map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
#fg = folium.FeatureGroup(name = "My Map")
#
#for lt, ln, el, name in zip(lat, lon, elev, name):
#    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
#    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

#map.add_child(fg)
#map.save("Map_html_popup_advanced.html")
