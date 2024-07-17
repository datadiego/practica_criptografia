from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

keyPair = RSA.generate(3072) # generar un par de claves RSA de 3072 bits
pubKey = keyPair.publickey() # obtener la clave pública

privKeyPEM = RSA.import_key(keyPair.exportKey()) # obtener la clave privada

aes_key = get_random_bytes(16) # generar una clave AES de 16 bytes

print("Clave AES antes: ", aes_key.hex()) # imprimir la clave AES antes de cifrarla

cipher = PKCS1_v1_5.new(pubKey) # crear un objeto de cifrado PKCS1_v1_5 con la clave pública
ciphertext = cipher.encrypt(aes_key) # cifrar la clave AES con la clave pública
print("Clave cifrada:", ciphertext.hex()) # imprimir el texto cifrado

sentinel = get_random_bytes(16) # generar un centinela aleatorio de 16 bytes
print("Centinela:" + sentinel.hex()) # imprimir el centinela

cipher = PKCS1_v1_5.new(privKeyPEM) # crear un objeto de cifrado PKCS1_v1_5 con la clave privada
aes_key = cipher.decrypt(ciphertext,sentinel,expected_pt_len=16) # descifrar la clave AES con la clave privada
print("Clave AES despues: ", aes_key.hex()) # imprimir la clave AES después de descifrarla
