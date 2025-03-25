import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(master_pwd):
    """Derive a key from the master password."""
    salt = b'\x08\xe2v\xf3Jp\xc1\x14'  # Use a fixed salt (change per user ideally)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))

master_pwd = input("What is the master password? ")
key = derive_key(master_pwd)
fer = Fernet(key)

def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                user, passw = line.rstrip().split("|")
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print(f"User: {user}, Password: {decrypted_pass}")
    except Exception as e:
        print("Error:", e)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open("password.txt", "a") as f:
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing one (view, add)? Press Q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
