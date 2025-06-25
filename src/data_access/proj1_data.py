import sys 
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import MyException
from src.constants import DATABASE_NAME


class Proj1Data:
    """
    Proj1Data is a record as a pandas Datafrem.
    class that provides methods to interact with the MongoDB database for the project.
    
    Attributes:
    ______
    client : MongoDBClient
        The MongoDB client instance for the class.
        
    database : Database
        The database instance for the class that connects to MongoDBClient.
        
    Methods:
    _______
    __init__(database_name: str) -> None:
        Initializes the Proj1Data with the specified database name.
        
    get_data_as_dataframe() -> pd.DataFrame:
        Retrieves data from the MongoDB collection and returns it as a pandas DataFrame.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Proj1Data with the specified database name.
        
        Raises:
            MyException: If there is an error connecting to the MongoDB database.
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)
    
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
        """
        Retrieves data from the specified MongoDB collection and returns it as a pandas DataFrame.
        
        Args:
            collection_name (str): The name of the collection to retrieve data from.
            database_name (Optional[str]): The name of the database to connect to. Defaults to None.
            
        Returns:
            pd.DataFrame: A pandas DataFrame containing the data from the specified collection.
            
        Raises:
            MyException: If there is an error retrieving data from the MongoDB collection.
        """
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            # Convert colllection data to dataFrame and preprocess.
            print("Fatiching data from MonoDB")
            df = pd.DataFrame(list(collection.find()))
            print("Data fetched successfully length of data is: ", len(df))

            
            # Drop the '_id' column if it exists and replace 'na' with np.nan
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)