#fname= raw_input('What is your filename?: ')
#try:
#    fhand= open(fname)
#except:
#    print "Your file cant be found"
#   exit()

#output:
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', #'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', #'through', 'what', 'window', 'with', 'yonder']

fhand= open('romeo.txt')
wlist= []
dup=[]
for lines in fhand:
        wlist= wlist + lines.split()
        #print wlist
        wlist.sort()

for words in wlist:       
    if not words in dup:
        dup.append(words)
    
print dup

    
    
    