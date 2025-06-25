
"""# below code is used to test the package
from src.logger import logging

logging.debug("This is a debug message") 
"""


#below code is to test the exception configuration

"""
from src.exception import MyException
import sys
try:
    a= 1+'z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e
"""

from src.pipline.training_pipeline import TrainPipeline
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion

#name = DataIngestion()
#print(name.data_ingestion_config.collection_name)
pipline = TrainPipeline()
pipline.run_pipeline()
