import urllib.request, urllib.parse, urllib.error
import json

serviceurl= "http://py4e-data.dr-chuck.net/geojson?sensor=false&"

while True:
    address= input("Enter location: ")
    if len(address) <1: break
    
    url= serviceurl+ urllib.parse.urlencode({"address": address})
    print ("Retrieving", url)
    uh= urllib.request.urlopen(url)
    data=uh.read().decode()
    print ("Retrieved", len(data), "characters")
    js= json.loads(data)
    #js= data
        
    #print (js)
    #print ("======REAL DATA======")
    placeid= js["results"][0]["place_id"]
    print ("Place id: ", placeid)
        
   
    
        
    
    