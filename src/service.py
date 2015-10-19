import requests
import json
 
endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"
 
header = { 'X-Application' : 'JOIdNhZjPP4AK9F4', 'X-Authentication' : 'o5458ZOim8wTO2ety08JS9cnc1bYHtf0+Pp/bk5+sXo=' ,'content-type' : 'application/json' }
 
json_req='{"filter":{ }}'
 
url = endpoint + "listEventTypes/"
 
response = requests.post(url, data=json_req, headers=header)
 
 
print json.dumps(json.loads(response.text), indent=3)