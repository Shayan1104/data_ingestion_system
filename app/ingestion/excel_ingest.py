import pandas as pd

def read_excel_file(file_path):

    df = pd.read_excel(file_path, engine="openpyxl")

    # normalize column names
    df.columns = df.columns.str.lower().str.strip()

    print("Columns:", df.columns)
    print("Data:", df)

    data = df.to_dict(orient="records")

    return data