text= "X-DSPAM-Confidence:    0.8475";
firstnum= text.find(" ")

num= text[firstnum: ]
num= float(num)
print num
