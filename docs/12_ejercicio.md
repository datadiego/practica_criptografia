# Ejercicio 12

Debemos detectar un fallo en el uso del siguiente algoritmo AES/GCM.

## Datos

Clave: E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74 
Nonce: 9Yccn/f5nJJhAt2S

## Procedimiento

Analizando los datos podemos ver que se está utilizando un nonce de 12 bytes, lo cual es correcto, pero este es fijo. 