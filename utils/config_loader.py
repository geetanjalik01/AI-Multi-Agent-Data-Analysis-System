from dotenv import load_dotenv
import os

load_dotenv()

def get_config():

    return {

        "groq_model": os.getenv(
            "OPENAI_MODEL_NAME"
        ),

        "database_url": os.getenv(
            "DATABASE_URL"
        )
    }