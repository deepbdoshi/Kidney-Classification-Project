from kidney_disease_classifier import logger
# from kidney_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidney_disease_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from kidney_disease_classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

# 1st Stage
# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f"####### {STAGE_NAME} has started #######")
#     objDITP = DataIngestionTrainingPipeline()
#     objDITP.main()
#     logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

# except Exception as e:
#     logger.exception(e)
#     raise e


# 2nd Stage
# STAGE_NAME = "Base Model Prep Stage"

# try:
#     logger.info(f"####### {STAGE_NAME} has started #######")
#     objPBMTP = PrepareBaseModelTrainingPipeline()
#     objPBMTP.main()
#     logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
# except Exception as e:
#     logger.exception(e)
#     raise e


# 3rd Stage
# STAGE_NAME = "Model Training Stage"

# try:
#     logger.info(f"####### {STAGE_NAME} has started #######")
#     objMTP = ModelTrainingPipeline()
#     objMTP.main()
#     logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
# except Exception as e:
#     logger.exception(e)
#     raise e

# 4th Stage
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"####### {STAGE_NAME} has started #######")
    objEP = EvaluationPipeline()
    objEP.main()
    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

except Exception as e:
    logger.exception(e)
    raise e