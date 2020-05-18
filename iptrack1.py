from flask import Flask,render_template,request
import geoip2.database
import folium
reader=geoip2.database.Reader('./GeoLite2-City_20200428/GeoLite2-City.mmdb')
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("file1.html")



if __name__=="__main__":
	app.run()