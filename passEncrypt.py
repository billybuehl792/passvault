#!python
# passwordVault - secure store passwords

import base64
import os
import csv
import time
from passwordmeter import test
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

#keygen
while True:
    root_pass = input('Enter Password for file: ')
    if test(root_pass)[0] > .9:
        print('password secure (>.9)')
        option = input('use pass?(y/n): ')
        if option == 'y':
            break
        break
    elif test(root_pass)[0] > .8:
        print('password relatively secure (>.8)')
        option = input('use pass?(y/n): ')
        if option == 'y':
            break
    else:
        print('password insecure.')

password = root_pass.encode()
salt = b'\xb5\xc1g\xcbC\x18\xd3\xd9\x97*\x87\x95\x81vp\xf9'
kdf = PBKDF2HMAC(
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations = 100_000,
    backend = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

print(str(key))

#createFile
outputFile = open('passFile.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

print('type x to finish.')
while True:
    site = input('Enter site: ')
    if site == 'x':
        break
    user = input('Enter username: ')
    if user == 'x':
        break
    passwd = input('Enter pass: ')
    if passwd == 'x':
        break
    email = input('Enter email: ')
    if email == 'x':
        break
    outputWriter.writerow([site, user, passwd, email])

outputFile.close()

#loadFile/read Data/ delete File
with open('passFile.csv', 'rb') as f:
    data = f.read()
os.remove('passFile.csv')
print('passFile.csv removed')

#encrypt with key
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#write encrypted to new file
with open('passFile.csv.encrypted', 'wb') as f:
    f.write(encrypted)

os.system('clear')
os.system('clear')
