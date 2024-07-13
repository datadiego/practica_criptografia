import jks
import os

path = os.path.dirname(__file__)
keystore = path + "/KeyStorePracticas"

ks = jks.KeyStore.load(keystore, "123456")
clave=""
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave = sk.key.hex()

def get_key(nombre):
    path = os.path.dirname(__file__)
    keystore = path + "/KeyStorePracticas"
    ks = jks.KeyStore.load(keystore, "123456")
    clave=""
    for alias, sk in ks.secret_keys.items():
        if sk.alias == nombre:
            clave = sk.key.hex()
    return clave