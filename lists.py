cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [0, 12, 34, 7, 82]

# for cheese in cheeses:
#     print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i]*2
print(numbers)

# The + operator concatenates lists:
    # >>> a = [1, 2, 3]
    # >>> b = [4, 5, 6]
    # >>> c = a + b
    # >>> print(c)
    # [1, 2, 3, 4, 5, 6]

# Similarly, the * operator repeats a list a given number of times:
    # >>> [0] * 4
    # [0, 0, 0, 0]
    # >>> [1, 2, 3] * 3
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# SLICE returns a subsection of a list (mutates it)
t = ['a', 'b', 'c', 'd', 'e', 'f']
    # >>> t[1:3]
    # ['b', 'c']
    # >>> t[:4]
    # ['a', 'b', 'c', 'd']
    # >>> t[3:]
    # ['d', 'e', 'f']
    # >>> t[:]
    # ['a', 'b', 'c', 'd', 'e', 'f']
# you can update elements in a list using SLICE. Does not need to be the same num of replacement elements:
t[1:3] = ['x', 'y', 'z']
print(t)
    # ['a', 'x', 'y', 'd', 'e', 'f']

# LIST METHODS
# can list all Python list methods in interpreter, use dir(list)

    # a couple examples:
        
    # EXTEND:
        # extend takes a list as an argument and appends all of the elements:

        # >>> t1 = ['a', 'b', 'c']
        # >>> t2 = ['d', 'e']
        # >>> t1.extend(t2)
        # >>> print(t1)
        # ['a', 'b', 'c', 'd', 'e']
        # This example leaves t2 unmodified.

    # SORT:
        # sort arranges the elements of the list from low to high:

        # >>> t = ['d', 'c', 'e', 'b', 'a']
        # NEED TO FIRST SORT IT, THEN AFTER, PRINT/RETURN IT.
        # >>> t.sort()
        # >>> print(t)
        # ['a', 'b', 'c', 'd', 'e']
        # Most list methods are void; they modify the list and return None. If you accidentally write t = t.sort(), you will be disappointed with the result. 
    
    #DEL
        # If you don’t need the removed value, you can use the del STATEMENT*:

        # >>> t = ['a', 'b', 'c']
        # >>> del t[1]
        # >>> print(t)
        # ['a', 'c']

        # To remove more than one element, you can use del with a slice index:

        # >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
        # >>> del t[1:5]
        # >>> print(t)
        # ['a', 'f']

        # *statements seem to flexible - can be used with many object types (list, string, etc)??

s = 'pining for the fjords'
# print(s[11:14])
t = s.split()
# print(t[2])
# print(t.index('the'))

m = 'spam-spam-spam'
n = m.split('-')
print((' ').join(n))


# >>> a = 'banana'
# >>> b = 'banana'
# >>> a is b
# True

# >>> a = [1, 2, 3]
# >>> b = [1, 2, 3]
# >>> a is b
# False

# >>> a = [1, 2, 3]
# >>> b = a
# >>> b is a
# True
# If the aliased object is mutable, changes made with one alias affect the other:

# >>> b[0] = 17
# >>> print(a)
# [17, 2, 3]
# Although this behavior can be useful, it is error-prone. In general, it is safer to avoid aliasing when you are working with mutable objects.

# For immutable objects like strings, aliasing is not as much of a problem. Because you cannot accidentally mutate a string (it will never change). In this example:

# a = 'banana'
# b = 'banana'


# It is important to distinguish between operations that modify original list (and do not return anything) and operations that create new lists. For example, the append method modifies a list, but the + operator creates a new list:

# List arguments
# >>> t1 = [1, 2]
# >>> t2 = t1.append(3)
# >>> print(t1)
# [1, 2, 3]
# >>> print(t2)
# None

# >>> t3 = t1 + [3]
# >>> print(t3)
# [1, 2, 3]
# >>> t1 is t3
# False

# DEBUGGING
# Careless use of lists (and other mutable objects) can lead to long hours of debugging. Here are some common pitfalls and ways to avoid them:

# Don’t forget that most list methods modify the argument and return None. This is the opposite of the string methods, which return a new string and leave the original alone.

# If you are used to writing string code like this:

# word = word.strip()
# It is tempting to write list code like this:

# t = t.sort()           # WRONG!

# Because sort returns None, the next operation you perform with t is likely to fail.


# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(l):
    l[1:len(l)-1]

print(chop([1,2,3,4]), '- chop function')

def middle(l):
    return l[1:len(l)-1]
print(middle([5,6,7,8]), '- middle function')