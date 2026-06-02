from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def save_dataframe(df, table_name):
    df.to_sql(table_name, engine, if_exists="replace", index=False)