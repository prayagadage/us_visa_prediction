import sys 
import os

def Us_VisaException(error_message:Exception, error_detail:sys)->None:
    """
    Custom Exception class for US Visa Prediction Project

    error_message : Exception : Exception object
    error_detail : sys : system object

    """
    _,_,tb=error_detail.exc_info()
    filename=tb.tb_frame.f_code.co_filename
    line_number=tb.tb_lineno
    error_message=f"Error occured in script : {filename} at line number : {line_number} error message : {str(error_message)}"
    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = Us_VisaException(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

        