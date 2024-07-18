# pedro manda a raul el siguiente mensaje:

mensaje = "Se debe ascender inmediaamente a Raúl. Es necesario mejorarle sus condiciones económicas un 20% para que se quede con nosotros."

# adjunto tenemos los siguientes archivos

firma = "MensajeRespoDeRaulARRHH.txt.sig"

# en RRHH tenemos las claves para verificar la firma

clave_privada = "Pedro-priv.txt"
clave_publica = "Raul-pub.txt"

# las claves de los ficheros de RRGG son RRHH-priv-txt y RRHH-publ.txt 

clave_RRHH = "RRHH-priv.txt"
clave_RRGG = "RRHH-publ.txt"

## firmar esto como RRHH
mensaje_para_firmar="Viendo su perfil en el mercado, hemos decidido ascenderle y mejorarle un 25 su salario. Saludos."

# firmar con la clave publica de RRGG como la de Pedro

mensaje_para_firmar2="Estamos todos de acuerdo, el ascenso será el mes que viene, agosto, si no hay sorpresas."