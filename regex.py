# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times 
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times 
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end




# Search for lines that start with From and have an at sign
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:.+@', line):
#         print(line)

# This matches lines that start with 'From:', followed by one or more characters (.+), following by an at-sign ---> the last at-sign if there are more than 1 in the line.

# *+  zero or more characters


# EXTRACT EMAIL ADDRESSES.  Search for lines that have an at-sign between non-whitespace characters:
# import re
# fhand = open('mbox_short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)


# Search for lines that have an at sign between characters
# The characters must be a letter or number
# import re
# hand = open('mbox_short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall(r'[a-zA-Z0-9]\S*@[a-zA-Z]\S*', line)
#     if len(x) > 0:
#         print(x)


# Find lines that start with 'X-' and extract the number (can be a float):
# import re
# fhand = open('mbox_short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('X\S*: [0-9.]+', line):
#         print(line)
# This prints the entire line.

# If you want to SEARCH and EXTRACT, use findall(). Parentheses indicate that while you want the whole expression to match, you are interested in extracting a portion of the substring.
# import re
# fhand = open('mbox_short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x):
#         x_string = "".join(x)
#         x_num = float(x_string)
#         print(x_num)

# EXERCISE TO DO:
# Find lines with email addresses and extract the HOUR only e.g.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# should only extract 09
import re
fhand = open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^From: .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)

# print('test')


# EXCERISE:
# Match the dollar amount only:
money = 'We just received $10.00 for cookies.'
return_money = re.findall('\$[0-9.]+', money)
# print(return_money)

# Prefixing the '$' with a backslash, escapes the '$' symbolic meaning. It just looks for a '$'.
# [0-9.] matches digits or a period.
    # Inside brackets, period is a period
    # Outside brackets, period is 'wild-card' character



# SAMPLE EXERCISE
import re
hand = open('regex_sample_ex.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        for num in x:
            int_num = int(num)
            sum += int_num
print(sum)