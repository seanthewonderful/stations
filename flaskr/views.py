from flask import render_template, redirect, request
from flaskr import app, simple_geoip
from flaskr.crud import make_map, get_all_stations
from os import environ, system
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import folium


@app.route('/')
def home():
    """Homepage"""
    
    variable = ["Bucee's", "QuikTrip", "Maverik", "Pilot"]
    
    return render_template("homepage.html", 
                           variable=variable)

@app.route('/map')
def display_map():
    
    user_location = (40.41930265443319, -111.8746632089035)
    # all_stations = get_all_stations()
    
    m = make_map(location=user_location, 
                 stations=[1,2])

    return m.get_root().render()


"""Route to return user's geolocation data """
@app.route('/geopi/')
def geopi():
    
    addr = request.remote_addr
    
    geopi_data = simple_geoip.get_geoip_data(addr)
    
    return geopi_data