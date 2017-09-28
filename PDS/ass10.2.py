fname= raw_input("Enter filename: ")
if len(fname) <1: fname= "mbox-short.txt"
fhand= open(fname)

counts= dict()
for lines in fhand:
    if lines.startswith("From "):
         words= lines.split()
         time= words[5]
         hour= time[:2]
         counts[hour]= counts.get(hour,0) +1

lst= list()
for k,v in counts.items():
    lst.append( (k,v) )
    lst.sort()

for k,v in lst:
    print k,v
         

        