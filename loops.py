# infinite loop with continue to jump out of current loop, and break to provide exit condition. 
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')