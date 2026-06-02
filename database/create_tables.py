from database.database import engine

from database.db_models import Base

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")