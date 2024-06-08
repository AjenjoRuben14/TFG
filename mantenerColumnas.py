import os
import csv

def mantener_columnas(archivo_entrada, archivo_salida, columnas_a_mantener):
    with open(archivo_entrada, 'r') as csv_entrada, open(archivo_salida, 'w', newline='') as csv_salida:
        lector_csv = csv.DictReader(csv_entrada)

        escritor_csv = csv.DictWriter(csv_salida, fieldnames=columnas_a_mantener)
        escritor_csv.writeheader()

        for fila in lector_csv:
            fila_nueva = {columna: fila[columna] for columna in columnas_a_mantener}
            escritor_csv.writerow(fila_nueva)

def cambios_directorio(directorio_entrada, directorio_salida, columnas_a_mantener):
    archivos_entrada = os.listdir(directorio_entrada)
    for archivo_entrada in archivos_entrada:
        ruta_entrada = os.path.join(directorio_entrada, archivo_entrada)
        ruta_salida = os.path.join(directorio_salida, archivo_entrada)
        mantener_columnas(ruta_entrada, ruta_salida, columnas_a_mantener)
        print(f"Se han mantenido las columnas especificadas en el archivo {ruta_salida}.")

if __name__ == "__main__":
    directorio_entrada = input("Introduce la ruta del directorio de entrada: ")
    directorio_salida = input("Introduce la ruta del directorio de salida: ")

    columnas_a_mantener = input("Introduce las columnas que deseas mantener (separadas por coma): ")
    columnas_a_mantener = [columna.strip() for columna in columnas_a_mantener.split(",")]

    cambios_directorio(directorio_entrada, directorio_salida, columnas_a_mantener)


