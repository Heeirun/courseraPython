print "Email counter!"
fhand= open('mbox-short.txt')
count= 0
for lines in fhand:
    lines= lines.rstrip()
    if lines.startswith('From:'):
        count= count+1
        print count,'\t', lines

print 'Total number of emails is: ', count
    

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
print "Done"