import re
fhand= open ("mbox-short.txt")
numlist= list()
for line in fhand:
    line= line.rstrip()
    stuff= re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff)!= 1: 
        continue
    num= float (stuff[0])
    numlist.append(num)
print ("Maximum: ", max(numlist) )

#code below got the total but removed similar numbers before adding!
import re
numlist= list()
intnumlist= list()
fname= "regex_sum_42.txt"
fhand= open(fname)

for line in fhand:
    line= line.rstrip()
    num= re.findall ("[0-9]+", line)
    if len(num) <= 1:continue
    for things in num:
        if not things in numlist:
            numlist.append(int(things))
            

print sum(numlist)