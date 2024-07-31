from kidney_disease_classifier.config.configuration import ConfigurationManager
from kidney_disease_classifier.components.model_evaluation_mlflow import Evaluation
from kidney_disease_classifier import logger

STAGE_NAME = "Model Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"####### {STAGE_NAME} has started #######")
        objEP = EvaluationPipeline()
        objEP.main()
        logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

    except Exception as e:
        logger.exception(e)
        raise e