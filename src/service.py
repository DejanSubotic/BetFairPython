import requests
import json

endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"
 
header = { 'X-Application' : 'JOIdNhZjPP4AK9F4', 'X-Authentication' : 'snbcJvB8HBRDrjoXPgrdCh+n7njJDx3AKD106Hk5cjg=' ,'content-type' : 'application/json' }
 
json_req='{"filter":{ }}'
 
url = endpoint + "listEventTypes/"

response = requests.post(url, data=json_req, headers=header)
 
 
print json.dumps(json.loads(response.text), indent=3)