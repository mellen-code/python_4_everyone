# t = ('a', 'b', 'c', 'd', 'e')
# You can’t modify the elements of a tuple, but you can replace one tuple with another: 
# **THEY ARE IMMUTABLE
# **THEY ARE COMPARABLE - can sort lists of them
# **THEY ARE HASHABLE - use as key values in dictionaries

# t = ('A',) + t[1:]
# print(t)
# ('A', 'b', 'c', 'd', 'e')


# ****DSU: Decorate, Sort, Undecorate
# For example, suppose you have a list of words and you want to sort them from longest to shortest:

txt= 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length,word in t:
    res.append(word)

# print(res)

# ****TUPLE ASSIGNMENT
# >>> m = ( 'have', 'fun' )
# >>> x, y = m
# >>> x
# 'have'
# >>> y
# 'fun'
# >>>

addr = 'monty@python.org'
uname, domain = addr.split('@')
# this assigns 'monty' to uname variable, and 'python.org' to domain variable

# ****DICTONARIES AND TUPLES

# items() method returns a list of tuples as key-value pairs
# d = {'b':1, 'a':10, 'c': 22}
# t = list(d.items())
# print(t)
# [('b':1), ('a':10), ('c': 22)]
# ***t is wrapped in a list. If not, it would return as:
# dict_items([('b':1), ('a':10), ('c': 22)])


# ****MULTIPLE ASSIGNMENT WITH DICTIONARIES
# d = {'a':10, 'b':1, 'c': 22}
# for key, val in d.items():
#   print(d)
# 
# 10 a
# 1 b
# 22 c
# note, in hash key order (i.e. no particular order)


# to print out contents of dictionary sorted by the VALUE stored in each key-value pair:
# d = {'a':10, 'b':1, 'c': 22}
# l = list()
# for key, val in d.items():
#   l.append( (val, key) )
# 
# l.sort(reverse=True)
# 
# [(22, 'c'), (10, 'a'), (1, 'b')]



# ***ROMEO AND JULIET EXERCISE
import string
fhand = open('romeo.txt')

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

for key, val in lst[:10]:
    # print(key, val)
# returns:
# 3 the
# 3 is
# 3 and
# 2 sun
# 1 yonder
# 1 with
# 1 window
# 1 who
# 1 what
# 1 through
    # print(f"{key=}, {val=}")
# key=3, val='the'
# key=3, val='is'
# key=3, val='and'
# key=2, val='sun'
# key=1, val='yonder'
# key=1, val='with'
# key=1, val='window'
# key=1, val='who'
# key=1, val='what'
# key=1, val='through'
    print(f"{key}, {val}")
# 3, the
# 3, is
# 3, and
# 2, sun
# 1, yonder
# 1, with
# 1, window
# 1, who
# 1, what
# 1, through

'''Multiple lines comment
testing multiple line string
with three single quotes
can also be with double quotes
If forget about the quotes, highlight in vsCode
and alt-shift-A!'''


# ***Using tuples as keys in dictionaries
# Because tuples are hashable and lists are not, if we want to create a composite* key to use in a dictionary we must use a tuple as the key.

# *composite key = unique identifier. Can contain multiple values, as a tuple

# Assuming that we have defined the variables last, first, and number, we could write a dictionary assignment statement as follows:
# directory[last,first] = number

# The expression in brackets is a tuple.

# We could use tuple assignment in a for loop to traverse this dictionary.

# for last, first in directory:
    # print(first, last, directory[last,first])

# This loop traverses the keys in directory, which are tuples. It assigns the elements of each tuple to last and first, then prints the name and corresponding telephone number.


# ***Sequences: strings, lists, and tuples - Oh My!

# In many contexts, the different kinds of sequences (strings, lists, and tuples) can be used interchangeably. So how and why do you choose one over the others?

    # ***STRINGS
    # - more limited than other sequences because the elements have to be characters. 
    # - They are also immutable. 
        # - If you need the ability to change the characters in a string (as opposed to creating a new string), you might want to use a list of characters instead.

    # ***LISTS
    # - more common than tuples
    # - mutable

    # ***TUPLES
    # - In some contexts, like a return statement, it is syntactically simpler to create a tuple than a list. In other contexts, you might prefer a list.

    # - If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.

    # - If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

    # - Because tuples are immutable, they don’t provide methods like sort and reverse, which modify existing lists. 

    # - However Python provides the built-in functions sorted and reversed, which take any sequence as a parameter and return a new sequence with the same elements in a different order.
