from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
privKeyPEM = keyPair.exportKey()
pubKeyPEM = pubKey.exportKey()

print(pubKeyPEM.decode('utf8'))
print(privKeyPEM.decode('utf8'))

