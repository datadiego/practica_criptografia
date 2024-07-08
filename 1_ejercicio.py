print("Ejercicio 1")
print("--------")
print("Datos conocidos:")
clave_fija=0xB1EF2ACFE2BAEEFF
clave_memoria=0x91BA13BA21AABB12
valor_keymanager=(hex(clave_fija^clave_memoria))
print("memoria: ", hex(clave_memoria))
print("fija: ", hex(clave_fija))
print("keymanager = clave_memoria ⊕ clave_fija: ", valor_keymanager)

print("\nMientras conozcamos dos de las tres claves, podemos obtener la tercera gracias a la propiedad conmutativa de la operación XOR.", "\n")
print("Datos conocidos (caso contrario):")
clave_fija=0xB1EF2ACFE2BAEEFF
clave_keymanager=0x20553975c31055ed
clave_memoria=(hex(clave_fija^clave_keymanager))
print("keymanager: ", hex(clave_keymanager))
print("fija: ", hex(clave_fija))
print("memoria = clave_keymanager ⊕ clave_fija: ", clave_memoria)

print("--------")

print("Datos conocidos:")
clave_fija=0xB1EF2ACFE2BAEEFF
clave_memoria=0xB98A15BA31AEBB3F
valor_keymanager=(hex(clave_fija^clave_memoria))
print("memoria: ", hex(clave_memoria))
print("fija: ", hex(clave_fija))
print("keymanager = clave_memoria ⊕ clave_fija: ", valor_keymanager)