import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#function to add color points
def color_get(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"
#Create a map object with location zoom and background type
map = folium.Map(location=[38.52,-99.1], zoom_start=6, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name="Volcanoes")
#Add multiple markers to the map using txt data of volcanoes
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6,popup=str(el)+" m",
    fill_color=color_get(el),color='grey',fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")
#Add population data using GeoJson
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
 style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']< 10000000
 else 'orange' if 10000000<=x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)

#Always remember to put LayerControl after ading the child otherwise no add layers will  appear in output
map.add_child(folium.LayerControl())
map.save("Map1.html")
