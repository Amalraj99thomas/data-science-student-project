#To view errors and exceptions
import sys
from src.studperform.logging.logger import logger

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in script name [{0}], line number [{1}], error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
#Inherits the Exception class

class CustomException(Exception):
    #Constructer Method. Then it can be used as a class.

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

#Try-catch block to check for errors if any.

if __name__=="__main__":

    try:
        a = 1/0
    except Exception as error:
        logger.info("Houston, we have a interesting problem")
        raise CustomException(error, sys)