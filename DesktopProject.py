from random import randint
uncoded = input("enter message. \n")
Binary = {'1':'00110001','2':'00110010','3':'00110011','4':'00110100',
          '5':'00110101','6':'00110110','7':'00110111','8':'00111000',
          '9':'00111001','0':'00110000',
          
          'a':'01100001','b':'01100010','c':'01100011','d':'01100100',
          'e':'01100101','f':'01100110','g':'01100111','h':'01101000',
          'i':'01101001','j':'01101010','k':'01101011','l':'01101100',
          'm':'01101101','n':'01101110','o':'01101111','p':'01110000',
          'q':'01110001','r':'01110010','s':'01110011','t':'01110100',
          'u':'01110101','v':'01110110','w':'01110111','x':'01111000',
          'y':'01111001','z':'01111010','~':'01111110',' ':'00100000'}
zero = input("input 0 replacers (lowercase only) \n")
one = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    if letter not in zero:
        one += letter
one = ""
def encode(binary, uncoded, zero, one):
    bina = []
    temp = ""
    temp2 = ""
    temp3 = ""
    for char in uncoded:
        temp = binary[char]
        bina.append(temp)
    for letter in bina:
        for char in letter:
            if char == "0":
                temp2 = zero[randint(len(zero))]
            elif char == "1":
                temp2 = one[randint(len(one))]
            temp3 += temp2


encode(Binary, uncoded, zero, one)









#desk1 = [test.txt]
#desk2 = []
#Storage = "C:\Users\XLHS\OneDrive\Desktop\altdesk"
#temp = "C:\Users\XLHS\OneDrive\Desktop\Temp"
#import shutil
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("C:\Users\XLHS\OneDrive\Desktop\altdesk\test.txt", "C:\Users\XLHS\OneDrive\Desktop\Temp")
#def move(destination, storage):
#    Storage = "C:\Users\XLHS\OneDrive\Desktop\altdesk"
#    temp = "C:\Users\XLHS\OneDrive\Desktop\Temp"
#    for objec in destination:
#        file = temp + objec
#        print(file)

#move(desk1,desk2)
#print(f"{storage}{desk1(0)}")
