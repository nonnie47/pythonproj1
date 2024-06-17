from sqlalchemy import URL, create_engine

url_object = URL.create(
    "postgresql+pg8000",
    username="postgres",
    password="oakhall139", 
    host="localhost",
    database="project1",
)

engine= create_engine(url_object)
