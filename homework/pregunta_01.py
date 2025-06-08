"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
from homework.utils import open_file_lines, found_header_line, define_rows, clean_text_column, create_dataframe

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    # Leer el archivo de texto
    lines = open_file_lines('files/input/clusters_report.txt')

    # Encontrar la línea donde empiezan los datos (después de los encabezados)
    header_line = found_header_line(lines, '---')
  
    # Procesar y definir las filas del dataframe
    data = define_rows(
        lines[header_line:],
        number_of_columns=4,
        separator_pattern=r'\s{2,}',
        row_start_pattern=r'^\s*\d+'
    )
    
    # Limpiar la columna de palabras clave
    data = clean_text_column(data, column_index=-1)

    columnas = [
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ]

    df = create_dataframe(data, columnas)
    
    return df

if __name__ == "__main__":
    print(pregunta_01().head())
