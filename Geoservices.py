import openrouteservice
import folium
from dotenv import load_dotenv
import os

load_dotenv()


coordinates_list ={"Haryana":[[77.09838732369364, 28.50036408080802],
                             [77.04502085438622,28.475792459532762],
                             [77.08699617059821,28.479827322463272],
                             [77.03921028731453,28.511857876980297],
                             [77.06608377935495,28.463136990100455],
                             [77.06166000301216,28.458209705407338],
                             [77.05427481328331,28.44128312008896]]
                  ,"Punjab":[[76.82881035326834,30.563361423039105],
                             [76.67821193640829,30.736973108669286],
                             [76.96984820055283,29.7487386062523]]
                  ,"Chandigarh":[[76.82881035326834,30.563361423039105],
                                 [76.67821193640829,30.736973108669286],
                                 [76.96984820055283,29.7487386062523]]
                  ,"Delhi":[[77.10127579844197,28.63924102573911],
                            [77.09701848388161,28.64130341687483]]
                  ,"Uttarakhand":[78.25657893275488,30.41947647039557]
                  ,"UP":[[77.387229308816,28.60449842249079],
                         [77.32696980351483,28.580963707940224],
                         [77.34124039547493,28.586573067106183]]
                  ,"Uttar Pradesh":[[77.387229308816,28.60449842249079],
                                    [77.32696980351483,28.580963707940224],
                                    [77.34124039547493,28.586573067106183]]
                  ,"Rajasthan":[76.81237700556501,28.194173517872024]}

API_KEY = os.getenv("LOCATION_API_KEY")
global routetime,routedist
def auto_mapper(long,lat,state):    
    client=openrouteservice.Client(key=API_KEY)
    minimum=[]
    for i in coordinates_list[state]:
        route = client.directions(coordinates=[i]+[[long,lat]],units="km",profile='cycling-electric',format='geojson')
        minimum.append(route['features'][0]['properties']['segments'][0]['duration'])
    mini=minimum.index(min(minimum))
    route = client.directions(coordinates=[coordinates_list[state][mini]]+[[long,lat]],profile='cycling-electric',format='geojson')
    routetime=route['features'][0]['properties']['segments'][0]['duration']
    routedist=route['features'][0]['properties']['segments'][0]['distance']
    map_directions = folium.Map(location=[lat,long],zoom_start=15,tiles="openstreetmap")
    folium.GeoJson(route, name='route').add_to(map_directions)
    folium.Marker(location=[coordinates_list[state][mini][1],coordinates_list[state][mini][0]],popup="Bite o'Clock Outlet",icon=folium.Icon(color="orange",icon_colour="white",icon="cutlery",angle=0,prefix="fa")).add_to(map_directions)
    folium.Marker(location=[lat,long],popup="Your Location",icon=folium.Icon(color="blue",icon_colour="white",icon="glyphicon-home",angle=0)).add_to(map_directions)
    folium.LayerControl().add_to(map_directions)
    map_directions.save("Bite o'Clock Geolocation Services.html")


