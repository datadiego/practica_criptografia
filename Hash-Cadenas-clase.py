import hashlib
from Crypto.Hash import keccak

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

m = hashlib.sha1()
m.update(bytes("Hola", "utf8"))
print("SHA1:   " + m.digest().hex())

m = hashlib.sha256()
m.update(bytes("Hola", "utf8"))
print("SHA256: " + m.digest().hex())

m = hashlib.sha512()
m.update(bytes("Hola", "utf8"))
print("SHA512: " + m.digest().hex())

m = hashlib.sha3_256()
m.update(bytes("Espero que todos aprendais criptografía", "utf8"))
print("SHA3-256: " + m.digest().hex())


texto_hashear = bytes("Hola","UTF-8")
hash_keccak = keccak.new(digest_bits=256)
hash_keccak.update(texto_hashear)

print ("El hash Keccak es: ", hash_keccak.hexdigest())
