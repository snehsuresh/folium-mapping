import folium
import pandas
#help(folium.Map to view more parameters and arguments)
data = pandas.read_csv("Volcanoes.txt");

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])



map = folium.Map(location=[34.586, -117.868],zoom_start=8, tiles="OpenStreetMap" )
fg = folium.FeatureGroup("My Map")


for lat,lon,elev in zip(latitude, longitude, elevation):    #when you iterate through 2 lists, use zip fun
    fg.add_child(folium.Marker(location=[lat,lon], popup=str(elev) + "m", icon=folium.Icon(color='red')))
#popup only takes strings
map.add_child(fg)

map.save("map1.html")


#***************to use html in this*************************
#html = """<h4>Volcano information:</h4>
#Height: %s m
#"""

#map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
#fg = folium.FeatureGroup(name = "My Map")

#for lt, ln, el in zip(lat, lon, elev):
#    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
#    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))


#T*****************he following code does a google search of the link in the popup*************
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
