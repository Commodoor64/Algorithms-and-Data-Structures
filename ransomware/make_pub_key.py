from Crypto.PublicKey import RSA
key = RSA.generate(2048)

public_key = key.public_key().export_key()
with open('public.pem','wb') as f:
    f.write(public_key)
    