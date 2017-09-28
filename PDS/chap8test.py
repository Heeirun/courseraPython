fhand= open ('mbox-short.txt')
fname= raw_input("What is the filename?: ")
try:
    fhand= open(fname)
    count= 0
except:
    print "Your file cannot be found"
    exit()

for line in fhand:
    line= line.rstrip()
    words= line.split()
    if (len(words) == 0 or len(words) < 3) or words[0] != 'From' : continue
    print words[2]
    
#double splitting
line= "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

words= line.split()
email= words[1]
#print email
address= email.split('@')
print address[1]

    
    
    


    
    






