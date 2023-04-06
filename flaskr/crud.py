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
    
    for station in stations:
        html = """
                <head>
                <base target="_parent">
                </head>
                <div class="card text-center" style="max-width: 22rem;">
                    <img class="card-img-top" src="" alt="an image should be here..." style="max-width: 20rem;">
                        <div class="card-body">
                            <h4 class="card-title fw-bold"
                                style="text-shadow: #cc9a07 0 1px 1px;">{0}</h4>
                            <h4 class="card-title" 
                                style="color: green; text-shadow: #a3cfbc 1px 0 3px;">{2}</h4>
                            <h6 class="card-text" style="font-style: italic;">{3}</h6>
                            <h4 style="color: #f4c109; font-weight:bold; text-shadow: #172c65 0 1px 1px;">{5} ⭐️ 
                                <span style="font-style:italic; font-size: smaller;"> ({6})</span></h4>
                            <a type="button" 
                                href="{4}" 
                                class="btn btn-primary btn-sm" 
                                style="color:white;">See Details</a>
                        </div>
                </div>
        """
        popup = folium.Popup(html.format())
    
    return station_map