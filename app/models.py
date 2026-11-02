from sqlalchemy import Column, Integer, String
from .database import Base


class ExcelData(Base):
    __tablename__ = "excel_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(String)


class PDFData(Base):
    __tablename__ = "pdf_data"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(String)