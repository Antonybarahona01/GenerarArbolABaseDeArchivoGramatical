#Integrantes
David Martinez
Franco Comas
Antony Barahona

# Instrucciones para Ejecutar el Programa de Análisis Sintáctico

## Introducción

Este programa está diseñado para construir y visualizar un árbol de análisis sintáctico basado en una gramática definida en un archivo de texto y una cadena de entrada. A continuación, encontrarás todos los pasos necesarios para ejecutar el programa.

## Requisitos

Asegúrate de tener instalado lo siguiente en tu computadora:

- Python 3
- Pip (administrador de paquetes de Python)

Además, necesitas instalar las bibliotecas `networkx` y `matplotlib`. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

`bash`
pip install networkx matplotlib
Estructura del Repositorio
Dentro del repositorio, encontrarás los siguientes archivos:

grafo.py: El archivo principal del programa.
gramatica.txt: Archivo que contiene la gramática que se utilizará para el análisis.
cadena.txt: Archivo que contiene la cadena de entrada que se analizará.
Contenido de los Archivos
1. gramatica.txt
Asegúrate de que el archivo gramatica.txt contenga el siguiente contenido:

plaintext
Copiar código
N: E, T, O, N
T: 2, 3, 4
S: E
P:
E -> E O N | N
O -> + | -
N -> 2 | 3 | 4
2. cadena.txt
Asegúrate de que el archivo cadena.txt contenga el siguiente contenido:

plaintext
Copiar código
2 + 3
Ejecución del Programa
Abre una terminal en la carpeta donde se encuentran los archivos grafo.py, gramatica.txt y cadena.txt.

Ejecuta el programa con el siguiente comando:

bash
Copiar código
python3 grafo.py
El programa leerá los archivos, construirá el árbol de análisis sintáctico y lo mostrará en una ventana emergente.
Visualización del Árbol
Una vez que el programa se ejecute, se abrirá una ventana que mostrará el árbol de análisis sintáctico correspondiente a la cadena de entrada.
