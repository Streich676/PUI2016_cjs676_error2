#Worked with William, Alexi and Shay



from __future__ import print_function
import sys
import os
import json
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

#Ignore, throw a sting error when used in the url
MTA_KEY =sys.argv[1]
BUS_LINE = sys.argv[2]


##From stackoverflow link
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data.keys()

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

numberofbuses = len(position)
busline = sys.argv[2]

print ("Bus Number:", busline)
print ("Number of Current Buses:", numberofbuses)

ii = 0
for i in position:
    latitude =  i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude =  i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    ii +=1
    print("Bus",ii, "is at", "latitude", latitude, "longitude", longitude)
