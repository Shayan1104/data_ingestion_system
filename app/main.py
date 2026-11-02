from fastapi import FastAPI
from .database import engine
from .routers import excel_router, pdf_router, weather_router

app = FastAPI(title="Data Ingestion API")

app.include_router(excel_router.router)
app.include_router(pdf_router.router)
app.include_router(weather_router.router)
@app.get("/")
def read_root():
    return {"message": "Data Ingestion API is running"}