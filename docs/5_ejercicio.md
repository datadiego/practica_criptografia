## Ejercicio 5

Se nos da un mensaje y su salida en keccak SHA3 y SHA2 y se nos pide identificar el tipo de SHA que se utilizó. 
Tambien se nos pide convertir a SHA3 Keccak de 256 bits y analizar un mensaje con un cambio menor en el string.

### Datos

mensaje original: En KeepCoding aprendemos cómo protegernos con criptografía
SHA3:bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
SHA2:4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833

mensaje a convertir: En KeepCoding aprendemos cómo protegernos con criptografía.

### Procedimiento


Podemos saber el tipo de SHA3 por el largo del hash, en este caso, el hash tiene 32 bytes, por lo que se utilizó SHA3-256.

Podemos comprobarlo con la salida al convertir el mensaje:

SHA3 del ejercicio: bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe

```bash
Mensaje: En KeepCoding aprendemos cómo protegernos con criptografía
sha3_224 28 5f12ac6c044097c694bf740504679ef78e38a4a8fca86eb4ef9e05ae
sha3_256 32 bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
sha3_384 48 e5bf162669b89ec5e6e7a406bf148719906ed3755baab32c891b1e0e59ec75e40564e2a3d9d4432defb28904eec7e827
sha3_512 64 cc4d56beacf9a488f92b32b612147c088e87d2c9563c6e38bca6e834d7c742dff906dcd68b8bb8ed98f045e02c2e59c6608216225179348ae4db66c65e6e927c
```

Si utilizamos SHA2:
SHA2 del ejercicio: 4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833

```bash
Mensaje: En KeepCoding aprendemos cómo protegernos con criptografía
sha224 28 a4544beb16e1dfb9b578d518bf19e2a8109ffe27cab9172911e55543
sha256 32 13067f558aed141a490bf95775e0c6fc583a09178ae7a0fefe93a8336be81237
sha384 48 dca9a06f36b492b374216e60dc7668bea8119ec35ca259aa797ec8125654f4dc088144b00f16d5155bcb3c1e295784f4
sha512 64 4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833
```

Podemos ver que el algoritmo utilizado fue sha512.

Si convertimos el mensaje dado y comparamos con el anterior:

```bash
Mensaje: En KeepCoding aprendemos cómo protegernos con criptografía.
sha3_256 32 302be507113222694d8c63f9813727a85fef61a152176ca90edf1cfb952b19bf

Mensaje: En KeepCoding aprendemos cómo protegernos con criptografía
sha3_256 32 bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
```

Podemos ver que el hash cambia completamente, por lo que los hashes son lo suficientemente distintos con un cambio menor.

![Ejercicio 5](./imgs/5.png)