import folium
from flaskr.model import Station

def get_all_stations():
    return Station.query.all()

def make_map(stations, location):
    
    lat = location[0]
    lng = location[1]
    
    station_map = folium.Map(location=[lat, lng], 
                             zoom_start=13,
                             tiles='https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
                             attr='Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC')
    
    # for station in stations:
    
    return station_map