#given a string from terminal input, it will complexify it
#1. enter the String
#2. encript it or decript it
#3. give output

import sys
from string import digits


def encryption(this):
    key = '@b(d3fg#!)k|mn0pqr$tuvwxyz'
    text = 'abcdefghijklmnopqrstuvwxyz'
    translation = str.maketrans(text, key)
    return this.translate(translation)

def decryption(this):

    key = '@b(d3fg#!)k|mn0pqr$tuvwxyz'
    text = 'abcdefghijklmnopqrstuvwxyz'
    translation = str.maketrans(key, text)
    return this.translate(translation)


if __name__ == "__main__":

    text_input = input("Enter the string \n  >>  ")
    if len(sys.argv) ==1:
        mode = input("Do you want to:\n\t\t1 : Encrypt it\n\t\t2 : decrypt it\n  >>  ")
    else:
        mode = sys.argv[0]
    if mode is '1':
        print (encryption(text_input))
    elif mode is '2':
        print (decryption(text_input))