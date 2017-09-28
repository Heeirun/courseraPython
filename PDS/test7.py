
fname=raw_input('Enter the file name in here: ')
try:
    fhand= open(fname)
    count= 0
except: 
    print 'Please enter a valid file name :('
    print 'File cannot be opened:', fname
    exit()

for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
        print line
print 'There were', count, 'subject lines in', fname
