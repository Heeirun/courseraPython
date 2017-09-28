import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#try to import ssl on this

url= input("Enter - ")
html= urllib.request.urlopen(url).read()
soup= BeautifulSoup(html, "html.parser")

total= 0
#print (soup) #test1 
tags= soup ("span")#this actually finds all span tags and puts them in a list straight
#print (tags) 
for tag in tags:
    #print ("Tag : ", tag)
    tag= tag.contents[0]
    #print (tag)
    total= total+ int(tag)
print (total)
    