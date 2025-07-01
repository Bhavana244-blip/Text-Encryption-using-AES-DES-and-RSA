from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text)%8!=0:
        text +=' '
    return text
#the above function is used to divide the text into 8 bytes as
#DES works on 8 byte blocks

key=get_random_bytes(8)
#the above line generates a random key of 8 bytes

cipher=DES.new(key, DES.MODE_ECB)
#this creates a new DES cipher object

def encrypt_des(data):
    data=pad(data)
    encrypted=cipher.encrypt(data.encode())
    return base64.b64encode(encrypted).decode(),key
#the above function encrypts the data using DES encryption

def decrypt_des(enc_data,key):
    cipher=DES.new(key,DES.MODE_ECB)
    decrypted=cipher.decrypt(base64.b64decode(enc_data))
    return decrypted.decode().strip()
