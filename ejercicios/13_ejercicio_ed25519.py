import ed25519
from Crypto.Hash import SHA256

privatekey = open("ed25519-priv","rb").read()
publickey = open("ed25519-publ","rb").read()
signedKey = ed25519.SigningKey(privatekey)

msg = bytes('Somos los mejores','utf8')

hash=SHA256.new(msg)
signature = signedKey.sign(bytes.fromhex(hash.hexdigest()), encoding='hex')

print("Mensaje:", msg)
print("Hash SHA256:", hash.hexdigest())
print("Clave publica:", publickey.hex())
print("Clave privada:", privatekey.hex())
print("Firma Generada (64 bytes):", signature)

print("-----")
try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, bytes.fromhex(hash.hexdigest()), encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
