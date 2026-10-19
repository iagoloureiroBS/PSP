
# Ejemplo de uso: python measure_command.py python tarea.py ping as.com
# Salida esperada: 
# Ejecutando: python tarea.py
# Salida del proceso:
# Tarea terminada

# Tiempo de ejecución: 2.01 segundos
# Código de salida: 0

import sys
import subprocess
import time

argumentos = sys.argv[1:]

print(argumentos)

print(f"""
Ejecutando: {" ".join(argumentos)}
Salida del proceso:
""")

inicio = time.perf_counter()

resultado = subprocess.run(argumentos, shell=True)

fin = time.perf_counter()
print(f"""
{resultado.stdout}
{resultado.stderr}
Tarea terminada

Tiempo de ejecución: {(fin - inicio):2.2} segundos
Código de salida: {resultado.returncode}




""")