# import urllib.request, urllib.parse, urllib.error

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('cover3.jpg', 'wb')
# fhand.write(img)
# fhand.close()

# Code: https://www.py4e.com/code3/curl1.py

# The above code simply takes the data, and READs it all at once (line 3). If data is a large file, could crash computer. Best to take the data in small chunks at a time, to MANAGE THE DATA FLOW:

# This program can read any size file without using up all memory you have in your computer:
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover4.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()

# Code: https://www.py4e.com/code3/curl2.py