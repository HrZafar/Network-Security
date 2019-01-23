text = input('Enter Text: ')
text = text.upper()
key = input('Enter Key(a word): ')
key = key.upper()
cipherText = Text = ''
i = j = 0
while i < len(text):
    if 65 <= ord(text[i]) <= 90:
        num = ord(text[i]) - 64
        num1 = ord(key[j]) - 64
        j += 1
        if j == len(key):
            j = 0
        num += num1
        if num > 26:
            num -= 26
        EC = num + 64
        ch = chr(EC)
        cipherText += ch
    else:
        cipherText += text[i]
    i += 1
print('Encipher: ', cipherText)
i = j = 0
while i < len(cipherText):
    if 65 <= ord(cipherText[i]) <= 90:
        num = ord(cipherText[i]) - 64
        num1 = ord(key[j]) - 64
        j += 1
        if j == len(key):
            j = 0
        num -= num1
        if num < 1:
            num += 26
        EC = num + 64
        ch = chr(EC)
        Text += ch
    else:
        Text += cipherText[i]
    i += 1
print('Decipher: ', Text)
