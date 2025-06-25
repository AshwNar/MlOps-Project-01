import os 
from datetime import date

DATABASE_NAME = "Ml-Pro1"
COLLECTION_NAME = "Pro1-Data"
MONGODB_URL_KEY = "MONGODB_URL"
#DB_NAME = "Ml-Pro1"
#COLLECTION_NAME = "Pro1-Data"


PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"
MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "Responce"
CURRENT_YEAR = date.today().year

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"


FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_NAME: str = os.path.join("config","schema.yaml")

"""
Data Ingestion related constants"""
DATA_INGESTION_COLLECTION_NAME: str = "Pro1-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

"""Data Validation related constants"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"