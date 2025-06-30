import json
import sys
import os

import pandas as pd

from pandas import DataFrame

from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import read_yaml_file
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.constants import SCHEMA_FILE_PATH

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        """
        :Param data_ingestion_artifact : Output refrance os data ingention artifact stage
        :param data_validation_config : configuration for data validation

        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        
        except Exception as e:
            raise MyException(e,sys)
        
    def validate_number_of_columns(self, dataframe: DataFrame) -> bool:
        """
        Method Name : validate_number_of_columns
        Description : This method validates number of columns

        output : returns bool value based on validation Results
        On Failure : Write an exception log and then raise an exception
        """
        try:
            status = len(dataframe.columns) == len(self._schema_config["columns"])
            logging.info(f"IS required column present : [{status}]")
            return status
        except Exception as e:
            raise MyException(e,sys)
        
    def is_column_exist(self, df: DataFrame) -> bool:
        """
        Method Name : is_column_exist
        Description : This method validates the existence of a numerical and categorical columns

        Output : Returns bool value based on validatiom results
        OnFailure : Write an exception log and then raise an exception
        """
        try:
            dataframe_columns = df.columns
            missing_numerical_columns = []
            missing_categorical_columns = []
            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    missing_numerical_columns.append(column)
            
            if len(missing_numerical_columns)>0:
                logging.info(f"Missing numerical column: {missing_numerical_columns}" )
            
            for column in self._schema_config["categorical_columns"]:
                if column not in dataframe_columns:
                    missing_categorical_columns.append(column)
            
            if len(missing_categorical_columns)>0:
                logging.info(f"Missing numerical column: {missing_categorical_columns}" )

            return False if len(missing_categorical_columns)>0 or len(missing_numerical_columns) else True
        except Exception as e:
            raise MyException(e,sys)

    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e,sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Method Name: Initiate_data_validation
        Description: this method start the data validation component of the pipeline 

        output: It returns the datavalidation booolen status
        On failure : Write an exception log and then raise an exception
        """

        try:
            validation_error_msg =""
            train_df,test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
                                DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))
            
            status = self.validate_number_of_columns(dataframe=train_df)
            if not status:
                validation_error_msg+= f"Columns are missing in trainign dataframe"
            else:
                logging.info(f"All require columns prensent in training dataframe : {status}")
            
            status = self.validate_number_of_columns(dataframe=test_df)
            if not status:
                validation_error_msg+= f"Columns are missing in test dataframe"
            else:
                logging.info(f"All require columns prensent in test dataframe : {status}")
            
            status = self.is_column_exist(df=train_df)
            if not status:
                validation_error_msg+= f"Columns are missing in trainign dataframe"
            else:
                logging.info(f"All Numeric and categorical columns prensent in training dataframe : {status}")
            
            status = self.is_column_exist(df=test_df)
            if not status:
                validation_error_msg+= f"Columns are missing in test dataframe"
            else:
                logging.info(f"All Numeric and categorical columns prensent in test dataframe : {status}")
            
            validation_status= len(validation_error_msg) == 0
            data_validation_artifact = DataValidationArtifact(validation_status=validation_status,
                                                              message=validation_error_msg,
                                                              validation_report_file_path=self.data_validation_config.validation_report_file_path
                                                              )
            report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(report_dir, exist_ok=True)
            validation_report ={
                "validation_status": validation_status,
                "message": validation_error_msg.strip()

            }

            with open(self.data_validation_config.validation_report_file_path,"w") as report_file:
                json.dump(validation_report, report_file, indent=4)
            
            logging.info(f"Data validtion artifact creatred and saved to JSON file.")
            logging.info(f"data validation artifact :{data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise MyException(e,sys) from e 


