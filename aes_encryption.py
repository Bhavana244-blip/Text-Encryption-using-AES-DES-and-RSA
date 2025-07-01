from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text)%16!=0:
        text +=' '
    return text
#the above function is used to divide the text into 16 bytes as
#AES works on 16 byte blocks

key=get_random_bytes(16)
#the above line generates a random key of 16 bytes

cipher=AES.new(key,AES.MODE_ECB)
#this creates a new AES cipher object

def encrypt_aes(data):
    data=pad(data)
    encrypted=cipher.encrypt(data.encode())
    return base64.b64encode(encrypted).decode(),key
#the above function encrypts the data using AES encryption

def decrypt_aes(enc_data,key):
    cipher=AES.new(key,AES.MODE_ECB)
    decrypted=cipher.decrypt(base64.b64decode(enc_data))
    return decrypted.decode().strip()
