hrs = raw_input("What is the number of hours you worked?: ")
rate= raw_input("What is the hourly rate?: ")

hrs= float(hrs)
rate=float(rate)

if hrs <= 40:

    grosspay= hrs*rate
    
    
if hrs >40:
    
    exhrs=hrs-40
    exrate=rate*1.5

    grosspay= (40*rate) + (exhrs*exrate)
    
print "Your pay is : ", grosspay