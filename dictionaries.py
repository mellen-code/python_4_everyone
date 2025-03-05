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
