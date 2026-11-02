from fastapi import APIRouter
import pandas as pd
from ..database import engine, excel_table

router = APIRouter()

@router.post("/ingest-excel")
def ingest_excel():

    file_path = "data/sample.xlsx"

    df = pd.read_excel(file_path)

    records = df.to_dict(orient="records")

    conn = engine.connect()

    for row in records:
        conn.execute(excel_table.insert().values(**row))

    conn.commit()
    conn.close()

    return {"message": "Excel ingested successfully"}


@router.get("/excel-data")
def get_excel_data():

    conn = engine.connect()

    result = conn.execute(excel_table.select()).fetchall()

    conn.close()

    return [dict(row._mapping) for row in result]