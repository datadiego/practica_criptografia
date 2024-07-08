from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

# Datos
mensaje = 'KeepCoding te enseña a codificar y a cifrar'
clave = 'AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120'
nonce = '9Yccn/f5nJJhAt2S'
print('Mensaje:', mensaje)
print('Clave:', clave)
print('Nonce:', nonce)

# Conversiones

mensaje_bytes = bytes(mensaje, 'UTF-8')
clave_bytes = bytes.fromhex(clave)
nonce_bytes = b64decode(nonce)
cipher = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
texto_cifrado = cipher.encrypt(mensaje_bytes)
print('Mensaje cifrado: ', texto_cifrado.hex())
print("--------")

# Descifrado

mensaje_cifrado_hex = texto_cifrado.hex()
print('Clave:', clave)
print('Nonce:', nonce)

# Conversiones

mensaje_cifrado=bytes.fromhex(mensaje_cifrado_hex)

# Descifrado

decipher = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
plaintext = decipher.decrypt(mensaje_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))
