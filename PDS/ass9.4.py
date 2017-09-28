name= raw_input("Enter filename: ")
handle= open(name)


counts= dict()
for line in handle:
    if line.startswith("From "):
        line= line.split()
        email= line[1]
        counts[email]= counts.get(email,0)+1
    
bigcount= None
bigword= None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword= word
        bigcount= count
print bigword, bigcount