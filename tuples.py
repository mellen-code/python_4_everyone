# t = ('a', 'b', 'c', 'd', 'e')
# You can’t modify the elements of a tuple, but you can replace one tuple with another:

# t = ('A',) + t[1:]
# print(t)
# ('A', 'b', 'c', 'd', 'e')


# DSU: Decorate, Sort, Undecorate
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

# TUPLE ASSIGNMENT
# >>> m = ( 'have', 'fun' )
# >>> x, y = m
# >>> x
# 'have'
# >>> y
# 'fun'
# >>>