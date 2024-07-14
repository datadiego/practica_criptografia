from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

mensaje="b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b4970186502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01dee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee"

def import_keys(public_key_path, private_key_path):
    public_key_aux=open(public_key_path).read()
    private_key_aux=open(private_key_path).read()

    public_key = RSA.import_key(public_key_aux)
    private_key = RSA.import_key(private_key_aux)
    key_pair = RSA.construct((public_key.n, public_key.e, private_key.d))
    return (public_key, private_key, key_pair)

def descifrar(mensaje, key_pair):
    mensaje_bytes = bytes.fromhex(mensaje)
    decryptor = PKCS1_OAEP.new(key_pair,SHA256)
    decrypted = decryptor.decrypt(mensaje_bytes)
    return decrypted
# TODO: Conseguimos importar las claves, pero no conseguimos descifrar ni crear un par de claves a partir de la clave privada.


# cifrar de nuevo hex con rsa usando la clave publica

def cifrar(mensaje, public_key):
    mensaje_bytes = bytes.fromhex(mensaje)
    encryptor = PKCS1_OAEP.new(public_key,SHA256)
    encrypted = encryptor.encrypt(mensaje_bytes)
    return encrypted

public_key, private_key, key_pair = import_keys("clave-rsa-oaep-publ.pem", "clave-rsa-oaep-priv.pem")

mensaje_descifrado_bytes = descifrar(mensaje, key_pair)
mensaje_hex = mensaje_descifrado_bytes.hex()
print("Mensaje cifrado:", mensaje, len(mensaje))
print("Clave privada:", private_key)
print("Clave pública:", public_key)
print("Mensaje descifrado:", mensaje_hex)
print("-------")

mensaje_cifrado_bytes = cifrar(mensaje_hex, public_key)

print("Mensaje cifrado de nuevo:", mensaje_cifrado_bytes.hex(), len(mensaje_cifrado_bytes.hex()))