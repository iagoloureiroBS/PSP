

import sys
import subprocess



nombre_fichero_alias = "alias.txt"
alias = {}

with open() as fichero:
    for linea in fichero.readlines():
        #separar la linea en dos partes y meter en el diccionario clave = valor
        k,v = linea.strip("\n").split("=")
        alias[k] = v

    # Meter cosas en diccionario alias

    alias = { k:v for k,v in list(map(lambda linea: linea.strip("\n").split("=") ,fichero.readlines()))}
print(alias)


argumentos = sys.argv[1:]

print("""
MiniShell
Escribe 'exit' para terminar.
""")
input()