# this is also fine--->from src.mlProject import logger
# just because you have a cinstructer file init, python recognizes 
from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME= "Data Ingestion stage"
try:
    logger.info(">>>>>> stage 01: Data Ingestion started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>>> stage 01: Data Ingestion completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


