def findlargest():
    largest= None
    for value in numberlist:
        if largest is None:
            largest= value
        elif value> largest:
            largest= value
        
    print "The largest value is", largest

def findsmallest():
    smallest=None
    for value in numberlist:
        if smallest is None:
            smallest= value
        elif value<smallest:
            smallest= value
    print "The smallest value is: ", smallest
            



junkstrings=[]
numberlist=[]
while True:
    newdata= raw_input("Enter your number: ")
    if newdata == "done": 
            break    
    if newdata != " ":
        try:
            newdata=int(newdata)
            numberlist.append(newdata)
        except ValueError:
            junkstrings.append(newdata)
            print "Invalid input. Please enter a number"

    
#print numberlist
#print junkstrings
findlargest()
findsmallest()




        

    

    