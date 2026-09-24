# Ejercicio 1. Demostracion de ejecucion

import sys
import psutil 

# i. PLATAFORMA
print(f"Estamos usando Windows. {psutil.WINDOWS}")
print(f"Estamos usando Linux. {psutil.WINDOWS}")

# ii. CPUs
print(f"Número de CPUs: {psutil.cpu_count()}")
print(f"Frecuencia de cada CPU: {[f.max for f in psutil.cpu_freq(percpu=True)]}")
print(f"Uso de CPU por CPUs: {psutil.cpu_times_percent(interval=1)}")

# iii. MEMORIA RAM
memoria = psutil.virtual_memory()
print(f"Memoria total: {memoria.total} bytes")
print(f"Memoria disponible: {memoria.available} bytes")
print(f"Porcentaje de memoria usada: {memoria.percent}%")

# iv. DISCOS
print(f"Listado de particiones: {psutil.disk_partitions(all=True)}")
# print(f"Uso de disco para la ruta: {psutil.disk_usage('/home/vagrant/scripts')}")
print(f"Número de operaciones de lectura: {psutil.disk_io_counters().read_count}")
print(f"Número de operaciones de escritura: {psutil.disk_io_counters().write_count}")
print(f"Número de bytes leídos: {psutil.disk_io_counters().read_bytes}")
print(f"Número de bytes escritos: {psutil.disk_io_counters().write_bytes}")

# v. RED
print(f"Bytes enviados: {psutil.net_io_counters().bytes_sent}")
print(f"Bytes recibidos: {psutil.net_io_counters().bytes_recv}")
print(f"Paquetes enviados: {psutil.net_io_counters().packets_sent}")
print(f"Paquetes recibidos: {psutil.net_io_counters().packets_recv}")