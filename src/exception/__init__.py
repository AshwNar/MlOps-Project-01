import sys
import logging 

def error_message_detail(error:Exception, error_detail:sys) -> str:
    """
    Returns a detailed error message.
    
    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module for accessing the exception traceback.
        
    Returns:
        str: A formatted error message with the exception type, value, and traceback.
    """
    _, _, exc_tb = error_detail.exc_info() #extract the error details
    # Get the file name and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    #
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] \nError message: [{str(error)}]"
    logging.error(error_message)  # Log the error message
    # Return the error message  
    return error_message

class MyException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    
    This class is used to raise exceptions with detailed error messages.
    """
    def __init__(self, error_message:Exception, error_detail:sys):
        """
        Initializes the MyException instance with a detailed error message.
        
        Args:
            error_message (Exception): The exception object containing the error message.
            error_detail (sys): The sys module for accessing the exception traceback.
        """
        super().__init__(error_message)  # Call the base class constructor with the detailed error message  
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the MyException instance.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message
        