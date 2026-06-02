from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def init_db():

    with engine.connect() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS runs (

            id SERIAL PRIMARY KEY,

            dataset_name TEXT,

            start_timestamp TEXT,

            agent_trace TEXT,

            report_path TEXT
        )
        """))

        conn.commit()

def log_run(
    dataset_name,
    trace,
    report_path
):

    with engine.connect() as conn:

        conn.execute(text("""
        INSERT INTO runs (
            dataset_name,
            start_timestamp,
            agent_trace,
            report_path
        )

        VALUES (
            :dataset_name,
            NOW(),
            :agent_trace,
            :report_path
        )
        """), {

            "dataset_name": dataset_name,
            "agent_trace": trace,
            "report_path": report_path
        })

        conn.commit()