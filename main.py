# Program for encrypt strings

import random
import string

chars = "  " + string.punctuation + \
    string.digits + string.ascii_letters  # adding caracter strings and spaces
chars = list(chars)  # Converting chars in a list
key = chars.copy()  # Create Copu for the list


random.shuffle(key)  # Shuffle the caracters with a diferent caracter

# print(f"chars: {{chars}}")
# print(f"key  : {{key}}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = " "

#
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original  message : {plain_text}")
print(f"encrypted message : {cipher_text}")


# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = " "

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message : {cipher_text}")
print(f"Original  message : {plain_text}")
