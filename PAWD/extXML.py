import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url= input ("Enter URL: ")
xml= urllib.request.urlopen(url).read().decode()
#print (xml)
tree= ET.fromstring(xml)

lst= tree.findall ("comments/comment")
numlst= list()

for item in lst:
     num= item.find("count").text
     numlst.append(int(num))

print ("Sum= ", sum(numlst))
#print("Count =", len(numlst))
    
    


