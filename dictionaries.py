# A dictionary is like a list, but more general. In a list, the index positions have to be integers; in a dictionary, the indices can be (almost) any type.

# You can think of a dictionary as a mapping between a set of indices (which are called keys) and a set of values. Each key maps to a value. The association of a key and a value is called a key-value pair or sometimes an item.

# The function dict creates a new dictionary with no items. Because dict is the name of a built-in function, you should avoid using it as a variable name.

# >>> eng2sp = dict()
# >>> print(eng2sp)
# {}
# >>> eng2sp['one'] = 'uno'
# >>> print(eng2sp)
# {'one': 'uno'}

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# If the key isn’t in the dictionary, you get an exception:
# >>> print(eng2sp['four'])
# KeyError: 'four'

# >>> len(eng2sp)
# 3

# The in operator works on dictionaries; it tells you whether something appears as a key in the dictionary (appearing as a value is not good enough).

# To search for a VALUE in a dictionary:
# >>> vals = list(eng2sp.values())
# >>> 'uno' in vals
# True

# in operator --> uses different algorithms for lists and dictionaries
    # LISTS: uses linear search
    # DICTIONARIES: uses a hash table, which uses the same time complexity to search a dictionary no matter how many items it contains


# EXERCISE: Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
# fname = input('Enter file name: ')
# fhand = open(fname)
# for line in fhand:
#     all_words = dict()
#     line = line.rstrip().split(' ')
#     for word in line:
#         # print(word)
#         all_words[word] = 1
# print(all_words)


# count the instances of each letter in a word:
# mushu = iterator variable

# word = 'brontosaurus'
# d = dict()
# for mushu in word:
#     if mushu not in d:
#         d[mushu] = 1
#     else:
#         d[mushu] += 1
# print(d)

# OR:
# use get()
word = 'brontosaurus'
d = dict()
for moomoo in word:
    d[moomoo] = d.get(moomoo,0) + 1
print(d)

# diction = dict()
# for letter in word:
#     diction[letter] = diction.get(letter, 0) + 1
# print(diction)





# Histogram - counts frequencies (a statistical term for a set of counters/frequencies)
counts = {}
names = ['name1', 'ben', 'cewn', 'cewn']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1


# x = counts.get(name, 0)
# print(x)
# second arg - 0 - is default value of name

# SO:
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# ADVANCED TEXT PARSING
# use translate()
# import string

# fname = input('Enter file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     line = line.rstrip()
    
#     line = line.translate(line.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()

#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# print(counts)




# EXERCISE 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# split the file into lines. For each line, if the line starts with 'From', add the word to a dictionary if the word isn't in there, if it is, add 1 to the word's count. Return the dictionary.

# fname = input('Enter a file name: ')
# if len(fname) < 1:
#     fname = 'mbox_short.txt'

# fhand = open(fname)

# days = dict()
# for line in fhand:
#     line = line.split(' ')

#     if len(line) > 1 and line[0] == 'From':
#         # if line[2] not in days:
#         #     days[line[2]] = 1
#         # else:
#         #     days[line[2]] += 1
#         days[line[2]] = days.get(line[2], 0) + 1

# print(days)



# EXERCISE 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'mbox_short.txt'
#     fhand = open(fname)
# else:
#     try:
#         fhand = open(fname)
#     except:
#         print('File not found', fname)
#         exit()

# emails = dict()
# for line in fhand:
#     words = line.split()

#     if len(words) > 1 and words[0] == 'From':
#         emails[words[1]] = emails.get(words[1], 0) +1

# print(emails)




# EXERCISE 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

# Using EXERCISE 3 code, after the loop to add data to dictionary, move dictionary's values to a list, get the max value, and find that value's key in the dictionary and return the pair as a string.

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox_short.txt'
    fhand = open(fname)
else:
    try:
        fhand = open(fname)
    except:
        print('File not found', fname)
        exit()

emails = dict()
for line in fhand:
    words = line.split()

    if len(words) > 1 and words[0] == 'From':
        emails[words[1]] = emails.get(words[1], 0) +1

# values = list(emails.values())
# max_value = max(values)
# key_of_max_value = [key for key, val in emails.items() if val == max_value]
# print("".join(key_of_max_value), max_value)

# OR just loop thru the dictionary and store max!
max_key = ''

# using .get() to search for max_key value in emails. If it doesn't exist, max_key value is set to zero:
for key in emails:
    if emails[key] > emails.get(max_key, 0):
        max_key = key

print(max_key, emails[max_key])
