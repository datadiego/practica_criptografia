from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

public_key_aux=open("../clave-rsa-oaep-publ.pem").read()
private_key_aux=open("../clave-rsa-oaep-priv.pem").read()

public_key = RSA.import_key(public_key_aux)
private_key = RSA.import_key(private_key_aux)

print(public_key)
print(private_key)

def import_keys(public_key_path, private_key_path):
    public_key_aux=open(public_key_path).read()
    private_key_aux=open(private_key_path).read()

    public_key = RSA.import_key(public_key_aux)
    private_key = RSA.import_key(private_key_aux)
    keyPair = RSA.construct((public_key.n, public_key.e, private_key.d))
    return (public_key, private_key, keyPair)