string = raw_input()

character = ''
X = 0

for i in string:
    if i == character:
        X += 1 
    else:
        if character != '':
            print('(%d, %s)' % (X, character))
        character = i
        X = 1
        
print('(%d, %s)' % (X, character))
