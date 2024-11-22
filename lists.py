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