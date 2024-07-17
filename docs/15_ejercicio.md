# Ejercicio 13

Se nos da un bloque TR31 y su clave de transporte.

Debemos obtener los siguientes datos a partir de los mismos:

- Algoritmo para proteger el bloque de clave.
- Para que algoritmo se ha definido la clave
- Para que modo de uso se ha generado
- Si es exportable o no
- Para que podemos usar la clave
- Valor de la clave

## Datos

Bloque TR31:

```
D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B
```

Clave de transporte:

```
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

## Solucion

Algoritmo para proteger el bloque de clave: AES Key Derivation Binding Method

Para que algoritmo se ha definido la clave: AES

Para que modo de uso se ha generado: Both Encrypt & Decrypt / Wrap & Unwrap

Es exportable con una clave no confiable

Podemos usar la clave para ********

El valor de la clave es: c2c1c1c1c1c1c1c1c1c1c1c1c1c1c1c2