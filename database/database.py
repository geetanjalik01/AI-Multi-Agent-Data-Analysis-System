from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os

# ---------------------------------------------------
# LOAD ENV VARIABLES
# ---------------------------------------------------

load_dotenv()

# ---------------------------------------------------
# DATABASE URL
# ---------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

# ---------------------------------------------------
# CREATE DATABASE ENGINE
# ---------------------------------------------------

engine = create_engine(DATABASE_URL)

# ---------------------------------------------------
# CREATE DATABASE SESSION
# ---------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)