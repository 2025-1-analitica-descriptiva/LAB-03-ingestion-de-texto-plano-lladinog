import pandas as pd
import re

def open_file_lines(file_path):
    """
    Helper function to open a file and return its content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def found_header_line(lines, search_pattern):
    """
    Helper function to find the line when end the header and start the data.
    It returns the line number where the data starts.
    """
    for i, line in enumerate(lines):
        if re.match(r'\s*' + re.escape(search_pattern), line, re.IGNORECASE):
            return i + 1
    return 0  # Default if no header found

def define_rows(lines, number_of_columns, separator_pattern, row_start_pattern):
    """
    Helper function to define rows from the lines of text.
    It splits the lines based on a separator pattern and identifies the start of each row.
    The function returns a list of lists, where each inner list represents a row of data.
    """
    data = []
    current_row = []
    for _, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue  # Saltar líneas vacías

        if re.match(row_start_pattern, line):
            if current_row:
                data.append(current_row)
            parts = re.split(separator_pattern, line, maxsplit=number_of_columns - 1)
            current_row = parts

        else:
            current_row[-1] += ' ' + line

    if current_row:
        data.append(current_row)

    return data

def clean_text_column(data, column_index):
    """
    Clean the text in a specific column of the data.
    """
    for row in data:
        palabras = row[column_index]
        palabras = re.sub(r'\s+', ' ', palabras)
        palabras = palabras.replace('.', '')
        palabras = ', '.join([p.strip() for p in palabras.split(',')])
        row[column_index] = palabras
    return data

def create_dataframe(data, columns):
    """
    Helper function to create a DataFrame from data and columns.
    """
    df = pd.DataFrame(data, columns=columns)
    for col in df.columns:
        # Verificar el tipo de dato y convertirlo si es necesario
        if df[col].str.contains('%').any():
            df[col] = df[col].str.replace(',', '.').str.replace('%', '').astype(float)
        elif df[col].str.isnumeric().all():
            df[col] = df[col].astype(int)
        
    return df
        
    