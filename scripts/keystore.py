import jks
import os

# Obteniendo el path
path = os.path.dirname(__file__)
keystore = path + "/../KeyStorePracticas"

ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    print(sk.alias, ":", sk.key.hex())
