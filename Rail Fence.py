text = input('Enter Text: ')
key = input('Enter Key(a number): ')
key = int(key)
check = 0
len = len(text)

#######################ENCIPHER#######################

cipherText = ''
rail = [[0 for x in range(len)] for y in range(key)]

for x in range(len):
    for y in range(key):
        rail[y][x] = '*'

j = 0

for i in range(len):
    rail[j][i] = text[i]
    if check == 0:
        j += 1
    elif check == 1:
        j -= 1
    if j == key:
        check = 1
        j -= 2
    if j == 0:
        check = 0

j = 0

while j < key:
    for i in range(len):
        if rail[j][i] != '*':
            cipherText += rail[j][i]
    j += 1

print('Encipher:', cipherText)

##########################DECIPHER#########################

Text = ''
fence = [[0 for x in range(len)] for y in range(key)]

for x in range(len):
    for y in range(key):
        fence[y][x] = '*'

k, l = 0, 0

while k < key:
    j, check = 0, 0
    for i in range(len):
        if k == j:
            fence[j][i] = cipherText[l]
            l += 1
        if check == 0:
            j += 1
        elif check == 1:
            j -= 1
        if j == key:
            check = 1
            j -= 2
        if j == 0:
            check = 0
    k += 1

j = 0

while j < len:
    for i in range(key):
        if fence[i][j] != '*':
            Text += fence[i][j]
    j += 1

print('Decipher:', Text)
