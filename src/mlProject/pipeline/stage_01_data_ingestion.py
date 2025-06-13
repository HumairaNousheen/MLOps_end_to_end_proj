from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        #self.data_ingestion_config = self.config.get_data_ingestion_config()
        #self.data_ingestion = DataIngestion(self.data_ingestion_config)

    def main(self):
         config = ConfigurationManager()
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion = DataIngestion(config=data_ingestion_config)
         data_ingestion.download_file()
         data_ingestion.extract_zip_file()                                                                                 

# This code is part of a data ingestion pipeline for a machine learning project.
# It handles downloading, unzipping, and splitting data into training and testing sets.
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e