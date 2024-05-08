from flask import config
from mlproject.components import data_ingestion
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_ingestion import DataIngestion
from mlproject import logger

STAGE_NAME = "DatA Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
       config = ConfigurationManager()

       data_ingestion_config = config.get_data_ingestion_config()
       data_ingestion = DataIngestion(data_ingestion_config)
       data_ingestion.download_file()
       data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME} completed successfully!")
    except Exception as e:
        logger.exception(e)