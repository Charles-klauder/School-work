from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyz"
#======================================
#Binary Dictionaries
ChartoBinary = {
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
BinarytoChar = {
'00110001':'1','00110010':'2','00110011':'3','00110100':'4',
'00110101':'5','00110110':'6','00110111':'7','00111000':'8',
'00111001':'9','00110000':'0',
'01100001':'a','01100010':'b','01100011':'c','01100100':'d',
'01100101':'e','01100110':'f','01100111':'g','01101000':'h',
'01101001':'i','01101010':'j','01101011':'k','01101100':'l',
'01101101':'m','01101110':'n','01101111':'o','01110000':'p',
'01110001':'q','01110010':'r','01110011':'s','01110100':'t',
'01110101':'u','01110110':'v','01110111':'w','01111000':'x',
'01111001':'y','01111010':'z','01111110':'~','00100000':' '}
#======================================
#Morse Dictionaries
chartomorse = {'a':'.-','b':'-...','c':'-.-.','d':'-..',
               'e':'.','f':'..-.','g':'--.','h':'....',
               'i':'..','j':'.---','k':'-.-','l':'.-..',
               'm':'--','n':'-.','o':'---','p':'.--.',
               'q':'--.-','r':'.-.','s':'...','t':'-',
               'u':'..-','v':'...-','w':'.--','x':'-..-',
               'y':'-.--','z':'--..'}
morsetochar = {'.-':'a','-...':'b','-.-.':'c','-..':'d',
               '.':'e','..-.':'f','--.':'g','....':'h',
               '..':'i','.---':'j','-.-':'k','.-..':'l',
               '--':'m','-.':'n','---':'o','.--.':'p',
               '--.-':'q','.-.':'r','...':'s','-':'t',
               '..-':'u','...-':'v','.--':'w','-..-':'x',
               '-.--':'y','--..':'z'}
#======================================
#binaryencoder
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
#binary decoder
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
#Text to Morse
def TTM(str, chartomorse):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for char in str:
        if char not in alphabet:
            output = output
        else:
            output += chartomorse[char]
            output += "/"
    output = output[:-1]
    return output
#Morse to Text
def MTT(morse, morsetochar):
    temp1 = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for char in morse:
        if char == ".":
            temp1 += "."
        elif char == "-":
            temp1 += "-"
        elif char == "/":
            output += morsetochar[temp1]
            temp1 = ""
        else:
            output = str(output)
    output += morsetochar[temp1]
    return output
#======================================
#input section
action = "while"
while action == "while":
    action = input("would you like to encode binary, decode binary, translate morse or stop? \n")
    if action == "encode binary":
        uncoded = input("enter message to encode. \n")
        zero = input("input 0 replacers (lowercase only) \n")
        one = ""
        for letter in alphabet:
            if letter not in zero:
                one += letter
        coded = (encode(ChartoBinary, uncoded, zero, one))
        print(coded)
        action = "while"
    elif action == "decode binary":
        encoded = input("enter encoded message. \n")
        zero = input("input 0 replacers (lowercase only) \n")
        one = ""
        for letter in alphabet:
            if letter not in zero:
                one += letter
        decoded = (decode(BinarytoChar, encoded, zero, one))
        print(decoded)
        action = "while"
    elif action == "translate morse" or action == "morse":
        act = input("would you like to translate text to morse or morse to text? (mtt/ttm)\n")
        if act == "morse to text" or act == "mtt":
            text = input("Input Morse \n (make sure there is an / between charecters) \n")
            print(MTT(text, morsetochar))
            action = "while"
        elif act == "text to morse" or act == "ttm":
            text = input("Input Text \n")
            print(TTM(text,chartomorse))
            action = "while"
        else:
            print("error incorrect input")
            action = "while"
    elif (action == "Stop") or (action =="stop"):
        action = "stopping"
        print(action)
    else:
        print("error incorrect input")
        action = "while"
#======================================
