# name = input('Enter file: ')
# handle = open(name, 'r')
# counts = dict()

# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word, count in list(counts.items()):
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)

# Code: https://www.py4e.com/code3/words.py

first = "test "
second = 3
print(first * second)  # => 'test test test'

# standard is snake_case for python (not camelCase as in JavaScript)
# variable names are case sensitive

x = 3
if x < 10:
    print('small')
