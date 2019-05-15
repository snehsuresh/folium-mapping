import folium

#help(folium.Map to view more parameters and arguments)
map = folium.Map(location=[9.129, 76.713],zoom_start=8 )



map.add_child(folium.Marker(location=[9.132428, 76.718013], popup="Here is my College", icon=folium.Icon(color='red')))

map.add_child(folium.Marker(location=[9.135044, 76.724287], popup="Here is my Hostel", icon=folium.Icon(color='green')))

map.save("CollegeMap.html")
