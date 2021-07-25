### Overview

This directory contains the ontology-based pilot interface for Dassault Jet. To launch the interface, open a terminal here (root of the repository) and type :
`cd python && python main.py`
Once the window is opened, you can click on the `Start simulation` button to start reading the csv. Two things will happen :
- Button `Start simulation` disappears, and you can the see the simulation starting. The progress of the simulation is prompted in the form `Ontology updated : (current time/total duration`. Each iteration lasts 20 seconds, total_duration actually is the number of line in *aircraft.csv* times 20 seconds. 
- Button `Start questions` will appear. You will see a few questions example, a large window where information will be displayed below a bar where you can type. Submit text by pressing `Backspace` key or `Submit` button.

### Requests available

For now, you can use these different requests. For each request, we will see what you have to type and what will be displayed.
- `approach checklist` : displays the approach checklist.
- `approach speed` : returns the approach speed with respect to actual configuration in kts.
- `landing speed` : returns the landing speed with respect to actual configuration in kts.
- `landing distance` : rthe landing distancence with respect to actual configuration in meters.
- `wind orientation at arrival` : returns the current wind orientation at the arrival airport in degrees.
- `wind speed at arrival` : returns the current wind speed at the arrival airport in kts.
- `weather arrival` : returns the current weather at the arrival airport.
- `nearest airport` : returns the nearest airport.
- `nearest airport landing` : returns the nearest airport you can land on.
- `MAR` : returns the maximal achievable range in nm.
- `waypoint eta` : returns the next waypoint ETA.
- `altitude waypoint WPNAME` : returns the expected altitude at the waypoint WPNAME in FL.
- `arrival ETA` : returns the expected time of arrival.
- `antiicing` : returns a boolean indicating if you need or not to start anti-icing.
- `weather waypoint WPNAME` : returns the current weather at the waypoint WPNAME.
- `weather airport ICAO` : returns the current weather at the airport ICAO.
- `fuel remaining` : returns the percentage of fuel remaining.
- `fuel airport ICAO` : returns the expected remaining fuel percentage at airport ICAO.
- `fuel waypoint ICAO` : returns the expected remaining fuel percentage at waypoint WPNAME.
- `optimal altitude` : returns the current optimal altitude in meters.

### Airports and waypoints available

Current airports available in the test set are : LFPO, LFBD, LFBA, LFMT, LFBO.

Current waypoints available in the test set are : SID_14R-3, MAKOX, LMG, BALAN, SOPIL, STAR_APP-5, STAR_24-12,STAR_24-8, SID_14R-6, SID_DEP-3, SID_DEP-4, SID_DEP-5, FIR12.


### Pilot monitoring

At each iteration of the simulation, we check the value of several parameters compared to reference parameters. The result of this comparison is displayed in the third frame `Pilot monitoring`. If everything is ok, *All parameters OK* is displayed.
