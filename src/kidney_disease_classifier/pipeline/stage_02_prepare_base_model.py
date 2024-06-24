from kidney_disease_classifier.config.configuration import ConfigurationManager
from kidney_disease_classifier.components.prepare_base_model import PrepareBaseModel
from kidney_disease_classifier import logger


STAGE_NAME = "Base Model Prep Stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


    
if __name__ == '__main__':
    try:
        logger.info(f"####### {STAGE_NAME} has started #######")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
    except Exception as e:
        logger.exception(e)
        raise e