#### Important modules ####
import rdflib
import rdfextras
import numpy as np
import sys
import os
sys.path.append(os.path.relpath("."))
from creating_entities import *

#### Ontology path ####
filename = "../ontology/final-archi_entities.owl" #replace with something interesting
form = rdflib.util.guess_format(filename)

#### Request functions ####
def test_request_1():
    g=rdflib.Graph()
    g.parse(filename, format=form)
    results = g.query("""PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#> SELECT ?Airport {?Airport pie:HasRunway pie:Runway_0}""")
    g.close
    return results

def request_5(): #Wind orientation at arrival airport
    g=rdflib.Graph()
    g.parse(filename, format=form)
    results = g.query("""PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#> SELECT ?winddir
        WHERE {
            ?arrival_airport pie:AirportIsArrival 1 .
            ?weather_at_arrival pie:BelongsToAirport ?arrival_airport .
            ?weather_at_arrival pie:WeatherOrientation ?winddir .
    }""")
    g.close
    return results

def request_6(): #Wind speed at arrival airport
    g=rdflib.Graph()
    g.parse(filename, format=form)
    results = g.query("""PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#> SELECT ?windspeed
        WHERE {
            ?arrival_airport pie:AirportIsArrival 1 .
            ?weather_at_arrival pie:BelongsToAirport ?arrival_airport .
            ?weather_at_arrival pie:WeatherSpeed ?windspeed .
    }""")
    g.close
    return results

def request_7(): #Weather at arrival airport
    g=rdflib.Graph()
    g.parse(filename, format=form)
    results = g.query("""PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#> SELECT ?Ceiling ?Clouds ?QNH ?Hail ?Orientation ?Speed ?Temp ?Rain ?Snow
    WHERE {
        ?Airport pie:AirportIsArrival 1 .
        ?Airport pie:HasWeather ?Weather .
        ?Weather pie:WeatherCeiling ?Ceiling .
        ?Weather pie:WeatherCloudsType ?Clouds .
        ?Weather pie:WeatherQNH ?QNH .
        ?Weather pie:WeatherHail ?Hail .
        ?Weather pie:WeatherOrientation ?Orientation .
        ?Weather pie:WeatherSpeed ?Speed .
        ?Weather pie:WeatherTemperature ?Temp .
        ?Weather pie:WeatherRain ?Rain .
        ?Weather pie:WeatherSnow ?Snow .
    }""")
    g.close
    return results

def request_8(): #nearest airport
    g=rdflib.Graph()
    g.parse(filename, format=form)
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Name ?ICAO ?lat ?long
    WHERE {
        ?Airport pie:AirportICAOCode ?ICAO .
        ?Airport pie:AirportName ?Name .
        ?Airport pie:AirportGPSLongitude ?long .
        ?Airport pie:AirportGPSLatitude ?lat .
        }
    """
    ans = g.query(query2)
    g.close
    resu = ""
    for row in ans:
        resu += ("%s %s %s %s " % row)
    resu2 = resu.split(" ") #resu2 format: [Name,ICAO,Lat,Long,Name,ICAO,Lat,Long... ]
    resu2.pop(-1)
    distances = [0]*(len(resu2)//4)
    AircraftLat = getAircraftLat()
    AircraftLong = getAircraftLong()
    for i in range(len(resu2)//4):
        distances[i] = coord_to_dist(AircraftLat, AircraftLong, float(resu2[i*4+2]), float(resu2[i*4+3]))
    index = distances.index(min(distances))
    return [resu2[index*4],resu2[index*4+1],distances[index]] #returns [Name,ICAO,Distance] of nearest airport
 
def request_9(): #closest airport I can land on
    g=rdflib.Graph()
    g.parse(filename, format=form)
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Name ?ICAO ?lat ?long ?arff ?rwPCN ?runway_length ?runway_width
    WHERE {
        ?Airport pie:AirportICAOCode ?ICAO .
        ?Airport pie:HasRunway ?rw .
        ?rw pie:RunwayLength ?runway_length .
        ?rw pie:RunwayWidth ?runway_width .
        ?Airport pie:AirportName ?Name .
        ?Airport pie:AirportGPSLongitude ?long .
        ?Airport pie:AirportGPSLatitude ?lat .
        ?Airport pie:AirportARFFIndex ?arff .
        ?rw pie:RunwayLength ?runway_length .
        ?rw pie:RunwayPCN ?rwPCN .
        }
    ORDER BY DESC(?runway_length)
    """
    results = g.query(query2)
    g.close
    resu = ""
    for row in results:
        resu += ("%s;%s;%s;%s;%s;%s;%s;%s;" % row)
    resu2 = resu.split(";")
    resu2.pop(-1)
    AircraftLat = getAircraftLat()
    AircraftLong = getAircraftLong()
    AircraftMAR = getAircraftMAR()
    AircraftWidth = getAircraftWidth()
    AircraftMLD = getAircraftMLD()
    AircraftWeight = getAircraftWeight()
    AircraftARFF = getAircraftARFF()
    airports_ICAO = []
    airports_name = []
    airports_lat = []
    airports_long = []
    for i in range(len(resu2)//8):
        AirportICAO = resu2[i*8+1][1:5]
        AirportName = resu2[i*8]
        AirportARFF = int(resu2[i*8+4])
        AirportLat = float(resu2[i*8+2])
        AirportLong = float(resu2[i*8+3])
        Runway_length = int(resu2[i*8+6])
        Runway_width = int(resu2[i*8+7])
        Runway_pcn = resu2[i*8+5]
        if AirportICAO == 'LFPO':
            print(f"arff : {AirportARFF}, RW length : {Runway_length}, RW width : {Runway_width}, RW PCN : {Runway_pcn}")
        #Create lists of data from all the airports I can land on
        if AirportARFF >= AircraftARFF \
            and Runway_length >= AircraftMLD \
            and Runway_width >= 0.75*AircraftWidth\
            and acn_ok(Runway_pcn,AircraftWeight):
            airports_ICAO.append(AirportICAO)
            airports_name.append(AirportName)
            airports_lat.append(AirportLat)
            airports_long.append(AirportLong)

    distances = [0]*(len(airports_ICAO))
    for i in range(len(airports_ICAO)):
        distances[i] = coord_to_dist(AircraftLat, AircraftLong, airports_lat[i], airports_long[i])

    index = distances.index(min(distances))

    return([airports_ICAO[index], airports_name[index], distances[index], distances[index]<=AircraftMAR])
    
def request_12(WPname): #Altitude at waypoint
    g=rdflib.Graph()
    g.parse(filename, format=form)
    stest = WPname
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?PlannedAlt
    WHERE {
        ?Waypoint pie:WaypointName ?WPname .
        ?Waypoint pie:WaypointPlannedAltitude ?PlannedAlt .
        FILTER regex(?WPname, """ + '"' + stest + '"' + """, "i")}
    """
    results = g.query(query2)
    g.close
    return results

def request_13(): #Arrival ETA
    g=rdflib.Graph()
    g.parse(filename, format=form)
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?ETA
    WHERE {
        ?Airport pie:AirportIsArrival 1 .
        ?Airport pie:AirportEstimatedTimeOfArrival ?ETA . }
    """
    results = g.query(query2)
    g.close
    return results

def request_14(): #Anti icing needed?
    g=rdflib.Graph()
    g.parse(filename, format=form)
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?IcingProbe ?IcingState
    WHERE {
        pie:DassaultJet pie:AircraftIcingProbe ?IcingProbe .
        pie:DassaultJet pie:AircraftAntiIcingState ?IcingState .
        }
    """
    results = g.query(query2)
    g.close
    return results

def request_15(WPname): #Weather at waypoint
    g=rdflib.Graph()
    g.parse(filename, format=form)
    stest = WPname
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Ceiling ?Clouds ?QNH ?Hail ?Orientation ?Speed ?Temp ?Rain ?Snow
    WHERE {
        ?Waypoint pie:WaypointName ?WPname .
        ?Waypoint pie:HasWeather ?Weather .
        ?Weather pie:WeatherCeiling ?Ceiling .
        ?Weather pie:WeatherCloudsType ?Clouds .
        ?Weather pie:WeatherQNH ?QNH .
        ?Weather pie:WeatherHail ?Hail .
        ?Weather pie:WeatherOrientation ?Orientation .
        ?Weather pie:WeatherSpeed ?Speed .
        ?Weather pie:WeatherTemperature ?Temp .
        ?Weather pie:WeatherRain ?Rain .
        ?Weather pie:WeatherSnow ?Snow .
        FILTER regex(?WPname, """ + '"' + stest + '"' + """, "i")}
    """
    results = g.query(query2)
    g.close
    return results

def request_16(ICAOCode): #Weather at Airport ICAOCode
    g=rdflib.Graph()
    g.parse(filename, format=form)
    stest = ICAOCode
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Ceiling ?Clouds ?QNH ?Hail ?Orientation ?Speed ?Temp ?Rain ?Snow
    WHERE {
        ?Airport pie:AirportICAOCode ?ICAO .
        ?Airport pie:HasWeather ?Weather .
        ?Weather pie:WeatherCeiling ?Ceiling .
        ?Weather pie:WeatherCloudsType ?Clouds .
        ?Weather pie:WeatherQNH ?QNH .
        ?Weather pie:WeatherHail ?Hail .
        ?Weather pie:WeatherOrientation ?Orientation .
        ?Weather pie:WeatherSpeed ?Speed .
        ?Weather pie:WeatherTemperature ?Temp .
        ?Weather pie:WeatherRain ?Rain .
        ?Weather pie:WeatherSnow ?Snow .
        FILTER regex(?ICAO, """ + '"' + stest + '"' + """, "i")}
    """
    results = g.query(query2)
    g.close
    return results

def request_18(ICAOCode): #Fuel at airport ICAO
    g=rdflib.Graph()
    g.parse(filename, format=form)
    stest = ICAOCode
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Lati ?Longi
    WHERE {
        ?Airport pie:AirportICAOCode ?ICAO .
        ?Airport pie:AirportGPSLatitude ?Lati .
        ?Airport pie:AirportGPSLongitude ?Longi .
        FILTER regex(?ICAO, """ + '"' + stest + '"' + """, "i")}
    """
    results = g.query(query2)
    g.close
    resu = []
    for row in results:
        resu = (("%s %s" % row)).split(" ")
        resu[0] = float(resu[0]) #Latitude
        resu[1] = float(resu[1]) #Longitude

    data = fuel_request_data() # data = [0:fuel consummed in 20s,1:current AC speed,2:AC latitude,3:AC longitude,4:current remaining fuel,5:total fuel capacity]
    dist = coord_to_dist(data[2], data[3], resu[0], resu[1]) #distance to airport in nm
    time_to_airport = -dist/data[1]*3600 #time to airport in seconds
    consummed_fuel_to_airport = data[0]*time_to_airport/20
    percentage_fuel_to_airport = consummed_fuel_to_airport/data[5]*100
    return (data[4]/data[5]*100 - percentage_fuel_to_airport)

def request_19(WPname): #Fuel at waypoint
    g=rdflib.Graph()
    g.parse(filename, format=form)
    stest = WPname
    query2 = """
    PREFIX pie:<http://www.semanticweb.org/clement/ontologies/2020/1/final-archi#>
    SELECT ?Lati ?Longi
    WHERE {
        ?Waypoint pie:WaypointName ?WPname .
        ?Waypoint pie:WaypointGPSLatitude ?Lati .
        ?Waypoint pie:WaypointGPSLongitude ?Longi .
        FILTER regex(?WPname, """ + '"' + stest + '"' + """, "i")}
    """
    results = g.query(query2)
    g.close
    resu = []
    for row in results:
        resu = (("%s %s" % row)).split(" ")
        resu[0] = float(resu[0])
        resu[1] = float(resu[1])
    
    data = fuel_request_data() # data = [0:fuel consummed in 20s,1:current AC speed,2:AC latitude,3:AC longitude,4:current remaining fuel,5:total fuel capacity]
    dist = coord_to_dist(data[2], data[3], resu[0], resu[1]) #distance to wp in nm
    time_to_wp = -dist/data[1]*3600 #time to airport in seconds
    consummed_fuel_to_wp = data[0]*time_to_wp/20
    percentage_fuel_to_wp = consummed_fuel_to_wp/data[5]*100
    return (data[4]/data[5]*100 - percentage_fuel_to_wp)




#### Print request results ####
def print_request(results):
    resu = ""
    for row in results:
        resu += ("%s" % row)
    return resu.split("#")[-1]

def print_weather_request(results):
    resu = ""
    for row in results:
        resu += (" Ceiling: %s ft | Clouds: %s | QNH: %s | Hail: %s | Wind orientation: %s ° | Wind speed: %s kts | Temperature: %s ° | Rain: %s | Snow: %s" % row)
    return resu
    
def print_nearest_airport(results):
    return "The nearest Airport is " + str(results[0]) + "|| ICAO : " + str(results[1]+ ", at a distance of " + str(round(results[2],2)) + "nm")

def print_icing_request(results):
    resu = ""
    txtans = ""
    for row in results:
        txtans += "AntiIcing probe: %s | AntiIcing State: %s" % row
        resu += ("%s %s" % row)
    resu2 = resu.split(" ")
    if resu2[0]==resu2[1]:
        txtans +=" || No action required"
    elif resu2[0] == "false":
        txtans +=" || Turn off AntiIcing"
    elif resu2[0] == "true":
        txtans +=" || Turn on AntiIcing"
    return txtans

def print_nearest_possible(results):
    if results[3]:
        return "The nearest Airport I can land on is " + str(results[1]) + "|| ICAO : " + str(results[0]) + ", at a distance of " + str(round(results[2],2)) + "nm"
    else:
        return "No airport I can land on within range. The closest is " +  str(results[1]) + "|| ICAO : " + str(results[0]) + ", at a distance of " + str(round(results[2],2)) + "nm"

####UTILS#####
def coord_to_dist(cur_lat, cur_long, dest_lat, dest_long):
    cur_lat = cur_lat*np.pi/180
    cur_long = cur_long*np.pi/180
    dest_lat = dest_lat*np.pi/180
    dest_long = dest_long*np.pi/180
    return 60*180/np.pi*np.arccos(np.sin(cur_lat)*np.sin(dest_lat)+np.cos(cur_lat)*np.cos(dest_lat)*np.cos(dest_long-cur_long))
