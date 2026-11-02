from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///data.db")

metadata = MetaData()

excel_table = Table(
    "excel_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("value", String)
)

pdf_table = Table(
    "pdf_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("content", String)
)
weather_table = Table(
    "weather_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("city", String),
    Column("temperature", String),
    Column("description", String)
)

metadata.create_all(engine)