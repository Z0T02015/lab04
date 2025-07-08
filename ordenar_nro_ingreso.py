import csv

# Leer los datos del archivo
with open("datos.csv", newline='') as archivo:
    lector = csv.DictReader(archivo, delimiter=';')
    ingresos = [int(fila["nro_ingreso"]) for fila in lector]

print("Datos leídos (nro_ingreso):")
print(ingresos)

# Ordenar de menor a mayor
ingresos.sort()

print("\n Datos ordenados (menor a mayor):")
print(ingresos)

# Guardar en nro_ingreso.csv
with open("nro_ingreso.csv", mode='w', newline='') as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(["nro_ingreso"])
    for ingreso in ingresos:
        escritor.writerow([ingreso])

print("\n Archivo 'nro_ingreso.csv' generado con éxito.")