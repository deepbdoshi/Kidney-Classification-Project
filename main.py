from kidney_disease_classifier import logger
from kidney_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"####### {STAGE_NAME} has started #######")
    objDITP = DataIngestionTrainingPipeline()
    objDITP.main()
    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

except Exception as e:
    logger.exception(e)
    raise e
