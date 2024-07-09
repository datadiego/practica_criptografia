import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


plaintext_bytes = bytes("Esto parece que va acabando....","UTF-8")
clave_bytes = bytes.fromhex('c936108299307d3f6f7585b96013346d')
nonce = bytes.fromhex('47e6831df094b7a6') # 16 bytes para AES

datos_asociados_bytes = bytes("id=1","UTF-8")
cipher = AES.new(clave_bytes, AES.MODE_GCM,nonce=nonce)

cipher.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(plaintext_bytes)

print("CipherText: ", texto_cifrado_bytes.hex())
print("Tag:", tag.hex())

try:
    tag_desc_bytes = bytes.fromhex("441471ad16a6023bf67e0ab2223c5f26")
    datos_asociados_desc_bytes = bytes("id=1","UTF-8")
    texto_cifrado_bytes= bytes.fromhex("1978566d9c99ea31a4e525a4d136aa6b26bda2b0ae3898ab90aa5d296eb3ff")
    cipher = AES.new(clave_bytes, AES.MODE_GCM, nonce=nonce)
    cipher.update(datos_asociados_desc_bytes)
    mensaje_des_bytes = cipher.decrypt_and_verify(texto_cifrado_bytes,tag_desc_bytes)
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 