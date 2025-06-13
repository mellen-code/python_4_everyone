# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
    
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = input('Enter file name: ')
if len(name) < 1:
    name = 'mbox_short.txt'
fhand = open(name)

hours_counts = dict()
res = list()

for line in fhand:
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        full_time = words[5]
        hour = full_time.split(':')[0]
        hours_counts[hour] = hours_counts.get(hour, 0) + 1
        # if hour in hours_counts:
        #     hours_counts[hour] += 1
        # else:
        #     hours_counts[hour] = 1

# loop through dictionary key/value pairs and append to a list as tuples
for key, val in hours_counts.items():
    res.append((key, val))

# sort the list of tuples by keys ascending (first value in the tuple), and print each tuple
res.sort()
for key, val in res:
    print(key, val)