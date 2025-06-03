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

print(res)

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
