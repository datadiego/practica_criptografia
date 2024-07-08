import base64
mensaje = bytes("Hola", "utf-8") # bytes
mensaje_b64 = base64.b64encode(mensaje) # bytes
mensaje_b64_str = mensaje_b64.decode("utf-8") # str
mensaje_hex = mensaje.hex() # str
