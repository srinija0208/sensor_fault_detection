import sys
import os


def error_message_details(error,error_detail:sys):


    _,_,exc_tb = error_detail.exc_info()   ## exc_info returns 3 things error line no., message and file name
    file_name = exc_tb.tb_frame.f_code.co_filename   ## filename where error has occured

    error_message = "error occured and file name is [{0}] and the linenumber is [{1}] and the error is [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))


    return error_message



class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys): ## find line no.of error,error message and error file using sys

        super().__init__(error_message)

        self.error_message = error_message_details(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message  ## to return the error in str 