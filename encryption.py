#encrypts stuff

def encrypt(message, key):
    output = ''
    for i in range(len(message)):
        output += chr((((ord(message[i]) - 32) + ord(key[0:len(message)][i]) - 32) % 95) + 32)
    return output

def decrypt(message, key):    
    output = ''
    for i in range(len(message)):
        output += chr((((ord(message[i]) - 32) - (ord(key[0:len(message)][i]) - 32)) % 95) + 32)
    return output

