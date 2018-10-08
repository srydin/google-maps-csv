# Discover Stuff https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=XXX
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json
import csv
import time

# setup variables
filename = raw_input('Filename to write in /usr/share/: ')
filebase = "/usr/share/"
filedestination = filebase + filename + ".csv"
coordinates = raw_input('Coordinates in lat/long: ')
radius = raw_input('Radius in meters - max: 50k: ')
keywords = raw_input('Keywords linked with a + sign: ')
google_api_key = "INSERT-YOUR-API-KEY-HERE"
#nearby search url = "https://maps.googleapis.com/maps/api/place/"
url = "https://maps.googleapis.com/maps/api/place/"
#nearby search parameters = "nearbysearch/json?location=%s&radius=%s&type=%s&key=%s" % (coordinates,radius,keywords,google_api_key)
parameters = "textsearch/json?query=%s&location=%s&radius=%s&key=%s" % (keywords,coordinates,radius,google_api_key)
location_lookup_url = url + parameters

# create a function to call from the main loop
def lookupDetails(place_id):
    time.sleep(0.1)
    parameters2 = "details/json?placeid=%s&key=%s" % (place_id,google_api_key)
    details_lookup_url = url + parameters2
    json_obj = urllib2.urlopen(details_lookup_url)
    data2 = json.load(json_obj)
    try:
        phone = data2['result']['formatted_phone_number']
    except KeyError:
        phone = "No value given"
    return phone

# begin writing
my_file = open(filedestination, "w")

# create column headers
my_file.write(str("place_id,name,location,categories,phone"))
my_file.write(" \n")
json_obj = urllib2.urlopen(location_lookup_url)
data = json.load(json_obj)
for item in data['results']:
    place_id = item['place_id']
    my_file.write(str(place_id) + str(","))
    my_file.write(str(item['name'].replace(",","")) + str(","))
    type = ' '.join(map(str, item['types']))
    #my_file.write(str(item['vicinity'].replace(",","") + str(",")))
    my_file.write(str(item['formatted_address'].replace(",","") + str(",")))
    my_file.write(type + str(","))
    phone = lookupDetails(place_id)
    my_file.write(phone)
    my_file.write(" \n")
	


my_file.close()
