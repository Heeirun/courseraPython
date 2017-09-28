import urllib.request, urllib.parse, urllib.error
import json

numlist= list()
count= 0

while True:
    address= input ("Enter location: ")
    if len(address)< 1: break
    
    print ("Retrieving ", address)
    uh= urllib.request.urlopen(address)
    data= uh.read()
    #info= data.decode()
    info= json.loads(data)
    #print (info)
    print ("Retrived", len(data), "characters")
    #print ("================REAL DATA===============")

    for item in info["comments"]:
        count= count+1
        num= item['count']
        numlist.append(num)
    
    print ("Count: ", count)
    print ("Sum: ", sum(numlist))
        
        
    
    