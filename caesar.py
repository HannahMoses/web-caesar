# files copied from crypto's helper.py and caesar.py

def alphabet_position(letter) :
    alpha= letter.lower()
    num=ord(alpha) - 97
#    print(num)
    return num

def rotate_character(char,rot) :
    if char.isalpha():
        if rot<26:
            rot = (alphabet_position(char)) + rot
            rot= rot%26
#            print(char ,'returns rot value ',rot)
            newChar = chr((rot+97))
            if char.isupper():
                newChar = newChar.upper()

        else:
            rot=rot-26
            rot = (alphabet_position(char)) + rot
            rot=rot%26
#            print(char ,'returns rot value ',rot)
            newChar = chr((rot+97))
            if char.isupper():
                newChar = newChar.upper()
    else:
        newChar=char
    return newChar

#from crypto caesar.py
def encrypt(text,rot) :
    newChar=''
#    for i in range(len(text)):
    newChar+= newChar
    for letr in text :
#        print('letr= ',letr)
        rotate_character(letr,rot)
        newChar+=rotate_character(letr,rot)
    return newChar
