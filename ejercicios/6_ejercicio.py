import os
import jks
from Crypto.Hash import HMAC, SHA256

def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result

def get_key(nombre):
    path = os.path.dirname(__file__)
    keystore = path + "/KeyStorePracticas"
    ks = jks.KeyStore.load(keystore, "123456")
    clave=""
    for alias, sk in ks.secret_keys.items():
        if sk.alias == nombre:
            clave = sk.key.hex()
    return clave

# Datos
clave = get_key("hmac-sha256")
datos = "Siempre existe más de una forma de hacerlo, y más de una solución válida."

print("Clave:", clave)
print("Datos:", datos)

# Conversiones
clave_bytes = bytes.fromhex(clave)
datos_bytes = bytes(datos, 'utf-8')

# HMAC
hmac = getHMAC(clave_bytes, datos_bytes)
validacion = validateHMAC(clave_bytes, datos_bytes, hmac)

# Validación
print("HMAC", hmac)
print("Validación:", validacion)