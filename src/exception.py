import sys  # Import the sys module to access system-specific parameters and functions

# Function to extract and format detailed error message
def error_message_detail(error, error_detail: sys):
    # Extracts the traceback object from the exception details
    _, _, exc_tb = error_detail.exc_info()

    # Gets the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Constructs the error message with the script name, line number, and error message
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Returns the constructed error message
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Generate a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.error_message
 

