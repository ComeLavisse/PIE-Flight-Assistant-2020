####Install modules####
import subprocess
subprocess.call(['pip', 'install', 'owlready2'])
subprocess.call(['pip', 'install', 'rdflib'])
subprocess.call(['pip', 'install', 'rdfextras'])

####MODULES####
import pandas as pd
import owlready2 as owl

###############################################################################
##########################FUNCTION DEFINITION##################################
###############################################################################

####aircraft CREATION####
####aircraft CREATION####
def create_aircraft(aircraft_name):
    onto.Aircraft("DassaultJet")
    return onto.DassaultJet

def create_aircraft_df(filename):
    df = pd.read_csv(filename, sep=';|,', engine='python')
    df = df.drop("Index", axis=1)
    return df

def load_aircraft_property(df, DassaultJet, time_index):
    index = time_index
    DassaultJet.AircraftLength.append(float(df['AircraftLength'][index]))
    DassaultJet.AircraftSpan.append(float(df['AircraftSpan'][index]))
    DassaultJet.AircraftFuelCapacity.append(float(df['AircraftFuelCapacity'][index]))
    DassaultJet.AircraftMLW.append(float(df['AircraftMLW'][index]))
    DassaultJet.AircraftARFF.append(str(df['AircraftARFF'][index]))
    DassaultJet.LiveAltitude.append(float(df['LiveAltitude'][index]))
    DassaultJet.LiveCurrentWeight.append(float(df['LiveCurrentWeight'][index]))
    DassaultJet.LiveMAR.append(float(df['LiveMAR'][index]))
    DassaultJet.LiveSR.append(float(df['LiveSR'][index]))
    DassaultJet.LiveIAS.append(float(df['LiveIAS'][index]))
    DassaultJet.LiveVz.append(float(df['LiveVz'][index]))
    DassaultJet.ReferenceVclimb.append(float(df['ReferenceVclimb'][index]))
    DassaultJet.ReferenceCruiseFL.append(int(df['ReferenceCruiseFL'][index]))
    DassaultJet.ReferenceMORA.append(float(df['ReferenceMORA'][index]))
    DassaultJet.ReferenceZpOpt.append(float(df['ReferenceZpOpt'][index]))
    DassaultJet.ReferenceVcruise.append(float(df['ReferenceVcruise'][index]))
    DassaultJet.ReferenceDescentFL.append(int(df['ReferenceDescentFL'][index]))
    DassaultJet.ReferenceVdescent.append(float(df['ReferenceVdescent'][index]))
    DassaultJet.ReferenceMLD.append(float(df['ReferenceMLD'][index]))
    DassaultJet.AircraftFlightPhase.append(str(df['AircraftFlightPhase'][index]))
    DassaultJet.AircraftNextWaypointETA.append(float(df['CurrentWaypointEstimatedTimeOfArrival'][index]))
    DassaultJet.AircraftGPSLatitude.append(float(df['AircraftGPSLatitude'][index]))
    DassaultJet.AircraftGPSLongitude.append(float(df['AircraftGPSLongitude'][index]))
    DassaultJet.Heading.append(float(df['Heading'][index]))
    DassaultJet.AircraftACN.append(df['AircraftACN'][index])
    DassaultJet.AircraftAntiIcingState.append(bool(df['AircraftAntiIcingState'][index]))
    DassaultJet.AircraftIcingProbe.append(bool(df['AircraftIcingProbe'][index]))
    DassaultJet.AircraftFlapsPosition.append(int(df['AircraftFlapsPosition'][index]))
    DassaultJet.AircraftSlatsPosition.append(int(df['AircraftSlatsPosition'][index]))
    DassaultJet.AircraftSpoilersPosition.append(bool(df['AircraftSpoilersPosition'][index]))
    DassaultJet.AircraftFuel.append(float(df['AircraftFuel'][index]))
    DassaultJet.AircraftLandingGearAuxilary.append(bool(df['AircraftLandingGearAuxilary'][index]))
    DassaultJet.AircraftLandingGearPrincipal.append(bool(df['AircraftLandingGearPrincipal'][index]))
      
def update_aircraft_property(df, DassaultJet, time_index):
    index = time_index
    DassaultJet.LiveAltitude.append(float(df['LiveAltitude'][index]))
    DassaultJet.LiveCurrentWeight.append(float(df['LiveCurrentWeight'][index]))
    DassaultJet.LiveMAR.append(float(df['LiveMAR'][index]))
    DassaultJet.LiveSR.append(float(df['LiveSR'][index]))
    DassaultJet.LiveIAS.append(float(df['LiveIAS'][index]))
    DassaultJet.LiveVz.append(float(df['LiveVz'][index]))
    DassaultJet.AircraftFlightPhase.append(str(df['AircraftFlightPhase'][index]))
    DassaultJet.AircraftGPSLatitude.append(float(df['AircraftGPSLatitude'][index]))
    DassaultJet.AircraftGPSLongitude.append(float(df['AircraftGPSLongitude'][index]))
    DassaultJet.Heading.append(float(df['Heading'][index]))
    DassaultJet.AircraftAntiIcingState.append(bool(df['AircraftAntiIcingState'][index]))
    DassaultJet.AircraftIcingProbe.append(bool(df['AircraftIcingProbe'][index]))
    DassaultJet.AircraftFlapsPosition.append(int(df['AircraftFlapsPosition'][index]))
    DassaultJet.AircraftSlatsPosition.append(int(df['AircraftSlatsPosition'][index]))
    DassaultJet.AircraftSpoilersPosition.append(bool(df['AircraftSpoilersPosition'][index]))
    DassaultJet.AircraftFuel.append(float(df['AircraftFuel'][index]))
    DassaultJet.ReferenceMLD.append(float(df['ReferenceMLD'][index]))
    DassaultJet.AircraftLandingGearAuxilary.append(bool(df['AircraftLandingGearAuxilary'][index]))
    DassaultJet.AircraftLandingGearPrincipal.append(bool(df['AircraftLandingGearPrincipal'][index]))
    
    DassaultJet.AircraftNextWaypointETA.append(float(df['CurrentWaypointEstimatedTimeOfArrival'][index]))



 ####WAYPOINT CREATION####
def create_waypoint_df(filename):
    df_wp = pd.read_csv(filename, sep=';')
    df_wp = df_wp.drop("Index", axis=1)
    return df_wp

def create_waypoints(df_wp):
    List_Waypoints = [0]*len(df_wp)
    for i in range(len(df_wp)):
        string = 'Waypoint_'+str(i)
        List_Waypoints[i] = onto.Waypoint(string)
    return List_Waypoints


def load_waypoint_data_property(df_wp, List_Waypoints):
    for waypoint_number in range(len(df_wp)):
        CurrentWaypoint = List_Waypoints[waypoint_number]
        CurrentWaypoint.WaypointPlannedAltitude.append(float(df_wp['WaypointPlannedAltitude'][waypoint_number]))
        CurrentWaypoint.WaypointName.append(str(df_wp['WaypointName'][waypoint_number]))
        CurrentWaypoint.WaypointGPSLongitude.append(float(df_wp['WaypointGPSLongitude'][waypoint_number]))
        CurrentWaypoint.WaypointGPSLatitude.append(float(df_wp['WaypointGPSLatitude'][waypoint_number]))

def load_waypoint_object_property(df_wp, df_wt, List_Waypoints, List_Weather):
    for i in range(len(df_wt)):
        bt = df_wt['BelongsTo'][i]
        for j in range(len(df_wp)):
            wp_index = df_wp['WaypointName'][j]
            if bt == wp_index:
                List_Waypoints[j].HasWeather = [List_Weather[i]]
                List_Weather[i].BelongsToWaypoint = [List_Waypoints[j]]


def print_waypoint_property(Waypoint):
    return [Waypoint.WaypointPlannedAltitude, Waypoint.WaypointEstimatedTimeOfArrival,     Waypoint.WaypointName , Waypoint.WaypointGPSLongitude, Waypoint.WaypointGPSLatitude]



####AIRPORT CREATION####
def create_airport_df(filename):
    df = pd.read_csv(filename, sep=';', engine='python')
    return df

def create_airport(df_ap):
    List_Airports = [0]*len(df_ap)
    for i in range(len(df_ap)):
        string = 'Airport_' + str(i)
        List_Airports[i]=onto.Airport(string)
    return List_Airports

def load_airport_data_property(df, List_Airports):
    for i in range(len(df)):
        List_Airports[i].AirportICAOCode.append(str(df['AirportICAOCode'][i]))
        List_Airports[i].AirportARFFIndex.append(str(df['AirportARFFIndex'][i]))
        List_Airports[i].AirportGPSLatitude.append(float(df['AirportGPSLatitude'][i]))
        List_Airports[i].AirportGPSLongitude.append(float(df['AirportGPSLongitude'][i]))
        List_Airports[i].AirportCTRGround.append(float(df['AirportCTRGround'][i]))
        List_Airports[i].AirportCTRLanding.append(float(df['AirportCTRLanding'][i]))
        List_Airports[i].AirportCTRTakeOff.append(float(df['AirportCTRTakeOff'][i]))
        List_Airports[i].AirportName.append(str(df['AirportName'][i]))
        List_Airports[i].AirportEstimatedDepartureTime.append(int(df['AirportEstimatedDepartureTime'][i]))
        List_Airports[i].AirportParkingSpot.append(str(df['AirportParkingSpot'][i]))
        List_Airports[i].AirportEstimatedTimeOfArrival.append(int(df['AirportEstimatedTimeOfArrival'][i]))
        List_Airports[i].AirportIsDeparture.append(int(df['AirportIsDeparture'][i]))
        List_Airports[i].AirportIsArrival.append(float(df['AirportIsArrival'][i]))
        List_Airports[i].AirportOpeningHours.append(str(df['AirportOpeningHours'][i]))
        List_Airports[i].CTRActiveHours.append(str(df['CTRActiveHours'][i]))
        List_Airports[i].Fuel.append(str(df['Fuel'][i]))
        List_Airports[i].WidthTaxiway.append(str(df['WidthTaxiway'][i]))
        List_Airports[i].Handling.append(str(df['Handling'][i]))

def load_airport_object_property(df_rw, df_ap, df_wt, List_Airports, List_Runways, List_Weather):
    for j in range(len(df_ap)): #for each airport
        temp = []
        for i in range(len(df_rw)): #goes through all the runways
            bt = df_rw['BelongsTo'][i] 
            icao = df_ap['AirportICAOCode'][j][1:5] 
            if bt == icao: #if the runway belongs to the airport
                List_Runways[i].BelongsToAirport = [List_Airports[j]] #add object prop to the runway
                temp.append(List_Runways[i]) #add the runway to the list of runways the airport has
        List_Airports[j].HasRunway = temp #add the completed list as object prop to the airport
                
    for i in range(len(df_wt)):
        bt = df_wt['BelongsTo'][i]
        for j in range(len(df_ap)):
            icao = df_ap['AirportICAOCode'][j][1:5]
            if bt == icao:
                List_Airports[j].HasWeather = [List_Weather[i]]
                List_Weather[i].BelongsToAirport = [List_Airports[j]]


####RUNWAYS CREATION####
def create_runways_df(filename):
    df_rw = pd.read_csv(filename,delimiter=';|,', engine='python')
    return df_rw

def create_runways(df_rw):
    List_Runways = [0]*len(df_rw)
    for i in range(len(df_rw)):
        string = 'Runway_' + str(i)
        List_Runways[i] = onto.Runway(string)
    return List_Runways

def load_runways_data_property(df_rw, List_Runways):
    for i in range(len(df_rw)):
        List_Runways[i].RunwayLength.append(int(df_rw['RunwayLength'][i]))
        List_Runways[i].RunwayWidth.append(int(df_rw['RunwayWidth'][i]))
        List_Runways[i].RunwayPCN.append(str(df_rw['RunwayPCN'][i]))

####WEATHER CREATION####
def create_weather_df(filename):
    df_wt = pd.read_csv(filename,delimiter=';|,', engine='python')
    return df_wt

def create_weather(df_wt):
    List_Weather = [0]*len(df_wt)
    for i in range(len(df_wt)):
      string = 'Weather_' + str(i)
      List_Weather[i] = onto.Weather(string)
    return List_Weather

def load_weather_data_property(df_wt, List_Weather):
    for i in range(len(df_wt)):
        List_Weather[i].WeatherRain.append(bool(df_wt['WeatherRain'][i]))
        List_Weather[i].WeatherSnow.append(bool(df_wt['WeatherSnow'][i]))
        List_Weather[i].WeatherHail.append(bool(df_wt['WeatherHail'][i]))
        List_Weather[i].WeatherQNH.append(int(df_wt['WeatherQNH'][i]))
        List_Weather[i].WeatherTemperature.append(float(df_wt['WeatherTemperature'][i]))
        List_Weather[i].WeatherCloudsType .append(str(df_wt['WeatherCloudsType'][i]))
        List_Weather[i].WeatherCeiling.append(float(df_wt['WeatherCeiling'][i]))
        List_Weather[i].WeatherOrientation.append(float(df_wt['WeatherOrientation'][i]))
        List_Weather[i].WeatherSpeed.append(float(df_wt['WeatherSpeed'][i]))


####CHECKLIST CREATION####
def create_checklist_df(filename):
    df_cl = pd.read_csv(filename,delimiter=';|,', engine='python')
    return df_cl

def create_checklist(df_cl):
    List_Checklists = [0]*len(df_cl)
    for i in range(len(df_cl)):
        string = 'Checklist_' + str(i)
        List_Checklists[i] = onto.Checklist(string)
    return List_Checklists

def load_checklist_data_property(df_cl, List_Checklists):
    for i in range(len(df_cl)):
        List_Checklists[i].CheckListLanding.append(str(df_cl['CheckListLanding'][i]))
        List_Checklists[i].CheckListStart.append(str(df_cl['CheckListStart'][i])) 
        List_Checklists[i].CheckListApproach.append(str(df_cl['CheckListApproach'][i])) 

###############################################################################
##############################EXECUTION########################################
###############################################################################


####LOAD ONTOLOGY####
owl.onto_path.append("")
#onto = owl.get_ontology("../ontology/final-archi.owl").load()

def create_ontology():
    global onto
    global df_aircraft
    onto = owl.get_ontology("../ontology/final-archi.owl").load()

    ####CREATE ENTITIES####
    DassaultJet = create_aircraft("DassaultJet")
    df_aircraft = create_aircraft_df("../csv/aircraft.csv")
    load_aircraft_property(df_aircraft, DassaultJet, time_index=0)

    df_waypoint = create_waypoint_df("../csv/waypoint.csv")
    List_Waypoints = create_waypoints(df_waypoint)
    load_waypoint_data_property(df_waypoint, List_Waypoints)

    
    df_airport = create_airport_df("../csv/airport.csv")
    List_Airports = create_airport(df_airport)
    load_airport_data_property(df_airport, List_Airports)

    df_weather = create_weather_df("../csv/weather.csv")
    List_Weathers = create_weather(df_weather)
    load_weather_data_property(df_weather, List_Weathers)

    df_runway = create_runways_df("../csv/runway.csv")
    List_Runways = create_runways(df_runway)
    load_runways_data_property(df_runway, List_Runways)

    df_checklist = create_checklist_df("../csv/checklist.csv")
    List_Checklists = create_checklist(df_checklist)
    load_checklist_data_property(df_checklist, List_Checklists)

    load_airport_object_property(df_runway, df_airport, df_weather, List_Airports, List_Runways, List_Weathers)
    load_waypoint_object_property(df_waypoint, df_weather, List_Waypoints, List_Weathers)

    ####SAVE ONTOLOGY####
    onto.save(file = "../ontology/final-archi_entities.owl", format = "rdfxml")

def update_ontology(time_index):
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    ####UPDATE ENTITIES####
    update_aircraft_property(df_aircraft, onto.DassaultJet, time_index)
    ####SAVE ONTOLOGY####
    onto.save(file = "../ontology/final-archi_entities.owl", format = "rdfxml")


####DATA PROPERTIES REQUESTS####
def test_request_3():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    return onto.DassaultJet.LiveIAS[-1]

def test_request_2():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    return onto.DassaultJet.LiveAltitude[-1]



def request_1(): #Print checklist approach
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    filename = onto.Checklist_0.CheckListApproach[0]
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def request_2(): #Approach speed
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    weight = onto.DassaultJet.LiveCurrentWeight[-1]/1000
    slats = onto.DassaultJet.AircraftSlatsPosition[-1]
    flaps = onto.DassaultJet.AircraftFlapsPosition[-1]
    increment = approach_speed_increment(slats,flaps)
    return 1.0125*weight+64.139+5+increment

def request_3(): #Landing speed
    return request_2() - 5

def request_4(): #Landing distance
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    mld = onto.DassaultJet.ReferenceMLD[-1]
    slats = onto.DassaultJet.AircraftSlatsPosition[-1]
    flaps = onto.DassaultJet.AircraftFlapsPosition[-1]
    factor = landing_distance_factor(slats,flaps)
    return mld*factor

def request_10(): #Altitude at waypoint 
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    FlightPhase = onto.DassaultJet.AircraftFlightPhase[-1]
    return [FlightPhase,onto.DassaultJet.LiveMAR[-1]]

def request_11(): #ETA at waypoint 
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    return onto.DassaultJet.AircraftNextWaypointETA[-1]

def request_17(): #Fuel remaining
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    current = onto.DassaultJet.AircraftFuel[-1]
    total_capa = onto.DassaultJet.AircraftFuelCapacity[-1]
    return current/total_capa*100

def request_20(): #Optimal altitude 
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    weight = onto.DassaultJet.LiveCurrentWeight[-1]/1000
    return optimal_altitude(weight)

def request_21(AirportICAOCode): #Opening hour airport 
    df = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range(len(df)):
        print(str(df['AirportICAOCode'][i]))
        if df['AirportICAOCode'][i] == "'" + AirportICAOCode + "'":
            return(df['AirportOpeningHours'][i])
    return "Unknown ICAO code"

def request_22(AirportICAOCode): #Opening hour airport 
    df = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range(len(df)):
        print(str(df['AirportICAOCode'][i]))
        if df['AirportICAOCode'][i] == "'" + AirportICAOCode + "'":
            return(df['CTRActiveHours'][i])
    return "Unknown ICAO code"

def request_23(AirportICAOCode): #Opening hour airport 
    df = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range(len(df)):
        print(str(df['AirportICAOCode'][i]))
        if df['AirportICAOCode'][i] == "'" + AirportICAOCode + "'":
            return(df['Fuel'][i])
    return "Unknown ICAO code"

def request_24(AirportICAOCode): #Opening hour airport 
    df = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range(len(df)):
        print(str(df['AirportICAOCode'][i]))
        if df['AirportICAOCode'][i] == "'" + AirportICAOCode + "'":
            return(df['WidthTaxiway'][i])
    return "Unknown ICAO code"

def request_25(AirportICAOCode): #Opening hour airport 
    df = pd.read_csv("../csv/airport.csv", sep=';', engine='python')
    for i in range(len(df)):
        print(str(df['AirportICAOCode'][i]))
        if df['AirportICAOCode'][i] == "'" + AirportICAOCode + "'":
            return(df['Handling'][i])
    return "Unknown ICAO code"



def request_pm_1():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    phase = onto.DassaultJet.AircraftFlightPhase[-1]
    vz = onto.DassaultJet.LiveVz[-1]
    ias = onto.DassaultJet.LiveIAS[-1]
    if "Climb" in phase:
        vref = onto.DassaultJet.ReferenceVclimb[0]
        if not (vref-200<vz<vref+200):
            return "CHECK ASCENDING SPEED\n"
        else:
            return ""
    elif "Cruise" in phase:
        vref = onto.DassaultJet.ReferenceVcruise[0]
        if not (vref-10<ias<vref+10):
            return "CHECK SPEED\n"
        else:
            return ""
    elif "Descent" in phase:
        vref = onto.DassaultJet.ReferenceVdescent[0]
        if not (vref-200<vz<vref+200):
            return "CHECK DESCENDING SPEED\n"
        else:
            return ""
    else:
        return ""

def request_pm_2():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    altitude = onto.DassaultJet.LiveAltitude[-1]
    ReferenceFL = onto.DassaultJet.ReferenceCruiseFL[-1]
    phase = onto.DassaultJet.AircraftFlightPhase[-1]
    if "Cruise" in phase:
        if (altitude <= ReferenceFL*100 - 250) or (altitude >= ReferenceFL*100+250):
            return "CHECK ALTITUDE\n"
        else:
            return ""
    else:
        return ""

def request_pm_3():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    mora = onto.DassaultJet.ReferenceMORA[0]
    altitude = onto.DassaultJet.LiveAltitude[-1]
    phase = onto.DassaultJet.AircraftFlightPhase[-1]
    if "Cruise" in phase:
        if not mora<altitude:
            return "CHECK ALTITUDE\n"
        else:
            return ""
    else:
        return ""

def request_pm_4():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    phase = onto.DassaultJet.AircraftFlightPhase[-1]
    if "Landing" in phase:
        if not ((onto.DassaultJet.AircraftLandingGearPrincipal[-1] == 1) and (onto.DassaultJet.AircraftLandingGearAuxilary[-1] == 1)):
            return "GEAR DOWN\n"
        else:
            return ""
    else:
        return ""

def request_pm_5():
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    phase = onto.DassaultJet.AircraftFlightPhase[-1]
    if "Climb" in phase:
        if not ((onto.DassaultJet.AircraftLandingGearPrincipal[-1] == 0) and (onto.DassaultJet.AircraftLandingGearAuxilary[-1] == 0)):
            return "GEAR UP\n"
        else:
            return ""
    else:
        return ""

def request_fp(): #flight phase
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    flight_phase = onto.DassaultJet.AircraftFlightPhase[-1]
    return flight_phase

####UTILS####
def get_len():
    df_aircraft = create_aircraft_df("../csv/aircraft.csv")
    return len(df_aircraft)

def getAircraftLat():
    return(onto.DassaultJet.AircraftGPSLatitude[-1])

def getAircraftLong():
    return(onto.DassaultJet.AircraftGPSLongitude[-1])
    
def getAircraftMAR():
    return(onto.DassaultJet.LiveMAR[-1])
    
def getAircraftWidth():
    return(onto.DassaultJet.AircraftSpan[-1])

def getAircraftMLD():
    return(onto.DassaultJet.ReferenceMLD[-1])
    
def getAircraftWeight():
    return(onto.DassaultJet.LiveCurrentWeight[-1])
    
def getAircraftARFF():
    return(int(onto.DassaultJet.AircraftARFF[-1]))


def fuel_request_data():
    #returns [,current AC speed, AC latitude, AC longitude]
    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    diff_fuel =  onto.DassaultJet.AircraftFuel[-1] - onto.DassaultJet.AircraftFuel[-2] #fuel consummed in 20 sec
    total_capa = onto.DassaultJet.AircraftFuelCapacity[-1] #total fuel capacity
    remaining_fuel = onto.DassaultJet.AircraftFuel[-1] #current remaining fuel
    curr_speed = onto.DassaultJet.LiveIAS[-1]
    return diff_fuel, curr_speed, onto.DassaultJet.AircraftGPSLatitude[-1], onto.DassaultJet.AircraftGPSLongitude[-1], remaining_fuel, total_capa


def approach_speed_increment(slats, flaps):
    if flaps == 0:
        if slats == 0:
            return 60
    elif flaps <1:
        if slats < 1:
            return 45
        elif slats >= 1:
            return 25
    elif flaps <2:
        if slats < 1:
            return 30
        elif slats >= 1:
            return 15
    elif flaps <3:
        if slats < 1:
            return 25
        elif slats >= 1:
            return 10
    elif flaps == 3:
        if slats < 1:
            return 25
        elif slats > 3:
            return 5
        else:
            return 10
    else:
        if slats < 1:
            return "not allowed"
        elif slats > 3:
            return 5
        else:
            return 10
    return "not allowed"

def landing_distance_factor(slats, flaps):
    if flaps == 0:
        if slats == 0:
            return 2.4
    elif flaps <1:
        if slats < 1:
            return 2.3
        elif slats >= 1:
            return 1.95
    elif flaps <2:
        if slats < 1:
            return 1.85
        elif slats >= 1:
            return 1.5
    elif flaps <3:
        if slats < 1:
            return 1.7
        elif slats >= 1:
            return 1.4
    elif flaps == 3:
        if slats < 1:
            return 1.65
        elif slats > 3:
            return 1.35
        else:
            return 1.3
    else:
        if slats < 1:
            return "not allowed"
        elif slats > 3:
            return 1.3
        else:
            return 1.25
    return "not allowed"

def optimal_altitude(weight):
    if weight < 54:
        return 390
    elif weight < 56:
        return 385
    elif weight < 58:
        return 375
    elif weight < 60:
        return 370
    elif weight < 62:
        return 365
    elif weight < 64:
        return 355
    elif weight < 66:
        return 345
    elif weight < 68:
        return 340
    elif weight < 70:
        return 340
    elif weight < 72:
        return 335
    elif weight < 74:
        return 325
    elif weight < 76:
        return 320
    else:
        return 310

def acn_ok(pcn,weight):

    onto = owl.get_ontology("../ontology/final-archi_entities.owl").load()
    filename = "../csv/"+onto.DassaultJet.AircraftACN[0]
    df = pd.read_csv(filename, sep=';', engine='python')
    df = df.drop("Index", axis=1)

    pcn = pcn.replace(' ','/').split('/')
    rw_type = pcn[1]
    rw_char = pcn[2]
    rw_numb = int(pcn[0])
    if rw_type == 'R':
        if rw_char == 'A':
            max_ = df['R/A'][0]
            min_ = df['R/A'][1]
        elif rw_char == 'B':
            max_ = df['R/B'][0]
            min_ = df['R/B'][1]
        elif rw_char == 'C':
            max_ = df['R/C'][0]
            min_ = df['R/C'][1]
        elif rw_char == 'D':
            max_ = df['R/D'][0]
            min_ = df['R/D'][1]

    elif rw_type == 'F':
        if rw_char == 'A':
            max_ = df['F/A'][0]
            min_ = df['F/A'][1]
        elif rw_char == 'B':
            max_ = df['F/B'][0]
            min_ = df['F/B'][1]
        elif rw_char == 'C':
            max_ = df['F/C'][0]
            min_ = df['F/C'][1]
        elif rw_char == 'D':
            max_ = df['F/D'][0]
            min_ = df['F/D'][1]
    acn  = min_+(max_-min_)*(weight-47000)/(83400-47000)
    return (acn<rw_numb)
