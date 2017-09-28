import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


urllist= list()
url= input("Enter URL: ")
count= int(input("Enter count: "))
pos= int(input("Enter position: "))
urllist.append(url)
iter= 0

while iter < count:
    html= urllib.request.urlopen(url).read()
    soup= BeautifulSoup (html, "html.parser")

    addurllist= list()
    tags= soup("a")
    for tag in tags: 
        tag= tag.get("href")
        addurllist.append(tag)
    url= addurllist[pos-1]
    urllist.append(url)
    iter= iter+ 1 

for link in urllist:
    print ("Retrieved:  ",link)
            




  