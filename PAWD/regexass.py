import re
numlist= list()
intnumlist= list()
fname= "regex_sum_5115.txt"
fhand= open(fname)

for line in fhand:
    line= line.rstrip()
    num= re.findall ("[0-9]+", line)
    if len(num) < 1:continue
    for things in num:
        numlist.append(int(things))
            
print sum(numlist)
    
    