from database.database import SessionLocal

from database.db_models import AnalysisLog


def save_analysis_log(
    filename,
    accuracy,
    report_path
):

    db = SessionLocal()

    try:

        log = AnalysisLog(
            filename=filename,
            model_accuracy=accuracy,
            report_path=report_path
        )

        db.add(log)

        db.commit()

    finally:

        db.close()