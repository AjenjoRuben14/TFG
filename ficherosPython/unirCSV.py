import pandas as pd
import glob

# Lista de archivos CSV en el directorio actual
csv_files = glob.glob("*.csv")

# Inicializar un DataFrame vacío para almacenar los datos combinados
combined_data = pd.DataFrame()

# Iterar sobre cada archivo CSV
for i, file in enumerate(csv_files):
    # Leer el archivo CSV
    data = pd.read_csv(file)
    # Si es el primer archivo, mantener la primera fila
    if i == 0:
        combined_data = combined_data.append(data)
    # Para los archivos restantes, omitir la primera fila
    else:
        combined_data = combined_data.append(data[1:], ignore_index=True)

# Escribir los datos combinados en un nuevo archivo CSV
combined_data.to_csv("combined_data.csv", index=False)



