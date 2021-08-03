#python version 3.9.5
#Caesar Cipher encoding

def ROTATE(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    new_data = ''
    for c in data:
        # Shift character
        index = alphabet.find(c)
        if index == -1:
            # Character not found
            new_data += c
        else:
            # Shift it based on key and mode
            new_index = index + key if mode == 1 else index - key
            new_index %= len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    # Return the ciphered text
    print (new_data)

userInput = input("enter data to encode: ")
userInput = userInput.lower()
ROT = int(input("How many rotations to use i.e 3 "))
mode = 1
ROTATE(userInput, ROT, mode)
