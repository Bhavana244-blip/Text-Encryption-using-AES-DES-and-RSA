# SecureTextPro - Multi Encryption Tool

## Overview

**SecureTextPro** is a Python-based command-line tool that provides secure text encryption and decryption using three major cryptographic algorithms: AES, DES, and RSA.  
This multi-encryption utility allows users to choose their preferred method for safeguarding sensitive information, demonstrating practical implementations of symmetric and asymmetric encryption techniques.

## Features

- **AES Encryption & Decryption**  
  Advanced Encryption Standard (AES) for fast, secure symmetric key encryption.

- **DES Encryption & Decryption**  
  Data Encryption Standard (DES) as a classical symmetric encryption method.

- **RSA Encryption & Decryption**  
  Rivest–Shamir–Adleman (RSA) for secure asymmetric encryption using public/private key pairs.

- Interactive command-line interface for easy encryption and decryption.

## Technologies Used

- Python 3.x  
- `pycryptodome` for cryptographic primitives  
- Modular codebase with separate modules for AES, DES, and RSA algorithms.

## Getting Started

### Prerequisites

Install Python 3 if not already installed.  
Install required dependencies:
pip install pycryptodome


How to Run
Clone the repository:
git clone https://github.com/Bhavana244-blip/Text-Encryption-using-AES-DES-and-RSA.git
cd Text-Encryption-using-AES-DES-and-RSA

Run the main program:
python main.py

Follow the on-screen prompts:

Enter the text you want to encrypt.

Choose encryption method: AES, DES, or RSA.

The program will display the encrypted text and the key (or private key in RSA).

It will also decrypt the text immediately to demonstrate correctness.

### Project Structure
├── aes_encryption.py       # AES encryption and decryption functions
├── des_encryption.py       # DES encryption and decryption functions
├── rsa_encryption.py       # RSA key generation, encryption, and decryption
├── main.py                 # Main CLI program to interact with all algorithms
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

### Security Notes
Keep encryption keys and private keys confidential.

This project is intended for educational purposes.

For production systems, use proper secure key management and cryptographic best practices.

### Contributing
Feel free to contribute by submitting issues or pull requests for enhancements and bug fixes.
