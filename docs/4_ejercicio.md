# Ejercicio 4

Se nos da un jwt y se nos pide con que algoritmo fue firmado.
Luego se nos proporciona otro jwt, debemos decodificarlo y analizar que está intentando hacer el usuario e intentar validarlo con pyjwt.

## Datos

jwt: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"

## Procedimiento

Podemos separar las partes del jwt usando como separador el punto. Luego decodificamos el contenido y obtenemos el algoritmo en el campo "alg" del header.

El algoritmo con el que fue firmado el jwt es HS256.

El cuerpo del jwt es:

```json
{"usuario":"Don Pepito de los palotes","rol":"isNormal","iat":1667933533}
```

![Ejercicio 4](./imgs/4.png)
