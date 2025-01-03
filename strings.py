# Strings are immutable!
# e.g. cannot do the following:
str = 'Hello World'
# str[0] = 'J'

# can do this instead:
strTheSecond = 'J' + str[1:]
print(strTheSecond)

def letter_count(str, ltr):
    count = 0
    for letter in str:
        if letter == ltr:
            count = count + 1
    return count

print(letter_count("banana", "a"))

# Question: why the 'return' within letter_count function instead of print, and use print for the function call on line 17?
# Answer: to call function and pass in values and print answers based on what is passed in. 
    # -- it's a fruitful function, it returns something. A void function doesn't return anything.

# The 'in' operator:
# >>> 'a' in 'banana'
# True
# >>> 'seed' in 'banana'
# False


# example string method from 
# https://docs.python.org/3/library/stdtypes.html#string-methods:
# str.count(sub[, start[, end]])
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

# If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.


# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

start = text.find('0')
num = (text[start:])
print(float(num))