from mlprojectwithmlflow import logger
from mlprojectwithmlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlprojectwithmlflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlprojectwithmlflow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlprojectwithmlflow.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlprojectwithmlflow.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_ingestion_obj=DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise(e)


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_validation_obj = DataValidationTrainingPipeline()
    data_validation_obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise(e)


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_transformation_obj = DataTransformationTrainingPipeline()
    data_transformation_obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise(e)


STAGE_NAME="Model Trainer stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    model_trainer_obj=ModelTrainerTrainingPipeline()
    model_trainer_obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    model_evaluation_obj=ModelEvaluationTrainingPipeline()
    model_evaluation_obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    

