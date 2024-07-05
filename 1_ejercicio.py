clave_fija=0xB1EF2ACFE2BAEEFF
clave_memoria=0x91BA13BA21AABB12
valor_keymanager=(hex(clave_fija^clave_memoria))
print("keymanager: ", valor_keymanager)
print("memoria: ", hex(clave_memoria))
print("fija: ", hex(clave_fija))

print("--------")

clave_fija=0xB1EF2ACFE2BAEEFF
clave_keymanager=0x20553975c31055ed
clave_memoria=(hex(clave_fija^clave_keymanager))
print("keymanager: ", hex(clave_keymanager))
print("memoria: ", clave_memoria)
print("fija: ", hex(clave_fija))