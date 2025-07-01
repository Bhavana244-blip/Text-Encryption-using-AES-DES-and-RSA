from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key=RSA.generate(2048)
# Generate a new RSA key pair
private_key = key.export_key()
# Save the private key
public_key = key.publickey().export_key()
# Save the public key
def encrypt_rsa(data,public_key):
    rsa_key = RSA.import_key(public_key)
    # Import the public key
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted).decode()
# Encrypt the data using RSA
def decrypt_rsa(enc_data,private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(base64.b64decode(enc_data))
    return decrypted.decode()

def get_keys():
    return public_key, private_key