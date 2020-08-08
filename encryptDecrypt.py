#!python3

import csv, os, shutil
from cryptography.fernet import Fernet


def decryptFile(fernet, rootPass, passFile):
    with open(passFile, 'rb') as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    decoded = decrypted.decode("utf-8")

    #change csv data to dictionary
    reader = csv.reader(decoded.split('\n'), delimiter=',')
    fileData = {}
    for row in reader:
        if len(row)>1:
            fileData[row[0]] = row[1], row[2], row[3]
    return(fileData)


def writeFile(fileData):
    outputFile = open('passFile.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)

    with open('passFile.csv', 'w') as f:
        outputWriter = csv.writer(f)
        for key in sorted (fileData.keys()):
            outputWriter.writerow([key, fileData.get(key)[0], fileData.get(key)[1], fileData.get(key)[2]])


def encryptFile(fernet, passFile):
    with open('passFile.csv', 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(passFile, 'wb') as f:
        f.write(encrypted)
    
    os.remove('passFile.csv')
    