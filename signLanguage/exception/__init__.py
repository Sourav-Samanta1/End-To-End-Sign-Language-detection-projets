##This code for where exception/error is raised
import sys

def error_message_detail(error, error_detail: sys):
    # Extracts exception information: type, value, traceback
    _, _, exc_tb = error_detail.exc_info()

    # Gets the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Creates a detailed error message including the script name, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

# Custom exception class for handling errors with detailed information
class SignException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: Error message in string format
        :param error_detail: Contains detailed info about the error, including traceback
        """
        super().__init__(error_message)  # Calls the base class constructor with the error message

        # Generates detailed error message using the error_message_detail function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Returns the detailed error message when the exception is printed
        return self.error_message
