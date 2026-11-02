import pandas as pd

def read_pdf_file(file_path):
    df = read_pdf_file(file_path, engine="openpyx1")
    df.columns = df.columns.str.lower().str.strip()
    print("Columns:", df.columns)
    print("Data:", df)
    data = df.to_dict(orient="records")
    return data
   