# sha256 hashing with salt and pepper

import hashlib
from Crypto.Random import get_random_bytes

mensaje = "Hola mundo"
# genera salt y pepper aleatorios

salt = get_random_bytes(16)
pepper = get_random_bytes(16)

# genera el hash con salt y pepper

m = hashlib.sha256()
m.update(salt)
m.update(mensaje.encode())
m.update(pepper)
hash = m.digest()
print("Mensaje:", mensaje)
print("Salt:", salt)
print("Pepper:", pepper)
print("Hash con salt y pepper:", hash.hex())

