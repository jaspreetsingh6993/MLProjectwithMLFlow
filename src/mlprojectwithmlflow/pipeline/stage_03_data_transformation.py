from mlprojectwithmlflow.config.configuration import ConfigurationManager
from mlprojectwithmlflow.components.data_transformation import DataTransformation
from mlprojectwithmlflow import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation= DataTransformation(config = data_transformation_config)
        data_transformation.train_test_spliting()
            

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise(e)
