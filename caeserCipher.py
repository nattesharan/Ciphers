def caeserCifer():
    key = int(input("Enter the key for encryption:"))
    messageToEncrypt = input("Enter the message to encrypt:")
    messageToEncrypt = messageToEncrypt.upper()
    encryptedMessage = ''
    for i in messageToEncrypt:
        echar = ord(i) + key
        if echar <= 90:
            encryptedMessage += chr(echar)
        if echar > 90:
            echar = echar - 26
            encryptedMessage += chr(echar)
    print(encryptedMessage)
    return encryptedMessage
def decryptCifer():
    key = int(input("Enter the key for decryption:"))
    messageToDecrypt = input("Enter the message to decrypt:")
    messageToDecrypt = messageToDecrypt.upper()
    decryptedMessage = ''
    for i in messageToDecrypt:
        dchar = ord(i) - key
        if dchar >= 65:
            decryptedMessage += chr(dchar)
        if dchar < 65:
            dchar = dchar + 26
            decryptedMessage += chr(dchar)
    print(decryptedMessage.replace(':',' '))
def bruteForceForDecryption(key,a):
    global inputGiven
    if key <= 25:
        messageToDecrypt = a
        key = key
        decryptedMessage = ''
        for i in messageToDecrypt:
            dchar = ord(i) - key
            if dchar >= 65:
                decryptedMessage += chr(dchar)
            if dchar < 65:
                dchar = dchar + 26
                decryptedMessage += chr(dchar)
        print(decryptedMessage.replace(':',' '))
        opt = input("Does the decrypted message has some meaning(y or n):")
        if opt.lower() == 'y':
            pass
        if opt.lower() == 'n':
            bruteForceForDecryption(key+1,a)
    else:
        print("Sorry no valid message found")
a = caeserCifer()
decryptCifer()
bruteForceForDecryption(1,a)
