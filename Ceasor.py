text = input('Enter Text: ')
text = text.upper()
key = input('Enter Key(a number): ')
key = int(key)
i = 0
cipherText = Text = ''
while i < len(text):
    if 65 <= ord(text[i]) <= 90:
        num = ord(text[i]) - 64
        EC = (num + key) % 26
        if EC == 0:
            EC += 26
        EC += 64
        ch = chr(EC)
        cipherText += ch
    else:
        cipherText += text[i]
    i += 1
print('Encipher: ', cipherText)
i = 0
while i < len(cipherText):
    if 65 <= ord(cipherText[i]) <= 90:
        num = ord(cipherText[i]) - 64
        if num <= key:
            EC = (num - key) + 26
        else:
            EC = (num - key) % 26
        EC += 64
        ch = chr(EC)
        Text += ch
    else:
        Text += cipherText[i]
    i += 1
print('Decipher: ', Text)
