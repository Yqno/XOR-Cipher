import sys

KEY = "x"

def xor(data, key):
    key = str(key)
    output_str = ""
    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr(current ^ ord(current_key))
    return output_str

def printCiphertext(ciphertext):
    print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')

try:
    plaintext = open(sys.argv[1], "rb").read()
except IndexError:
    print("File argument needed! Usage: %s <filename>" % sys.argv[0])
    sys.exit()

ciphertext = xor(plaintext, KEY)
printCiphertext(ciphertext)
