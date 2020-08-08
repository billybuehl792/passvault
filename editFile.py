#!python3

import passGen, csv, encryptDecrypt, colors
import os, pyperclip

def getPass(fileData):
    print('\n\'{}x{}\' to exit.\n'.format(colors.bcolors.FAIL, colors.bcolors.ENDC))
    while True:
        site = input('\n{}Enter site: {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC))
        if site == 'x':
            break
        try:
            print('{}Username:{}   {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC, fileData[site][0]))
            print('{}Password:{}   {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC, fileData[site][1]))
            print('{}Email:{}      {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC, fileData[site][2]))
            pyperclip.copy(fileData[site][1])
            print('(password copied to clipboard)')
        except KeyError:
            print(colors.bcolors.WARNING + 'Invalid Key: Enter legitimate site.' + colors.bcolors.ENDC)

def delPass(fileData):
    print('\n\'{}x{}\' to exit.\n'.format(colors.bcolors.FAIL, colors.bcolors.ENDC))
    while True:
        site = input('Enter Site name: ')
        if site == 'x':
            break
        try:
            del fileData[site]
            print(colors.bcolors.FAIL + site + ' deleted.\n' + colors.bcolors.ENDC)
        except KeyError:
            print(colors.bcolors.WARNING + site + ' not in passFile.\n' + colors.bcolors.ENDC)
    
    return(fileData)

def appendPass(fileData):
    print('\n\'{}x{}\' to exit.\n'.format(colors.bcolors.FAIL, colors.bcolors.ENDC))
    while True:
        site = input('{}Enter Site name:{} '.format(colors.bcolors.BOLD, colors.bcolors.ENDC))
        if site == 'x':
            break
        username = input('{}Enter Username:{} '.format(colors.bcolors.BOLD, colors.bcolors.ENDC))
        if site in fileData.keys():
            site += '({})'.format(username)
        
        option = input('user pass(u) or generate pass(g)? ')
        if option == 'u':
            password = passGen.userPass(site)
        else:
            while True:
                passBuild = passGen.passGen()
                print('{}Generated Password:{} {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC, passBuild[0]))
                print('{}Password Strength:{}  {}'.format(colors.bcolors.BOLD, colors.bcolors.ENDC, passBuild[1]))
                userResponse = input('use pass(y/n)?')
                if userResponse == 'y':
                    password = passBuild[0]
                    break
                else:
                    continue

        email = input('{}Enter Email:{} '.format(colors.bcolors.BOLD, colors.bcolors.ENDC))
        print(colors.bcolors.GREEN + site + ' added to passFile.\n' + colors.bcolors.ENDC)
        fileData[site] = username, password, email

    return(fileData)
    