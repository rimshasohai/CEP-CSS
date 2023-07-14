from cryptography.fernet import Fernet
import base64
import os

# Generate a new Fernet key
#key = '28bdd4a228c935a9791ba9d85a3aa857'
#key= 'a7489f3e6b1f9279e5756ba449ed147d7ee545e250e1b21c38ad96e3243e32f1'

# Encode the key to URL-safe base64 format
encoded = base64.b64encode(b'28bdd4a228c935a9791ba9d85a3aa857')
print(encoded)

my_fernet = Fernet(encoded)
#print(my_fernet)

message = "this is the secret message".encode()
print('Plain Text',message)

# Plain Text
encrypted = my_fernet.encrypt(message)


#Use object of Fernet Key to encrypt the message
print('Cipher Text',encrypted)

#Use object of Fernet Key to encrypt the message
# If message is decrypted correctly that means we found the right key
decrypted_encrypted = my_fernet.decrypt(encrypted)
print('Decrypted Text',decrypted_encrypted)

