import sys
from dsproject.logger import logging

# Function to extract detailed information about the exception
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
     # exc_info() returns a tuple of:exception_type, exception_value, traceback)
    file_name=exc_tb.tb_frame.f_code.co_filename
    # Get the filename where the exception happened
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
 # message containing: the script name, line no, and real exception message  
    return error_message

    

class CustomException(Exception):# Custom exception class
    def __init__(self,error_message,error_detail:sys): 
        # error_message -> Original exception and 
        # error_detail -> 'sys' module used to access traceback info
        super().__init__(error_message)# Initialize the parent Exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        # formatted error message with file name and line number
    
    def __str__(self):# Defines what gets printed when the exception object is printed
        return self.error_message
    


    
