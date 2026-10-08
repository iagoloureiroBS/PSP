import psutil


# 3.

# a.
print(f"Información de todos los procesos: {[p for p in psutil.process_iter(attrs=['pid','name', 'username'])]}")

# b.
procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username']) if p.memory_percent()>1]

print(f"Procesos filtrados por uso de memoria: {procesos.sort(key=lambda p: p.memory_percent(), reverse=True)}")

#c.