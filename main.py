from cnnClassifier import logger
from cnnClassifier.pipeline .stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline


STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==============x")

    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME2 = "Prepare Base Model"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME2} started <<<<<<<")
        data_ingestion = PrepareBaseModelTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> stage {STAGE_NAME2} completed <<<<<<<<<\n\nx==============x")

    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME3 = "Training"

if __name__ == "__main__":
    try:
        logger.info(f"-------------------stage {STAGE_NAME3} started ---------------")
        training = TrainingPipeline()
        training.main()
        logger.info(f"-----------stage {STAGE_NAME3} completed successfully ---------<<\n\n----")
    except Exception as e:
        logger.exception(e)
        raise e