#!python3

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

#verify key from given password
def keyVerify(rootPass, passFile):
    key = keyGen(rootPass)
    with open(passFile, 'rb') as f:
        data = f.read()
    try:
        Fernet(key).decrypt(data)
        return Fernet(key)
    except:
        return False

def keyGen(rootPass):
    password = rootPass.encode()
    salt = b'\xb5\xc1g\xcbC\x18\xd3\xd9\x97*\x87\x95\x81vp\xf9'
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100_000,
        backend = default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key
    