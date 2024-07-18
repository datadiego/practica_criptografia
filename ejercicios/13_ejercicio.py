from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
#from Crypto.PublicKey import Ed25519
from Crypto.Hash import SHA256
import os

# Cargar las llaves RSA
from Crypto.PublicKey import RSA

rsa_pubKey = RSA.import_key(open("clave-rsa-oaep-publ.pem", "rb").read())
rsa_privKeyPEM = RSA.import_key(open("clave-rsa-oaep-priv.pem", "rb").read())
mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
mensaje_bytes = mensaje.encode("utf-8")
print("Clave RSA pública:", rsa_pubKey)
print("Clave RSA privada:", rsa_privKeyPEM)
print("Mensaje: ", mensaje)
print("Mensaje en bytes: ", mensaje_bytes)

hash = SHA256.new(mensaje_bytes)
signer = pkcs1_15.new(rsa_privKeyPEM)
signature = signer.sign(hash)
print("Firma:", signature.hex())

print("----")

# Cargar las llaves Ed25519

#ed25519_pubKey = Ed25519.import_key(open("clave-ed25519-publ.pem", "rb").read())
#ed25519_privKey = Ed25519.import_key(open("clave-ed25519-priv.pem", "rb").read())
#print("Clave Ed25519 pública:", ed25519_pubKey)

#hash = SHA256.new(mensaje_bytes)
#signer = pkcs1_15.new(ed25519_privKey)
#signature = signer.sign(hash)
#print("Firma:", signature)
#print("----")
