class Errors(Exception):
    """Base class for exceptions in this module."""
    pass


class UnknownCellType(Errors):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression:"Entity", message:str=None):
        if message == None:
            message = f"Unknown entity type {expression} found."
        self.expression = expression
        self.message = message
        super().__init__(message)