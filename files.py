# fname = input('Enter the file name: ')

# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# Exercise:
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter file name: ')

try:
    fh = open(fname)
except:
    print(f'File cannot be found: {fname}')
    exit()

total = 0
count = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        # print(line)
        start = line.find('0')
        num = float(line[start:])
        # print(num)
        total += num
        count += 1
print(f"Average spam confidence: {total/count}")