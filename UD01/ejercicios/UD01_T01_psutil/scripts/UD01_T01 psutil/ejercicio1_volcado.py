import psutil
import _json

info = {
    "plataforma": {
        "windows": psutil.WINDOWS,
        "linux": psutil.WINDOWS
    },
    "cpus": {
        "numero": psutil.cpu_count(),
        "frecuencia": [f.max for f in psutil.cpu_freq(percpu=True)],
        "uso_porcentaje": dict(psutil.cpu_times_percent(interval=1)._asdict())
    },
    "memoria_ram": {
        "total": psutil.virtual_memory().total,
        "disponible": psutil.virtual_memory().available,
        "porcentaje_usado": psutil.virtual_memory().percent
    },
    "discos": {
        "particiones": [p._asdict() for p in psutil.disk_partitions(all=True)],
        "uso_ruta": dict(psutil.disk_usage('.')._asdict()),
        "io_lectura_count": psutil.disk_io_counters().read_count,
        "io_escritura_count": psutil.disk_io_counters().write_count,
        "io_bytes_leidos": psutil.disk_io_counters().read_bytes,
        "io_bytes_escritos": psutil.disk_io_counters().write_bytes
    },
    "red": {
        "bytes_enviados": psutil.net_io_counters().bytes_sent,
        "bytes_recibidos": psutil.net_io_counters().bytes_recv,
        "paquetes_enviados": psutil.net_io_counters().packets_sent,
        "paquetes_recibidos": psutil.net_io_counters().packets_recv
    }
}