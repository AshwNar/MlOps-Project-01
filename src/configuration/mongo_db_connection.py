import os 
import sys
import certifi
import pymongo

from src.exception import MyException
from src.logger import logging
from src.constants import MONGODB_URL_KEY, DATABASE_NAME

# Load the certificate authority file to avoid timeout errors  when connection to MongoDB Atlas
ca = certifi.where()


class MongoDBClient:
    """
    MongoDBClient is a class that provides methods to connect to a MongoDB database and perform operations on it.
    
    Attributes:
    ______
    client : MongodbClient
        The manodb client instance. for the class
        
    database : Database
        The database instance for the class that connnect to Mangodbcliet.
        
    Methods:
    _______
    __init__(database_name: str)--> none:
        Initializes the MongoDBClient with the specified database name.
    """
    client = None 

    def __init__(self, database_name: str = DATABASE_NAME)-> None:  
        """
        Initializes the MongoDBClient with the specified database name. IF the database connetiopn is found , it estabblishes a connection to the MongoDB database using the URL from environment variables.
        
        Args:
            database_name (str): The name of the database to connect to. Defaults to DATABASE_NAME.

        Raises:
            MyException: If the MongoDB URL is not set in the environment variables or if there
        """
        try:
            # Check idf the MongoDB client is already initialized; if not create a new client\
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # Get the MongoDB URL from environment variables
                if mongo_db_url is None:
                    raise MyException(f"Environment variable '{MONGODB_URL_KEY}' is not set.", sys)
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            # Create a MongoDB client
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Connected to MongoDB database: {database_name}")
        except Exception as e:
            raise MyException(e, sys)