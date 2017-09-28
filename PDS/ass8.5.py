fname= raw_input("Enter file name: ")
count= 0
try:
    fhand= open(fname)
except:
    print" Please enter a valid file name!\n"
    exit()
    
for lines in fhand:
    if not lines.startswith("From "): 
        continue
    count += 1
    lines= lines.split()
    print lines[1]

print "There were", count,"lines in the file with From as the first word"
    