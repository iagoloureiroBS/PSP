# 2.

# a.
import psutil


def mostrar_todos():
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
            print("El formato debe ser por ejemplo: 'iniciado manual'.")
            print("Estados: iniciado, parado. Inicios: manual, automático.")
            return

    print(f"\n{'NOMBRE':<35} | {'PID':<8} | {'ESTADO':<12} | {'TIPO INICIO':<12}")
    print("-" * 70)
    
    try:
        for s in psutil.win_service_iter():
            try:
                d = s.as_dict()
                status = d.get('status', '')
                start_type = d.get('start_type', '')
                
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