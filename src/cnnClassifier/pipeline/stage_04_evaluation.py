from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger
from cnnClassifier.components.Evaluation import Evaluation


STAGE_NAME = 'Evaluation'


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evalu = Evaluation(val_config)
        evalu.evaluation()
        evalu.save_score()

if __name__ == "__main__":
    try:
        logger.info("*************************************")
        logger.info(f"-------------stage:-- {STAGE_NAME}-----------------")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"--------------stage {STAGE_NAME} completed successsfully")

    except Exception as e:
        logger.exception(e)
        raise e