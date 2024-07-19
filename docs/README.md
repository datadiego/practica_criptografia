# Ejercicio 1

Se han disociado dos claves, se nos da una clave fija y otra clave que se ha obtenido de la memoria. Se nos pide que obtengamos la clave original establecida por el clavero.

## Datos

memoria:  0x91ba13ba21aabb12

fija:  0xb1ef2acfe2baeeff

## Procedimiento

Para obtener la clave original, se debe realizar una operación XOR entre la clave fija y la clave obtenida de la memoria. Gracias a la propiedad conmutativa de la operación XOR, se puede obtener la clave original:

```bash
0101 XOR 1100 = 1001

0101 XOR 1001 = 1100

1100 XOR 1001 = 0101
```

keymanager = clave_memoria XOR clave_fija:  0x20553975c31055ed

![Ejercicio 1](./imgs/1.png)# Ejercicio 2

## Enunciado

Se nos pide descrifrar el mensaje cifrado con el algoritmo AES-256 en modo CBC y relleno PKCS.

## Datos

```bash
Tag en el keystore: cifrado-sim-aes-256

IV: 0000000000000000000000000000000 (16 bytes)

Clave: A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72

Cifrado: TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg
3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=

Tipo: AES/CBC/PKCS
```

## Procedimiento

En cyberchef, podemos usar la receta "AES Decrypt" con los datos, deberemos convertir el mensaje de base64 a hex o raw, podemos usar la siguiente receta:

```bash
From_Base64('A-Za-z0-9+/=',true,false)
To_Hex('Space',0)
AES_Decrypt({
    'option':'Hex',
    'string':'A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72'
    },
    {
        'option':'Hex',
        'string':'0000000000000000000000000000000'
    },
    'CBC',
    'Hex',
    'Raw',
    {
        'option':'Hex',
        'string':''
    },
    {
        'option':'Hex',
        'string':''
    })
```

Una vez cargados los datos obtenemos el mensaje.

También podemos usar python, importando la clave y el IV en hexadecimal, y el mensaje cifrado en base64, y decodificarlo:

![Ejercicio 2](./imgs/2.png)# Ejercicio 3

Se nos pide cifrar un mensaje en ChaCha20
Despues se nos pide aumentar la seguridad del cifrado autenticando el mensaje con Poly1305, esto nos permitira detectar si el mensaje ha sido modificado.

Después de cifrar el mensaje, se nos pide mejorar la seguridad del cifrado autenticando el mensaje con Poly1305, esto nos permitirá detectar si el mensaje ha sido modificado.

## Datos

```bash
Mensaje: KeepCoding te enseña a codificar y a cifrar

Clave: AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120

Nonce: 9Yccn/f5nJJhAt2S
```

## Procedimiento

En python, deberemos asegurarnos de tener los datos necesarios, el mensaje, clave y nonce, convertimos a bytes el mensaje y la clave, y ciframos el mensaje con la clave y el nonce.

Para autenticar el mensaje, deberemos usar Poly1305, deberemos generar un Nonce de 12 bytes, unos datos adicionales que servirán para autenticar el mensaje, y la clave, con estos datos, generamos un tag que servirá para autenticar el mensaje.

![Ejercicio 3](./imgs/3.png)# Ejercicio 4

Se nos da un jwt y se nos pide con que algoritmo fue firmado.
Luego se nos proporciona otro jwt, debemos decodificarlo y analizar que está intentando hacer el usuario e intentar validarlo con pyjwt.

## Datos

```bash
JWT: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9u
IFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0Ijo
xNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"
```

## Procedimiento

Podemos separar las partes del jwt usando como separador el punto. Luego decodificamos el contenido y obtenemos el algoritmo en el campo "alg" del header.

El algoritmo con el que fue firmado el jwt es HS256.

El cuerpo del jwt es:

```json
{"usuario":"Don Pepito de los palotes","rol":"isNormal","iat":1667933533}
```

Si analizamos el segundo token, podemos ver que el usuario intenta cambiar su rol a "isAdmin" para obtener más permisos.

![Ejercicio 4](./imgs/4.png)
## Ejercicio 5

Se nos da un mensaje y su salida en keccak SHA3 y SHA2 y se nos pide identificar el tipo de SHA que se utilizó. 
Tambien se nos pide convertir a SHA3 Keccak de 256 bits y analizar un mensaje con un cambio menor en el string.

### Datos

```bash
Mensaje_original: En KeepCoding aprendemos cómo protegernos con criptografía

SHA3: bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe

SHA2: 4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f29
08aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c
5351c833

Mensaje_diferente: En KeepCoding aprendemos cómo protegernos con criptografía.
```

### Procedimiento


Podemos saber el tipo de SHA3 por el largo del hash, en este caso, el hash tiene 32 bytes, por lo que se utilizó SHA3-256.

Podemos comprobarlo con la salida al convertir el mensaje:

```bash
SHA3 del ejercicio: 
bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
```

![Ejercicio 5](./imgs/5.png)

Si utilizamos SHA2:

```bash
SHA2 del ejercicio: 
4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d
63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833
```

![Ejercicio 5](./imgs/5b.png)

Podemos ver que el algoritmo utilizado fue sha512.

Si convertimos el mensaje dado y comparamos con el anterior:

![Ejercicio 5](./imgs/5c.png)

Podemos ver que el hash cambia completamente, por lo que los hashes son lo suficientemente distintos con un cambio menor.## Ejercio 6

Se nos pide calcular la HMAC del mensaje "Siempre existe más de una forma de hacerlo, y más de una solución válida" usando la clave almacenada en el keystore.

## Datos

```bash
Mensaje: Siempre existe más de una forma de hacerlo, y más de una solución válida

Clave: A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB
```

## Procedimiento

Extaemos la clave del keystore

Utilizamos la función para crear el HMAC y obtenemos y validamos el resultado:

![Ejercicio 6](./imgs/6.png)# Ejercicio 7

Se nos hacen las siguientes preguntas:

- ¿Por qué SHA-1 no es seguro?
- ¿Cómo fortalecer SHA-256 y mejorar su seguridad?

## Procedimiento

SHA-1 es vulnerable a colisiones entre hashes, con diferentes mensajes se puede generar el mismo hash, esto puede ser un problema para la integridad de los datos.

En cuanto a SHA-256, es un algoritmo más seguro que SHA-1, pero se puede mejorar su seguridad añadiendo un salt a los datos antes de cifrarlos, esto hará más difícil la generación de colisiones entre hashes.

Adicionalmente, podemos añadir un pepper a los datos antes de cifrarlos, esto añadirá una capa de seguridad adicional a los datos cifrados.

![Ejercicio 7](./imgs/7.png)# Ejercicio 8

Se nos muestra una API REST que recibe datos sensibles, como tarjetas de crédito, nombres, ids, etc.

Se nos pide buscar información sobre qué algoritmo usar para cifrar estos datos, asegurando la integridad y confidencialidad de los mismos.

Se asume que el sistema no usa TLS (https) para cifrar los datos.

## Procedimiento

Podemos usar o AES/GCM o Chacha20-poly1305 para el cifrado, los dos aseguran integridad y confidencialidad.

Si buscamos rapidez, podemos elegir Chacha20-poly1305, que es más rápido que AES/GCM.

![Ejercicio 8](./imgs/8.png)# Ejercicio 9

## Enunciado

Se nos pide calcular el KCV de una clave AES, necesitaremos el KCV(SHA-256) y el KCV(AES).

KCV(SHA-256) => primeros 3 bytes de SHA-256 de la clave

KCV(AES) => primeros 3 bytes de AES de la clave o toda??

## Datos

```bash
Clave AES: A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72

Mensaje: 00000000000000000000000000000000

IV: 00000000000000000000000000000000
```

## Procedimiento

Para obtener el KCV de la clave AES ciframos el mensaje (en este caso 16 bytes de 0) con la clave AES y el IV proporcionados. Luego obtenemos los primeros 3 bytes de la salida y los convertimos a hexadecimal.

Para obtener el KCV de la clave SHA-256, simplemente obtenemos los primeros 3 bytes de la salida de la función hash SHA-256 de la clave y los convertimos a hexadecimal.

![Ejercicio 9](./imgs/9.png)# Ejercicio 10

Se nos pide verificar la firma del fichero "MensajeRespoDeRaulARRHH.txt.sig" y evidenciar que el mensaje fue firmado por Pedro.

Además, se nos pide firmar el siguiente mensaje:

## Datos

```bash
Mensaje: Se debe ascender inmediatamente a Raúl. Es necesario 
mejorarle sus condiciones económicas un 20% para que se quede
con nosotros.

Firma pgp: MensajeRespoDRaulARRHH.txt.sig

Claves: Pedro-priv.txt y Pedro-publ.txt

Mensaje a firmar como RRHH: Viendo su perfil en el mercado, 
hemos decidido ascenderle y mejorarle un 25% su salario. Saludos.

Mensaje a cifrar con cable publica de RRHH y pedro: 
Estamos todos de acuerdo, el ascenso será el mes que viene, 
agosto, si no hay sorpresas.
```

## Procedimiento

Para verificar la firma del archivo "MensajeRespoDeRaulARRHH.txt.sig" debemos importar la clave pública de Pedro y verificar la firma del archivo:

```bash
gpg --import Pedro-publ.txt
```

![Importar clave pública de Pedro](./imgs/10.png)

Una vez importada la clave pública de Pedro, verificamos la firma del archivo "MensajeRespoDeRaulARRHH.txt.sig":

```bash
gpg --verify MensajeRespoDeRaulARRHH.txt.sig
```

![Verificar firma del archivo](./imgs/10b.png)

Para firmar el segundo mensaje como si fueramos RRHH, primero importamos la clave privada de RRHH:

```bash
gpg --import RRHH-priv.txt
```

![Importar clave privada de RRHH](./imgs/10c.png)

Necesitaremos el id de la clave privada que acabamos de importar, podemos verlas con `gpg --list-secret-keys`:

![Listar claves privadas](./imgs/10d.png)

Con el id de la clave privada de RRHH, firmamos el mensaje usando `gpg --output <archivo_salida> --sign -u <id> mensaje.txt`:


![Firmar mensaje](./imgs/10e.png)

Para cifrar el mensaje con la clave pública de RRHH y Pedro, importamos las claves publicas necesarias y comprobamos sus ids con `gpg --list-keys`:

![Listar claves públicas](./imgs/10f.png)

Con los ids de las claves públicas de RRHH y Pedro, ciframos el mensaje con `gpg --output <archivo_salida> --encrypt --recipient <id> --recipient <id> mensaje.txt`:

![Cifrar mensaje](./imgs/10g.png)

El archivo cifrado está en `ejercicios/mensaje_cifrado.gpg`:
# Ejercicio 11

Se nos da una clave rsa privada y una clave rsa pública y un mensaje cifrado en RSA OAEP mediante SHA-256.
Se nos pide descifrar el mensaje, una vez hecho, lo volvemos a descifrar y comprobamos si el cifrado es el mismo que el original.

## Datos

```bash
SHA256: b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18
283b32e1709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dff
a76a329d04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc12733038826099
57c4c0ae2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82
f5b4970186502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf
8f8e0498a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf6376808822
6e2a9177485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651
cf24b01dee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e
447cb8ee
```

Podemos hacer cat *.pem para ver el contenido de los archivos y vemos que son claves RSA.

```bash
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/absrLf79T7cz
tzjt/hHGJ+2LTBrZ90mJqVTwCtLU5xCd9helfOiVQ+ZFZH5a1ewI3Q5hPA16R/Ad
g63clqWY4iRp4JZt84GGw2XeLURQ60VNxlufQt1aC9oU0Qi1YksI1+LqNa6y5KOw
HqZFkoq+25EGkduNh9zAPevy1kVne/lfUJsxvtgjuNFN+WieCtq3M5fszjeBM2ew
5HfHPLINKr5YpYTRkU80TmrN0R0iewSmlupaAk/hSL2ADUdmzraVqLzqvJ763R79
cO+SmugoEEDEKlxK+xCE42vu9W00d9m2ZSEJgiVeV5yDCoOKzFyJnmhL6dKYFMuD
UU1K4OxtAgMBAAECggEAPqkQGoyOIsKLyKQ8QLyheOrtOmKJj70CF8yU/5ereQLD
T9KV3xjK0sJNiX3iVz4cbLJg2Lfd+Z+/HQpUShgO0cOGBBr/Y7MJPeKNYHQVHyBF
qbY7nCE5cRbcJ2Bep3Ir+hMiN2WncOykIS2HZNMaFGywRyRMaUKGo3Ah43b9dWhx
RYhLee8CD1c9IllkRZ2UycmeJdgWe+CmUOiFWH87r0FBcqVI+6zlKMk2IRh/HfVp
v646kOwKBF3XPT4YFjX+t2JSeLSaQbRQ+aVq3Twyz354GvPvaVsON91FsToQbj+1
fOJRzleWz/CU1XlbhnTvd8TCMv8+hPzf3weyOeTcgQKBgQDdm6wdu54/B/pfQlUX
T3cyYHFKxDj5S/s96HlLcuUR89Sn7LQwwkkZYwki/osm9B5e54/rbSop/1+beCoO
OxKpSozc8/xms3ulbwpDxR3+xTMj9vAGjjp2hw5vylTH6o7Kyq8kYyPjmGnqNpCf
ANv7mfDl8Jvw/kIAEpWxEo6+HQKBgQDdHm4jLWek8PZbBUmZajzzf1MddXMKX50u
dzhKOF2W57WutJpYRbg4/sz3Ty6qtulDexuWnw+feEkroq8cMfBB7FQaQPtq3nac
coWkTSEUG7Tz1RQ318kslVVJ3Y93iSaoMtrThcaa18+FmVG3SwBefl0uEX8SpAVg
1iP0+pfWkQKBgQCTDDwuUpOT4ZhaY2qRGDLQ47vpT8E6cxeYoczyqp+jxPcEIoYC
oLjetp+Wb+8n/u60LNWL85j52zG2uQq2/K3KVeSYrPF7uHdAdCkMhRz9NB9WKwJk
ZzYV9lI3DbwqF9N+bvW+oGZtHHKTbneSeoB+OEzoVzsys5RZ9fsMT3MWZQKBgAye
W/Kt+Kg1CBoRpy2WHnxW28tmlHYXFsU8EH5L0St3darOq7A16ll2UQQcBLHBVnZ/
ZAeodB/JoYNX+V5Gi0t3zSTiaHak02gCMRY7QJQBMMZpdonpSpW8v+1DM5jCvu4C
WPKRQ9A6WKFrKnqnURITbAXhAbtymMv57HtigZ/BAoGAdpmMRDQNKqai7aGbmbmF
Wy1GbLITkxWAOFScQQUYrFs8cuOGu79aB7PHwzeOIHk/5ESj/gz7hoKJtOgi4ikx
zG2lYqqe11/Gg6wHendR1qR8VrbLBkpqylFTGusmLBuq7y4E/z9y2b4rMciU3OY2
X230g/Q6y6kMprauaCuxNSk=
-----END PRIVATE KEY-----
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2m7Ky3+/U+3M7c47f4R
xifti0wa2fdJialU8ArS1OcQnfYXpXzolUPmRWR+WtXsCN0OYTwNekfwHYOt3Jal
mOIkaeCWbfOBhsNl3i1EUOtFTcZbn0LdWgvaFNEItWJLCNfi6jWusuSjsB6mRZKK
vtuRBpHbjYfcwD3r8tZFZ3v5X1CbMb7YI7jRTflongratzOX7M43gTNnsOR3xzyy
DSq+WKWE0ZFPNE5qzdEdInsEppbqWgJP4Ui9gA1HZs62lai86rye+t0e/XDvkpro
KBBAxCpcSvsQhONr7vVtNHfZtmUhCYIlXlecgwqDisxciZ5oS+nSmBTLg1FNSuDs
bQIDAQAB
-----END PUBLIC KEY-----
```

# Proceso

Usaremos las clave RSA privada para descifrar y volver a cifrar el mensaje.

El padding de PKCS1_OAEP que usamos introduce aleatoriedad en el cifrado, por lo que al descifrar y volver a cifrar el mensaje, obtendremos un mensaje cifrado diferente.

![Ejercicio 11](./imgs/11.png)# Ejercicio 12

Debemos detectar un fallo en el uso del siguiente algoritmo AES/GCM.

## Datos

```bash
Clave: E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74

Nonce: 9Yccn/f5nJJhAt2S
```

## Procedimiento

Usando los datos conseguimos cifrar y descifrar un mensaje. Sin embargo, en el enunciado se dice que en cada comunicación el nonce es compartido. Lo ideal es que el nonce sea único para cada mensaje cifrado.# Ejercicio 13

Se nos pide calcular una firma en hexadecimal con PKCS#1 v1.5 del mensaje dado. Para ello, se nos proporciona la clave privada y publica en formato pem.

Además, debemos calcular el valor de la firma hexadecimal con la curva elíptica ed25519 del mensaje dado con otras claves.

## Datos

```bash
Mensaje: El equipo está preparado para seguir con el proceso, 
necesitaremos más recursos

Clave privada: clave-rsa-oaep-priv.pem

Clave publica: clave-rsa-oaep-publ.pem

Clave privada ed: ed25519-priv

Clave publica ed: ed25519-publ
```

## Procedimiento

Importamos nuestras claves publica y privada en formato pem y el mensaje a firmar. Calculamos el hash del mensaje con sha256 y firmamos el hash con la clave privada. Finalmente, mostramos la firma en hexadecimal.

![Ejercicio 13](./imgs/13.png)

El proceso para calcular la firma con la curva elíptica ed25519 es similar, importamos las claves y el mensaje, calculamos el hash del mensaje y firmamos el hash con la clave privada. Finalmente, mostramos la firma en hexadecimal.

![Ejercicio 13b](./imgs/13b.png)# Ejercicio 14

Se nos pide calcular una clave AES, usando una HKDF con SHA-512, se nos da una clave maestra en el keystore y un identificador de dispositivo.

## Datos

```bash
Master key: A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72
Identificador: e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3
```
## Procedimiento

Importamos la masterkey del keystore y el identificador del dispositivo. Calculamos la clave AES con HKDF y SHA-512. Finalmente, mostramos la clave en hexadecimal.

![Ejercicio 14](./imgs/14.png)# Ejercicio 15

Se nos da un bloque TR31 y su clave de transporte.

Debemos obtener los siguientes datos a partir de los mismos:

- Algoritmo para proteger el bloque de clave.
- Para que algoritmo se ha definido la clave
- Para que modo de uso se ha generado
- Si es exportable o no
- Para que podemos usar la clave
- Valor de la clave

## Datos

```bash
Bloque TR31: 
D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDB
E6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E0
3CD857FD37018E111B
Clave de transporte:
A1A10101010101010101010101010102
```

## Procedimiento

Podemos separar las partes del bloque TR31 para obtener los datos que necesitamos.

Utilizando python y la librería pytr31 podemos obtener los datos que necesitamos:

```
c2c1c1c1c1c1c1c1c1c1c1c1c1c1c1c2
Key Version ID: D
Algoritmo: A
Modo de uso: B
Uso de la clave: D0
Exportabilidad: S
```

Interpretando estos valores podemos saber que:

Key Version: Key block protected using the AES Key Derivation Binding Method.
Modo de uso: Both Encrypt & Decrypt / Wrap & Unwrap
Algoritmos posibles: AES
Key usage: Symmetric Key for Data Encryption 
Exportable: Sensitive, exportable under untrusted key

![Ejercicio 13](./imgs/13.png)
