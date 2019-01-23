text = input('Enter Text(8 bits): ')
key = input('Enter Key(10 bits): ')

#########################TABLES##############################

class tables():
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P_8 = [6, 3, 7, 4, 8, 5, 10, 9]
    P_4 = [2, 4, 3, 1]
    IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]

    S0 = [['01', '00', '11', '10'],
          ['11', '10', '01', '00'],
          ['00', '10', '01', '11'],
          ['11', '01', '11', '10']]

    S1 = [['00', '01', '10', '11'],
          ['10', '00', '01', '11'],
          ['11', '00', '01', '00'],
          ['10', '01', '00', '11']]


#####################LEFT CIRCULAR SHIFT######################

def LCS(k):
    k1 = ''
    for i in range(len(k)):
        if i == len(k)-1:
            k1 = k1 + k[0]
        else:
            k1 = k1 + k[i + 1]
    return k1

##########################XOR############################

def xor(a, b):
    k = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            k = k + '0'
        else:
            k = k + '1'
    return k

#########################S0/S1##############################

def get_s_value(s, n):
    row = s[0] + s[3]
    col = s[1] + s[2]
    if row == '00':
        r = 0
    elif row == '01':
        r = 1
    elif row == '10':
        r = 2
    elif row == '11':
        r = 3
    if col == '00':
        c = 0
    elif col == '01':
        c = 1
    elif col == '10':
        c = 2
    elif col == '11':
        c = 3

    s_tables=tables()
    if n == 0:
        return s_tables.S0[r][c]
    elif n == 1:
        return s_tables.S1[r][c]

#######################ROUNDs#############################

def round(text, key, n):
    text_L = ''
    text_R = ''
    text_EP = ''
    s0 = ''
    s1 = ''
    tab=tables()

    for i in range(4):
        text_L = text_L + text[i]
        text_R = text_R + text[i + 4]

    for i in range(len(tab.EP)):
        text_EP = text_EP + text_R[tab.EP[i] - 1]

    text_EP = xor(text_EP, key)
    for i in range(4):
        s0 = s0 + text_EP[i]
        s1 = s1 + text_EP[i + 4]

    s0 = get_s_value(s0, 0)
    s1 = get_s_value(s1, 1)

    s = s0 + s1
    p4 = ''
    for i in range(len(tab.P_4)):
        p4 = p4 + s[tab.P_4[i] - 1]

    if n == 1:
        temp = text_R
        text_R = xor(p4, text_L)
        text_L = temp
    elif n == 2:
        text_L = xor(p4, text_L)

    return text_L + text_R

#########################KEY GENERATION######################

def generate_keys():
    key_P10 = ''
    key_P10_1 = ''
    key_P10_2 = ''
    key1 = ''
    key2 = ''
    tab=tables()

    for i in range(len(tab.P_10)):
        key_P10 = key_P10 + key[tab.P_10[i] - 1]
    for i in range(5):
        key_P10_1 = key_P10_1 + key_P10[i]
        key_P10_2 = key_P10_2 + key_P10[i + 5]

    key_P10_1 = LCS(key_P10_1)
    key_P10_2 = LCS(key_P10_2)

    k1 = key_P10_1 + key_P10_2
    for i in range(len(tab.P_8)):
        key1 = key1 + k1[tab.P_8[i] - 1]

    key_P10_1 = LCS(key_P10_1)
    key_P10_2 = LCS(key_P10_2)
    key_P10_1 = LCS(key_P10_1)
    key_P10_2 = LCS(key_P10_2)

    k2 = key_P10_1 + key_P10_2
    for i in range(len(tab.P_8)):
        key2 = key2 + k2[tab.P_8[i] - 1]

    return key1,key2

######################ENCIPHER############################
tab=tables()
textIP = ''
for i in range(len(tab.IP)):
    textIP = textIP + text[tab.IP[i] - 1]

key1,key2=generate_keys()
text1 = round(textIP, key1, 1)
text2 = round(text1, key2, 2)
cipherText = ''
for i in range(len(tab.IP_1)):
    cipherText = cipherText + text2[tab.IP_1[i] - 1]

print('Encipher: ', cipherText)

######################DECIPHER############################

textIP = ''
for i in range(len(tab.IP)):
    textIP = textIP + cipherText[tab.IP[i] - 1]

key2,key1=generate_keys()
text1 = round(textIP, key1, 1)
text2 = round(text1, key2, 2)
Text = ''
for i in range(len(tab.IP_1)):
    Text = Text + text2[tab.IP_1[i] - 1]

print('Decipher: ', Text)
