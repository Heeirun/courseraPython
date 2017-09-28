import urllib.request, urllib.parse, urllib.error

fhand= urllib.request.urlopen('http://www.dr-chuck.com/pag1.htm')

wlist= list()
words= list()
for line in fhand:
    code= line.decode().strip()
    code= code.strip().split()
    #print (code)
    wlist.extend(code)
#print (wlist)

for object in wlist:
    if object.startswith("h"):
        stlink= object.find("=")
        link= object[stlink+2:-2]

print (link)
    
   