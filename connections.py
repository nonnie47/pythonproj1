from sqlalchemy import URL, create_engine
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

url_object = URL.create(
    "postgresql+pg8000",
    username=(os.getenv("acc_user")),
    password=(os.getenv("acc_password")), 
    host=(os.getenv("acc_host")),
    database=(os.getenv("acc_name")),
)

engine= create_engine(url_object)
