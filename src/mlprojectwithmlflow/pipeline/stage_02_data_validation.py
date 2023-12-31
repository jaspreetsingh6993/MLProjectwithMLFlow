from mlprojectwithmlflow.config.configuration import ConfigurationManager
from mlprojectwithmlflow.components.data_validation import DataValidation
from mlprojectwithmlflow import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config =  data_validation_config)
        data_validation.validate_all_columns()
    

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
        data_validation_obj = DataValidationTrainingPipeline()
        data_validation_obj.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise(e)
