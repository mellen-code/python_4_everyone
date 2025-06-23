# Find lines with email addresses and extract the HOUR only e.g.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# should only extract 09
print('why not printing')

import re
hand = open('mbox_short.txt')
for line in hand:
    line = line.strip()
    x = re.findall('^From: .* ([0-9][0-9]):', line)
    if len(x) > 0: 
        print(x)