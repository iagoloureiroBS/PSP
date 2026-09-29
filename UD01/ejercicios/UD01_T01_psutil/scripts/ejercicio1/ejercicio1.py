# Ejercicio 1. Demostracion de ejecucion

import datetime
import json
import sys
import psutil 

# i. PLATAFORMA
print(f"Estamos usando Windows. {psutil.WINDOWS}")
print(f"Estamos usando Linux. {psutil.WINDOWS}")

# ii. CPUs
print(f"Número de CPUs: {psutil.cpu_count()}")
freqs = [f.max for f in psutil.cpu_freq(percpu=True)]
print(f"Frecuencia de cada CPU: {[f.max for f in psutil.cpu_freq(percpu=True)]}")
cpu_times = psutil.cpu_times_percent(interval=1)
print(f"Uso de CPU por CPUs: {psutil.cpu_times_percent(interval=1)}")

# iii. MEMORIA RAM
memoria = psutil.virtual_memory()
print(f"Memoria total: {memoria.total} bytes")
print(f"Memoria disponible: {memoria.available} bytes")
print(f"Porcentaje de memoria usada: {memoria.percent}%")

# iv. DISCOS
print(f"Listado de particiones: {psutil.disk_partitions(all=True)}")
disk_io = psutil.disk_io_counters()
# print(f"Uso de disco para la ruta: {psutil.disk_usage('/home/vagrant/scripts')}")
print(f"Número de operaciones de lectura: {psutil.disk_io_counters().read_count}")
print(f"Número de operaciones de escritura: {psutil.disk_io_counters().write_count}")
print(f"Número de bytes leídos: {psutil.disk_io_counters().read_bytes}")
print(f"Número de bytes escritos: {psutil.disk_io_counters().write_bytes}")

# v. RED
net_io = psutil.net_io_counters()
print(f"Bytes enviados: {psutil.net_io_counters().bytes_sent}")
print(f"Bytes recibidos: {psutil.net_io_counters().bytes_recv}")
print(f"Paquetes enviados: {psutil.net_io_counters().packets_sent}")
print(f"Paquetes recibidos: {psutil.net_io_counters().packets_recv}")

# b. Guardar información del sistema en JSON
ruta_destino = "./" 
nombre_fichero = f"{datetime.now().strftime('%Y%m%D%H%M%S')}-system-info.json"

with open(f"{ruta_destino}{nombre_fichero}", "w") as f:
    json.dump({
        "cpus": {"count": psutil.cpu_count(), "freq": freqs},
        "memoria": {"total": memoria.total, "available": memoria.available, "percent": memoria.percent},
        "discos": {"read_bytes": disk_io.read_bytes, "write_bytes": disk_io.write_bytes},
        "red": {"bytes_sent": net_io.bytes_sent, "bytes_recv": net_io.bytes_recv}
    }, f, indent=4)

# 2.

# a.
def mostrar_todos():
    """Muestra todos los servicios de Windows con su nombre, PID, estado y tipo de inicio."""
    print(f"\n{'NOMBRE':<35} | {'PID':<8} | {'ESTADO':<12} | {'TIPO INICIO':<12}")
    print("-" * 70)
    try:
        for s in psutil.win_service_iter():
            try:
                d = s.as_dict()
                name = d.get('name', '')
                pid = d.get('pid', 'N/A')
                status = d.get('status', '')
                start_type = d.get('start_type', '')
                print(f"{name:<35} | {str(pid):<8} | {status:<12} | {start_type:<12}")
            except (Exception):
                continue
    except Exception as e:
        print(f"Error al mostrar: {e}")

def mostrar_filtrados():
    filtro = input("Introduce el filtro (ej: 'iniciado manual' o solo 'parado'): ").strip().lower()
    
    palabras = filtro.split()

    
    if not palabras or len(palabras) > 2:
        print("Filtro no válido. Debe introducir una o dos palabras (ej: 'iniciado manual').")
        return
