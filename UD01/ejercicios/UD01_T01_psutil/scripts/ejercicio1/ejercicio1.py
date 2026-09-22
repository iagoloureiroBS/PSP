# Ejercicio 1. Demostracion de ejecucion

import psutil

# i.

print(f"Estamos usando Windows. {psutil.WINDOWS}")
print(f"Estamos usando Linux. {psutil.LINUX}")

# ii.

print(f"Número de CPUs: {psutil.cpu_count}")
print(f"Frecuencia de cada CPU: {[f.max for f in psutil.cpu_freq(percpu=True)]}")
print(f"Uso de CPU por CPUs: {psutil.cpu_times_percent(interval=1, percpu=True)}")