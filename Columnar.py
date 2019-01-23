text = input('Enter Text: ')
key = input('Enter Key(a word): ')
key = key.upper()
k_len = len(key)
t_len = len(text)

#######################ENCIPHER########################

cipherText = ''
row, k = 0, 0
row = t_len / k_len
row = int(row)

if t_len % k_len != 0:
    row += 1

col = [[0 for x in range(k_len)] for y in range(row)]

for i in range(row):
    for j in range(k_len):
        if k < t_len:
            col[i][j] = text[k]
        else:
            col[i][j] = '*'
        k += 1

seq = [0 for x in range(k_len)]
seq1 = [0 for x in range(k_len)]
count = 0

for i in range(k_len):
    seq[i] = ord(key[i]) - 64

while count < len(seq1):
    mini = 100
    index = -1
    for i in range(len(seq)):
        if seq[i] < mini:
            mini = seq[i]
            index = i
    seq[index] += 50
    seq1[count] = index
    count += 1

count = 0

while count < len(seq1):
    index = seq1[count]
    for i in range(row):
        cipherText += col[i][index]
    count += 1

print('Encipher:', cipherText)

##########################DECIPHER#########################

Text = ''
t_len = len(cipherText)
row = t_len / k_len
row = int(row)

if t_len % k_len != 0:
    row += 1

col1 = [[0 for x in range(k_len)] for y in range(row)]

for i in range(k_len):
    seq[i] = ord(key[i]) - 64

count = 0

while count < len(seq1):
    mini = 100
    index = -1
    for i in range(len(seq)):
        if seq[i] < mini:
            mini = seq[i]
            index = i
    seq[index] += 50
    seq1[count] = index
    count += 1

count = 0
k = 0

while count < len(seq1):
    index = seq1[count]
    for i in range(row):
        if k < len(cipherText):
            col1[i][index] = cipherText[k]
            k += 1
    count += 1

for i in range(row):
    for j in range(k_len):
        if col1[i][j] != '*':
            Text += col1[i][j]

print('Decipher:', Text)
