# encripta el objeto usando AES GCM

# Importamos las librerías necesarias
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Datos

req = {
    "idUsuario": 1,
    "usuario": "Jose Manuel Barrio Barrio",
    "tarjeta": 123456789
}

res = { 
 "idUsuario": 1, 
 "movTarjeta": [{ 
  "id": 1, 
  "comercio": "Comercio Juan", 
  "importe": 5000 
 }, { 
  "id": 2, 
  "comercio": "Rest Paquito", 
  "importe": 6000 
 }], 
 "Moneda": "EUR", 
 "Saldo": 23400 
}

# random clave

clave = get_random_bytes(16)

# IVs

iv_req = get_random_bytes(16)
iv_res = get_random_bytes(16)

# Cifrado

cipher_req = AES.new(clave, AES.MODE_CBC, iv_req)
cipher_res = AES.new(clave, AES.MODE_CBC, iv_res)

# Cifrado de los objetos

req_cifrado = cipher_req.encrypt(pad(str(req).encode(), AES.block_size, style='pkcs7'))
res_cifrado = cipher_res.encrypt(pad(str(res).encode(), AES.block_size, style='pkcs7'))

# Mostramos los datos cifrados

print("Clave:", clave.hex())
print("IV Request:", iv_req.hex())
print("IV Response:", iv_res.hex())
print("Request original:", req)
print("Request cifrado:", req_cifrado.hex())

print("Response original:", res)
print("Response cifrado:", res_cifrado.hex())

