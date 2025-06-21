# below code is used to test the package
from src.logger import logging

logging.debug("This is a debug message") 



#below code is to test the exception configuration
from src.exception import MyException
import sys
try:
    a= 1+'z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e