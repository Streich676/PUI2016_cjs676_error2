#Worked extensively with William, Alexi and Shay as well as Kelsey who gave us some info on printing to a csv



from __future__ import print_function
import sys
import os
import json
import sys
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info.py 4027f2e7-f7cc-4765-84fa-3259403cb893 <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

writer = csv.writer(open(sys.argv[3], 'w'))
headers = ['Latitude', 'Longitude', 'StopName', 'StopStatus']
writer.writerow(headers)

#Ignore, throw a sting error when used in the url
#MTA_KEY =sys.argv[1]
#BUS_LINE = sys.argv[2]


##From stackoverflow link
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data.keys()

#data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

numberofbuses = len(position)
busline = sys.argv[3]

print ("Bus Number:", busline)
print ("Number of Current Buses:", numberofbuses)

ii = 0
for i in position:
    latitude =  i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude =  i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    ii +=1
    try:
        StopName = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        StopName = "N/A"
    try:
        StopStatus = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        StopStatus ="N/A"
    print("Bus",ii, "is at", "latitude", latitude, "longitude", longitude, StopName, StopStatus)

b = 0
for ii in position:
    row = []
    row.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    row.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    row.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
    row.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
    writer.writerow(row)
    b = b + 1
