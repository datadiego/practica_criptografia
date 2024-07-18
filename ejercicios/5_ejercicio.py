import hashlib

mensaje0 = hashlib.sha3_224()
mensaje1 = hashlib.sha3_256()
mensaje2 = hashlib.sha3_384()
mensaje3 = hashlib.sha3_512()

mensaje = "En KeepCoding aprendemos cómo protegernos con criptografía"
# providing the input to the hashing algorithm.
mensaje0.update(bytes(mensaje,"UTF-8"))
mensaje1.update(bytes(mensaje,"UTF-8"))
mensaje2.update(bytes(mensaje,"UTF-8"))
mensaje3.update(bytes(mensaje,"UTF-8"))
print("Mensaje: " + mensaje)
print(mensaje0.name, mensaje0.digest_size, mensaje0.hexdigest())
print(mensaje1.name, mensaje1.digest_size, mensaje1.hexdigest())
print(mensaje2.name, mensaje2.digest_size, mensaje2.hexdigest())
print(mensaje3.name, mensaje3.digest_size, mensaje3.hexdigest())

mensaje_sha224 = hashlib.sha224()
mensaje_sha256 = hashlib.sha256()
mensaje_sha384 = hashlib.sha384()
mensaje_sha512 = hashlib.sha512()

mensaje = "En KeepCoding aprendemos cómo protegernos con criptografía"
# providing the input to the hashing algorithm.
mensaje_sha224.update(bytes(mensaje,"UTF-8"))
mensaje_sha256.update(bytes(mensaje,"UTF-8"))
mensaje_sha384.update(bytes(mensaje,"UTF-8"))
mensaje_sha512.update(bytes(mensaje,"UTF-8"))
print("------")
print("Mensaje: " + mensaje)
print(mensaje_sha224.name, mensaje_sha224.digest_size, mensaje_sha224.hexdigest())
print(mensaje_sha256.name, mensaje_sha256.digest_size, mensaje_sha256.hexdigest())
print(mensaje_sha384.name, mensaje_sha384.digest_size, mensaje_sha384.hexdigest())
print(mensaje_sha512.name, mensaje_sha512.digest_size, mensaje_sha512.hexdigest())

mensaje_aux = "En KeepCoding aprendemos cómo protegernos con criptografía."
print("------")
#convertir a sha3-256

mensaje_sha3_256_aux = hashlib.sha3_256()
mensaje_sha3_256_aux.update(bytes(mensaje_aux,"UTF-8"))
print("Mensaje: " + mensaje_aux)
print(mensaje_sha3_256_aux.name, mensaje_sha3_256_aux.digest_size, mensaje_sha3_256_aux.hexdigest())
print("\nMensaje: " + mensaje)
print(mensaje1.name, mensaje1.digest_size, mensaje1.hexdigest())
