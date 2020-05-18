import geoip2.database
import folium
reader=geoip2.database.Reader('./GeoLite2-City_20200428/GeoLite2-City.mmdb')
response=reader.city('27.97.230.239')
m=folium.Map(location=[response.location.latitude,response.location.longitude],zoom_start = 15)
folium.Marker(location=[response.location.latitude,response.location.longitude],icon=folium.Icon(color='red')).add_to(m)
m.save('index.html')
print(response.country.name)
print(response.country.iso_code)
print(response.location.latitude)
print(response.location.longitude)
print(response.city.name)
print(response.postal.code)
print(response.subdivisions.most_specific.name)

