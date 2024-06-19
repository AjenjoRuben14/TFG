import json
import csv

def fusionar_json(archivos_txt, archivo_salida):
    # Obtener todos los nombres de campo únicos de todos los archivos JSON
    nombres_campos = set()
    for archivo_txt in archivos_txt:
        with open(archivo_txt, 'r') as f:
            datos_json = json.load(f)
            for fila in datos_json:
                nombres_campos.update(fila.keys())

    # Escribir los datos fusionados en un archivo CSV
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as csvfile:
        escritor_csv = csv.DictWriter(csvfile, fieldnames=nombres_campos)
        escritor_csv.writeheader()

        # Leer cada archivo JSON y escribir los datos en el archivo CSV
        for archivo_txt in archivos_txt:
            with open(archivo_txt, 'r') as f:
                datos_json = json.load(f)
                for fila in datos_json:
                    # Verificar si cada nombre de campo está presente en la fila
                    # Si no está presente, agregar un valor en blanco para ese campo
                    for campo in nombres_campos:
                        if campo not in fila:
                            fila[campo] = ''
                    escritor_csv.writerow(fila)

def main(archivos_txt, archivo_salida):
    fusionar_json(archivos_txt, archivo_salida)
    print("Se ha creado el archivo CSV fusionando los datos de los archivos JSON.")

if __name__ == "__main__":
    archivos_txt = [
        "C:/Users/ruben/OneDrive/Escritorio/TFG/DatosMeteorologicos/LasPalmas_2009.txt",
        "C:/Users/ruben/OneDrive/Escritorio/TFG/DatosMeteorologicos/LasPalmas_2014.txt",
        "C:/Users/ruben/OneDrive/Escritorio/TFG/DatosMeteorologicos/LasPalmas_2019.txt",
        "C:/Users/ruben/OneDrive/Escritorio/TFG/DatosMeteorologicos/LasPalmas_2024.txt"
    ]
    archivo_salida = "datos_fusionados.csv"
    main(archivos_txt, archivo_salida)
