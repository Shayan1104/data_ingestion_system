from fastapi import APIRouter
import PyPDF2
from ..database import engine, pdf_table

router = APIRouter()

@router.post("/ingest-pdf")
def ingest_pdf():

    file_path = "data/sample.pdf"
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    conn = engine.connect()

    conn.execute(
        pdf_table.insert().values(content=text)
    )

    conn.commit()

    return {"message": "PDF ingested successfully"}


@router.get("/pdf-data")
def get_pdf_data():

    conn = engine.connect()

    result = conn.execute(pdf_table.select()).fetchall()

    return [dict(row._mapping) for row in result]