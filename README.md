# Ejercicio RSA

## Respuesta Parte 1

El sistema usa RSA como mecanismo de intercambio de clave, protegiendo una clave AES que cifra el documento real. ¿Explique por qué no cifrar el documento directamente con RSA?

Realmente no se cifra un documento directamene con RSA porque este no está diseñado para cifrar grandes cantidades
de datos de manera eficiente. Aunque RSA sí puede cifrar datos, su uso principal es proteger pequeñas porciones de 
datos, como claves de cifrado, no fue diseñado para cifrar documentos completos.

Además RSA es significativamente más lento en comparación con algoritmos simétricos como AES, debido a que sus 
operaciones criptográficas involucran cálculos matemáticos complejos con números muy grandes. Otra limitación es que 
RSA solo puede cifrar mensajes donde el tamaño sea menor al de la clave. Por esta razón, RSA no es adecuado para cifrar archivos o documentos grandes.

