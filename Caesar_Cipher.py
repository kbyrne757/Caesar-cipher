#python version 3.9.5
#Caesar Cipher encoding

import string
from time import sleep

alphabet = string.ascii_lowercase


def encrypt():
    decrypted_message = input("Enter the message you would like to encrypt: ").strip()
    key = int(input("Enter key to encrypt: "))

    encrypted_message = ""

    for c in decrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c


    print(encrypted_message)


def decrypt():
    
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print(decrypted_message)




choice = input("Would you like to encrypt or decrypt? ")
choice = choice.lower()

if choice == "encrypt":
    encrypt()

elif choice == "decrypt":
    decrypt()

else:
    print("Invalid Input")

