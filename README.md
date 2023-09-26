# Volcano Map Visualization with Folium

This Python script generates an interactive map using the Folium library to visualize volcano data from a CSV file. The map shows volcano locations, names, and elevations, and it uses color-coding to represent different elevation ranges.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- Folium
- Pandas
You can install them using pip

### Usage

The map displays volcano locations with markers.
Clicking on a marker displays a popup with the volcano name and elevation.
The marker colors indicate different elevation ranges (green, orange, and red).
A population layer is added to the map, displaying country population data with color-coding.
The map includes a layer control to toggle between volcano data and population data.

### Customization

You can customize the map's initial location and zoom level by modifying the folium.Map() parameters in the code.
```python
map = folium.Map(location=[34.586, -117.868], zoom_start=8, tiles="OpenStreetMap")
You can change the color-coding logic for elevations by editing the color() function.
```

### Attribution
The volcano data in "Volcanoes.txt" is assumed to be in the format of latitude, longitude, elevation, and name.
The population data is sourced from "world.json," which provides country-level population information.
