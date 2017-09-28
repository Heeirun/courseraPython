fname= raw_input("What is your file name?")
try:
    fhand= open(fname)
except:
    print "Errror 404: File not found"
    exit()

count= 0
numlist= []
total=0
    

for lines in fhand:
    if not lines.startswith("X-DSPAM-Confidence:"): continue
    count= count+1
    #print count
    #print lines
    snum= lines.find(" ")
    #print snum
    num= lines[snum:]
    #print num
    num= float(num)
    numlist.append(num)

for n in numlist:
    total= total+n
#print total
    

#print numlist

average= total/count

print "Average spam confidence: ", average