#!python3

import secrets, string
from passwordmeter import test
import requests
from os.path import isfile
import random
import colors


def passGen():
    wordFile = 'wordFile.txt'
    words = open(wordFile).read().split('\n')
    specialChars = r'!?_@$#'
    
    while True:
        passwd = ''
        for _ in range(2):
            passwd += secrets.choice(words).lower().capitalize()
        for _ in range(random.randint(1, 6)):
            passwd += secrets.choice(string.digits)
        for _ in range(1):
            passwd += secrets.choice(specialChars)

        if test(passwd)[0] > .9:
            return(passwd, test(passwd)[0])
        else:
            continue


def userPass(site):
    while True:
        passwd = input('{}Enter password for{} {}: '.format(colors.bcolors.BOLD, colors.bcolors.ENDC, site))
        testResult = test(passwd)[0]
        if testResult > .9:
            print('{}password security: {} | secure password.{}'.format(colors.bcolors.GREEN, testResult, colors.bcolors.ENDC))
        elif testResult > .8:
            print('{}password security: {} | password relatively secure.{}'.format(colors.bcolors.BLUE, testResult, colors.bcolors.ENDC))
        else:
            print('{}password security: {} | password insecure.\n{}'.format(colors.bcolors.FAIL, testResult, colors.bcolors.ENDC))
        
        option = input('use password(y/n)? ')
        if option == 'y':
            print()
            break
        else:
            continue
    
    return(passwd)