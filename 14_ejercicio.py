#hash SHA-512
#cifrado-sim-aes-256 en la keystore
#dispositivo e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3

from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets

salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
master_key=bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
key1, key2 = HKDF(master_key, 32, salt, SHA512, 2)

print("Clave key1: ", key1.hex())
print("Clave key2: ", key2.hex())