from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#Datos de entrada
mensaje_cifrado="518ccb2dd2a66c632b366c661da53f529165dfd44f833fe9ddec21a8bc2407df"
iv = "47e6831df094b7a6c0ef1fbe0da96ad3"
clave="c936108299307d3f6f7585b96013346d"

#Descifrado
try:
    iv_bytes = bytes.fromhex(iv)
    texto_cifrado_bytes = bytes.fromhex(mensaje_cifrado)
    clave = bytes.fromhex(clave)
    cipher = AES.new(clave, AES.MODE_CBC, iv_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 