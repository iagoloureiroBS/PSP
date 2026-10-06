# Ejercicio 1. Demostracion de ejecucion

#import datetime
from datetime import datetime
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

# b.
def mostrar_filtrados():
    filtro = input("Introduce el filtro (ej: 'iniciado manual' o solo 'parado'): ").strip().lower()
    
    palabras = filtro.split()
    
    if not palabras or len(palabras) > 2:
        print("Filtro no válido. Debe introducir una o dos palabras (ej: 'iniciado manual').")
        return
    
    map_estado = {"iniciado": "running", "parado": "stopped"}
    map_inicio = {"manual": "manual", "automático": "automatic", "automatico": "automatic"}

    estado_buscado = None
    inicio_buscado = None

   
    if len(palabras) == 1:
        if palabras[0] in map_estado:
            estado_buscado = map_estado[palabras[0]]
        elif palabras[0] in map_inicio:
            inicio_buscado = map_inicio[palabras[0]]
        else:
            print(f"Palabra desconocida '{palabras[0]}'. Use: iniciado, parado, manual o automático.")
            return
   
    elif len(palabras) == 2:
        if palabras[0] in map_estado and palabras[1] in map_inicio:
            estado_buscado = map_estado[palabras[0]]
            inicio_buscado = map_inicio[palabras[1]]
        else:
            print("El formato debe ser '<estado> <inicio>'. Ejemplo: 'iniciado manual'.")
            print("Estados válidos: iniciado, parado. Inicios válidos: manual, automático.")
            return

    print(f"\n{'NOMBRE':<35} | {'PID':<8} | {'ESTADO':<12} | {'TIPO INICIO':<12}")
    print("-" * 70)
    
    try:
        for s in psutil.win_service_iter():
            try:
                d = s.as_dict()
                status = d.get('status', '')
                start_type = d.get('start_type', '')
                
                # Comprobar si el servicio cumple con las condiciones establecidas
                cumple_estado = (estado_buscado is None) or (status == estado_buscado)
                cumple_inicio = (inicio_buscado is None) or (start_type == inicio_buscado)
                
                if cumple_estado and cumple_inicio:
                    name = d.get('name', '')
                    pid = d.get('pid', 'N/A')
                    print(f"{name:<35} | {str(pid):<8} | {status:<12} | {start_type:<12}")
            except Exception:
                continue
    except Exception as e:
        print(f"Error al mostrar servicios filtrados: {e}")


# c.
def mostrar_descripcion():
    nombre_servicio = input("\nIntroduce el nombre exacto del servicio: ").strip()
    
    try:
        servicio = psutil.win_service_get(nombre_servicio)
        descripcion = servicio.description()
        display_name = servicio.display_name()
        
        print("-" * 70)
        print(f"Servicio: {nombre_servicio} ({display_name})")
        
        if descripcion:
            print(f"Descripción: {descripcion}")
        else:
            print("Descripción: (No hay descripción disponible para este servicio).")
            
        print("-" * 70)
        
    except psutil.NoSuchProcess:
        print(f"Error: El servicio '{nombre_servicio}' no existe o el nombre es incorrecto.")
    except psutil.AccessDenied:
        print(f"Error: Acceso denegado. Es posible que necesites ejecutar el script como Administrador.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al buscar el servicio: {e}")

