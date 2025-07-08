import csv

# Leer y filtrar los DNI pares
with open("datos.csv", newline='') as archivo:
    lector = csv.DictReader(archivo, delimiter=';')
    dnis_pares = [int(fila["dni"]) for fila in lector if int(fila["dni"]) % 2 == 0]

print(" DNI pares encontrados:")
print(dnis_pares)

# Ordenar de mayor a menor
dnis_pares.sort(reverse=True)

print("\n DNI ordenados (mayor a menor):")
print(dnis_pares)

# Guardar en dni.csv
with open("dni.csv", mode='w', newline='') as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(["dni"])
    for dni in dnis_pares:
        escritor.writerow([dni])

print("\n Archivo 'dni.csv' generado con éxito.")