# Ejercicio RSA

## Respuesta Parte 1

El sistema usa RSA como mecanismo de intercambio de clave, protegiendo una clave AES que cifra el documento real. ¿Explique por qué no cifrar el documento directamente con RSA?

Realmente no se cifra un documento directamene con RSA porque este no está diseñado para cifrar grandes cantidades
de datos de manera eficiente. Aunque RSA sí puede cifrar datos, su uso principal es proteger pequeñas porciones de 
datos, como claves de cifrado, no fue diseñado para cifrar documentos completos.

Además RSA es significativamente más lento en comparación con algoritmos simétricos como AES, debido a que sus 
operaciones criptográficas involucran cálculos matemáticos complejos con números muy grandes. Otra limitación es que 
RSA solo puede cifrar mensajes donde el tamaño sea menor al de la clave. Por esta razón, RSA no es adecuado para cifrar archivos o documentos grandes.

## Respuesta Parte 2

¿Qué información contiene un archivo .pem? Abre public_key.pem con un editor de texto y
describe su estructura.

El archivo .pem contiene la información criptográfica codificada en texto para que pueda ser leída y compartida fácilmente. Al abrir
la public_key.pem logre ver que contiene un encabezado que indica que es una llave pública, seguido de un bloque de texto en Base64
que es la clave en sí, y al final un pie que marca el final de la llave. No es legible totalmente pero entre ese bloque se encuentran los datos de la clave pública RSA.

## Respuesta Parte 2

¿Porqué cifrar el mismo mensaje dos veces produce resultados distintos? Demuéstrenlo y
expliquen que propiedad de OAEP lo cause

Al cifrar el mismo mensaje dos veces con RSA-OAEP, se obtienen resultados distintos porque OAEP agrega aleatoriedad al proceso de cifrado. Esto hace que, aunque el mensaje y la clave pública sean los mismos, cada salida cifrada sea diferente, lo cual mejora la seguridad al evitar patrones repetidos.
