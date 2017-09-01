import math
def transPositionCipher():
    key = int(input("Enter the key:"))
    message = input("Enter the message to encrypt:")
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    ciphertext = ''.join(ciphertext)
    print(ciphertext + '|')
def decrypttransPositionCipher():
    key = int(input("Enter the decryption key:"))
    message = input("Enter the message to Decrypt:")
    mycols = int(math.ceil(float(len(message))/key))
    myrows = key
    myshadedboxes = (mycols * myrows) -len(message)
    col = 0
    row = 0
    plainText = ['']*mycols
    for symbol in message:
        plainText[col] += symbol
        col += 1
        if col == mycols or (col == mycols-1 and row >= myrows-myshadedboxes):
            col = 0
            row += 1
    plainText = ''.join(plainText)
    print(plainText)
transPositionCipher()
decrypttransPositionCipher()
