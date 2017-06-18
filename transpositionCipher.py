def transPositionCipher():
    key = int(raw_input("Enter the key:"))
    message = raw_input("Enter the message to encrypt:")
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    ciphertext = ''.join(ciphertext)
    print(ciphertext + '|')
transPositionCipher()