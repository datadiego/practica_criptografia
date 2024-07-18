from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

#Datos de entrada

clave = 'c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca' # debe ser de 256 bits o 128 bits
nonce = 'fbdbffb77f5966b2' # deberia ser aleatorio
mensaje_cifrado = '7b195152b8917611e8d2e2c8118a42c50d4ded1d582ba0a0c8d79265131f6c87b58a201625ab785fa2c7f02b8828abc312ad6f8737fbb5ab861adcc78106e180d935b6e43c96b503' # resultado de decode.py
print('Clave:', clave)
print('Nonce:', nonce)

# Conversiones

clave_bytes = bytes.fromhex(clave)
nonce_bytes = bytes.fromhex(nonce)
mensaje_cifrado=bytes.fromhex("7b195152b8917611e8d2e2c8118a42c50d4ded1d582ba0a0c8d79265131f6c87b58a201625ab785fa2c7f02b8828abc312ad6f8737fbb5ab861adcc78106e180d935b6e43c96b503")

# Descifrado

decipher = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
plaintext = decipher.decrypt(mensaje_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))
