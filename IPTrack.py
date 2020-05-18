import geoip2.database
from flask import Flask,render_template,request
import folium
import webbrowser
app = Flask(__name__)
reader=geoip2.database.Reader('./GeoLite2-City_20200428/GeoLite2-City.mmdb')

@app.route('/profile1/',methods=['post','get'])
def profile():
	ip=request.form('ip')
	response=reader.city(ip)
	lat=response.location.latitude
	lang=response.location.longitude
	m=folium.Map(location=[lat,lang],zoom_start = 15)
	folium.Marker(location=[lat,lang],icon=folium.Icon(color='red')).add_to(m)
	# m.save('index.html')
	# m=folium.Map(location=[28.1253,26.1523],zoom_start=2)
	# folium.Marker(location=[28.1253,26.1523],icon=folium.Icon(color='red')).add_to(m)
	m.save('C:\\Users\\Rakesh\\Desktop\\Ip\\index.html')
	webbrowser.open_new_tab("C:\\Users\\Rakesh\\Desktop\\Ip\\templates\\file1.html")

webbrowser.open_new_tab("C:\\Users\\Rakesh\\Desktop\\Ip\\templates\\file1.html")












# print(response.country.name)
# print(response.country.iso_code)
# print(response.location.latitude)
# print(response.location.longitude)
# print(response.city.name)
# print(response.postal.code)
# print(response.subdivisions.most_specific.name)
if __name__ == '__main__':
    app.run()