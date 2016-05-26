import urllib
import json

#inputing place names
place_name = raw_input("Enter a place name: ")
#inputting url
base_url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
address_param = urllib.urlencode({'address': place_name})
#combines
target = base_url + address_param

print "Retrieving {0}".format(target)
#reads the data
connection = urllib.urlopen(target)
raw_data = connection.read()
#retrieves the id
print "Retrieved {0} characters".format(len(raw_data))
parsed_data = json.loads(raw_data)

print "Place id", parsed_data["results"][0]["place_id"]
