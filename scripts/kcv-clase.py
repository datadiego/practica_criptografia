import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#Cifrado
textoPlano_bytes = bytes.fromhex('00000000000000000000000000000000')

clave = bytes.fromhex('979DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
print("KCV AES:", texto_cifrado_bytes.hex()[0:6])
print("texto_cifrado con padding: ", texto_cifrado_bytes.hex())

#cipher2 = AES.new(clave, AES.MODE_CBC,iv_bytes)
#texto_cifrado_bytes = cipher2.encrypt(textoPlano_bytes)
#print("KCV AES:", texto_cifrado_bytes.hex()[0:6])
#print("texto_cifrado sin padding: ", texto_cifrado_bytes.hex())

m = hashlib.sha256()
m.update(bytes.fromhex("979DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120"))
print("KCV SHA256: " + m.digest().hex()[0:6])