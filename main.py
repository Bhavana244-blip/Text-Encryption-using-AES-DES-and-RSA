from aes_encryption import encrypt_aes, decrypt_aes
from des_encryption import encrypt_des, decrypt_des
from rsa_encryption import encrypt_rsa, decrypt_rsa, get_keys

def main():
    print("\n SecureTextPro - Multi Encryption \n")
    text = input("Enter the text to encrypt: ")

    print("\nChoose Encryption Method:")
    print("1. AES")
    print("2. DES")
    print("3. RSA")

    choice = input("\nYour choice (1/2/3): ")

    if choice == '1':
        enc, key = encrypt_aes(text)
        print(f"\n Encrypted (AES): {enc}")
        print(f" AES Key (Keep it safe!): {key.hex()}")
        dec = decrypt_aes(enc, key)
        print(f" Decrypted: {dec}")

    elif choice == '2':
        enc, key = encrypt_des(text)
        print(f"\n Encrypted (DES): {enc}")
        print(f" DES Key (Keep it safe!): {key.hex()}")
        dec = decrypt_des(enc, key)
        print(f" Decrypted: {dec}")

    elif choice == '3':
        pub, priv = get_keys()
        enc = encrypt_rsa(text, pub)
        print(f"\n Encrypted (RSA): {enc}")
        print(f" Private Key (Keep it secret!):\n{priv.decode()}")
        dec = decrypt_rsa(enc, priv)
        print(f" Decrypted: {dec}")

    else:
        print(" Invalid option, try again.")

if __name__ == '__main__':
    main()