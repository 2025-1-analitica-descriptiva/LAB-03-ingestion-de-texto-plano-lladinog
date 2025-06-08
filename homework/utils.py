import pandas as pd
import re

def open_file_lines(file_path):
    """
    Helper function to open a file and return its content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def clean_text(lines):
    # Encontrar la línea donde empiezan los datos (después de los encabezados)
    header_line = 0
    for i, line in enumerate(lines):
        if re.match(r'\s*-----', line, re.IGNORECASE):
            header_line = i+1
            print("Header line found at:", header_line)
            break
    # Procesar los datos
    data = []
    current_row = []
    for line in lines[header_line:]:
        if re.match(r'\s*\d+', line):
            # Nueva fila
            if current_row:
                data.append(current_row)
            parts = re.split(r'\s{2,}', line.strip(), maxsplit=3)
            current_row = parts
        else:
            # Continuación de palabras clave
            if current_row:
                current_row[-1] += ' ' + line.strip()
    if current_row:
        data.append(current_row)

    # Limpiar y formatear las palabras clave
    for row in data:
        palabras = row[-1]
        palabras = re.sub(r'\s+', ' ', palabras)
        palabras = palabras.replace('.','')
        palabras = ', '.join([p.strip() for p in palabras.split(',')])
        row[-1] = palabras
    return data

def create_dataframe(data, columns):
    """
    Helper function to create a DataFrame from data and columns.
    """
    df = pd.DataFrame(data, columns=columns)
    df['cluster'] = df['cluster'].astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.').str.replace('%', '').astype(float)
    return df
        
    