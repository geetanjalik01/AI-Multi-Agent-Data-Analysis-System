from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AnalysisLog(Base):

    __tablename__ = "analysis_logs"

    id = Column(Integer, primary_key=True)

    filename = Column(String)

    model_accuracy = Column(Float)

    report_path = Column(String)