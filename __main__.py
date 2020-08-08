#! python3

import keyVerify, encryptDecrypt, editFile, passGen, colors
import getpass
from os.path import isfile
import sys, os
import time


#get passfile
def main():
    passFile = 'passFile.csv.encrypted'
    if isfile(passFile):
        passFile = passFile
    else:
        while not isfile(passFile):
            passFile = input('Enter Password File: ')


    # access to file
    while True:
        rootPass = getpass.getpass('Enter Password: ')
        if not keyVerify.keyVerify(rootPass, passFile):
            print('Incorrect Password')
        else:
            fernet = keyVerify.keyVerify(rootPass, passFile)
            break

    # decrypt/ decode File
    fileData = encryptDecrypt.decryptFile(fernet, rootPass, passFile)

    # mainloop
    while True:
        os.system('clear')

        # print available sites
        print('\n' + colors.bcolors.UNDERLINE + 'Available Sites:' + colors.bcolors.ENDC)
        for site in fileData.keys():
            print(colors.bcolors.GREEN + site + colors.bcolors.ENDC)

        # menu
        print(colors.bcolors.BLUE + '\n(p) View Passwords, (d) Delete Password, (a) Append Password, (x) Exit' + colors.bcolors.ENDC)
        userResponse = input('Response: ')

        # get pass
        if userResponse == 'p':
            editFile.getPass(fileData)

        # append pass   
        elif userResponse == 'a':
            fileData = editFile.appendPass(fileData)
            encryptDecrypt.writeFile(fileData)
            encryptDecrypt.encryptFile(fernet, passFile)

        # delete Pass    
        elif userResponse == 'd':
            fileData = editFile.delPass(fileData)
            encryptDecrypt.writeFile(fileData)
            encryptDecrypt.encryptFile(fernet, passFile)

        # quit    
        elif (userResponse == 'x') or (userResponse == ''):
            break
        else:
            print('Enter Legitimate key.')
            time.sleep(.5)

    print('\ndone.')
    os.system('clear')
    os.system('clear')

if __name__ == '__main__':
    main()
