import urllib.request as ur
import urllib.parse as up
import json

serviceurl = "https://www.py4e.com/code3/geojson.py?PHPSESSID=f8684c330ee5e07af3a98f749697a69e"

address_input = input("Enter location: ")
params = {"sensor": "false", "address": address_input}
url = serviceurl + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)