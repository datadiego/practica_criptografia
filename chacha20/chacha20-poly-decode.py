from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

# Datos de entrada

nonce="PwJVHN2bwiwYaFUg"
datos_asociados="RGF0b3Mgbm8gY2lmcmFkb3Mgc8OzbG8gYXV0ZW50aWNhZG9z"
texto_cifrado="s0i3B8WaoKIpOezrB9Ncdzn/qZYqcnrDfMsUpNqpL5u3zXmnpY+0ANhgELPrL3tLueMOig1nmz2OiXT1ayFHF8CsIinm1cWklJksanYm4RA="
tag="ESoovNYWbK0w4FWVP17DVA=="
clave="c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca"

print('Nonce:', nonce)
print('Datos asociados:', datos_asociados)
print('Texto cifrado:', texto_cifrado)
print('Tag:', tag)
print('Clave:', clave)

try:
    # Conversiones
    clave_bytes = bytes.fromhex(clave)
    datos_asociados_bytes = b64decode(datos_asociados)
    texto_cifrado_bytes = b64decode(texto_cifrado)
    tag_bytes = b64decode(tag)

    # Descifrado
    decipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=b64decode(nonce))
    decipher.update(datos_asociados_bytes)
    mensaje_descifrado = decipher.decrypt_and_verify(texto_cifrado_bytes, tag_bytes)
    print('Datos descifrados:', mensaje_descifrado.decode('utf-8'))
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)