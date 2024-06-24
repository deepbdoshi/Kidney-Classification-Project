from kidney_disease_classifier import logger
from kidney_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f"####### {STAGE_NAME} has started #######")
#     objDITP = DataIngestionTrainingPipeline()
#     objDITP.main()
#     logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

# except Exception as e:
#     logger.exception(e)
#     raise e



STAGE_NAME = "Base Model Prep Stage"

try:
    logger.info(f"####### {STAGE_NAME} has started #######")
    objPBMTP = PrepareBaseModelTrainingPipeline()
    objPBMTP.main()
    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
except Exception as e:
    logger.exception(e)
    raise e