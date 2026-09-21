Elabora un programa en Python que permita consultar la información del sistema. El programa mostrará un menú con dos opciones:
1. Mostrar información del sistema: Deberán mostrarse por pantalla los siguientes datos:
    - Plataforma sobre la que se ejecuta el script: Windows o Linux
    - Información de CPUs
        . Número de CPUs
        . Frecuencia de cada CPU
        . Uso de CPU por CPUs
    - Información de memoria
2. Memoria total
    - Memoria disponible
    - Porcentaje de memoria usada
3. Información de discos
    - Listado de particiones
    - Uso de disco para cada unidad o partición
    - Número de operaciones de lectura
    - Número de operaciones de escritura
    - Número de bytes leídos
    - Número de bytes escritos
4. Estadísticas de red
    - Bytes enviados
    - Bytes recibidos
    - Paquetes enviados
    - Paquetes recibidos
 Guardar información del sistema:
Realizará un volcado de la información del sistema que se muestra por pantalla a un fichero JSON en la ruta que se proporcione, siendo el nombre del fichero el siguiente: yyyyMMddhhmmss-system-info.json
