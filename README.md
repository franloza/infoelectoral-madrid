# infoelectoral-madrid
Aplicación para obtener los datos de las candidaturas a las elecciones autonómicas de la Comunidad de Madrid en los últimos años.

Repositorio inspirado en [infoelectoral](https://github.com/JaimeObregon/infoelectoral) de [JaimeObregon](https://github.com/JaimeObregon).
Este repositorio surge de la necesidad de acudir a los portales de cada gobierno autómico para obtener las candidaturas (Ver [Issue](https://github.com/JaimeObregon/infoelectoral/issues/2))

Esta aplicación genera un fichero CSV con los datos contenidos en el [portal de la JEC](http://www.juntaelectoralcentral.es/cs/jec/elecciones/autonomicas/madrid) para las elecciones autonómicas de Madrid 
celebradas entre 2011 y 2019.

## Proceso
1. He añadido todos los documentos en formato comprimido en la carpeta [files/pdf](files/pdf). Para añadir algún fichero mas,
solo es necesario añadir la URL y la fecha a [files/info.csv](files/info.csv) y ejecutar el script [files/download.sh](files/download.sh)
2. He descomprimido los documentos PDF y he usado la CLI de [pdfminer.six](https://github.com/pdfminer/pdfminer.six) para extraer la versión en texto
de los documentos. La versión .txt no es del todo perfecta así que he adaptado los ficheros de manera manual para tener la siguiente estructura:
```
PARTIDO #2(SIGLAS)
1. Candidato #1
2. Candidato #2
...
Suplentes
1. Suplente #1
...

PARTIDO #2 (SIGLAS)
...
```
3. He comprimido los ficheros .txt en la carpeta [files/txt](files/txt).

## Requisitos
- Docker o Python>=3.7

## Obtener datos
`make run > data.csv` o `python3 src/parse.py files > data.csv`
