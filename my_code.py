from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyz"
#======================================
#Binary Dictionaries
BinarytoChar = {
          '1':'00110001','2':'00110010','3':'00110011','4':'00110100',
          '5':'00110101','6':'00110110','7':'00110111','8':'00111000',
          '9':'00111001','0':'00110000',
          
          'a':'01100001','b':'01100010','c':'01100011','d':'01100100',
          'e':'01100101','f':'01100110','g':'01100111','h':'01101000',
          'i':'01101001','j':'01101010','k':'01101011','l':'01101100',
          'm':'01101101','n':'01101110','o':'01101111','p':'01110000',
          'q':'01110001','r':'01110010','s':'01110011','t':'01110100',
          'u':'01110101','v':'01110110','w':'01110111','x':'01111000',
          'y':'01111001','z':'01111010','~':'01111110',' ':'00100000'}
ChartoBinary = {}
for k, v in BinarytoChar.items():
    ChartoBinary[v] = k
#======================================
#encoder
def encode(binary, uncoded, zero, one):
    bina = []
    temp1 = ""
    temp2 = ""
    encoded = ""
    for char in uncoded:
        temp1 = binary[char]
        bina.append(temp1)
    for letter in bina:
        for char in letter:
            if char == "0":
                temp2 = zero[randint(0,len(zero)-1)]
            elif char == "1":
                temp2 = one[randint(0,len(one)-1)]
            encoded += temp2
    return encoded
#decoder
def decode(binary, encoded, zero, one):
    bina = ""
    temp1 = ""
    temp2 = ""
    temp3 = []
    decoded = ""
    for char in encoded:
        if char in zero:
            temp1 = "0"
        elif char in one:
            temp1 = "1"
        bina += temp1
    for letter in bina:
        if len(temp2) < 8:
            temp2 += letter
        else:
            temp3.append(temp2)
            temp2 = letter
    temp3.append(temp2)
    for charecter in temp3:
        decoded += binary[charecter]
    return decoded
#======================================
#input section
action = "while"
while action == "while":
    action = input("would you like to encode, decode or stop? \n")
    if (action == "Encode") or (action == "encode"):
        uncoded = input("enter message to encode. \n")
        zero = input("input 0 replacers (lowercase only) \n")
        one = ""
        for letter in alphabet:
            if letter not in zero:
                one += letter
        coded = (encode(BinarytoChar, uncoded, zero, one))
        print(coded)
        action = "while"
    elif (action == "Decode") or (action == "decode"):
        encoded = input("enter encoded message. \n")
        zero = input("input 0 replacers (lowercase only) \n")
        one = ""
        for letter in alphabet:
            if letter not in zero:
                one += letter
        decoded = (decode(ChartoBinary, encoded, zero, one))
        print(decoded)
        action = "while"
    elif (action == "Stop") or (action =="stop"):
        action = "stopping"
        print(action)
    else:
        print("error incorrect input")
        action = "while"
#======================================