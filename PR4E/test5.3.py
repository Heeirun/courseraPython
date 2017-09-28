smallest_so_far= None
print "Current smallest number:", smallest_so_far

for the_num in [3, 41, 12, 9, 74, 15]:
    
    if smallest_so_far is None:
        smallest_so_far= the_num
    elif the_num< smallest_so_far:
        smallest_so_far= the_num
    print smallest_so_far, the_num

print"Final smallest number from the list: ", smallest_so_far
