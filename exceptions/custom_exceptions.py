class AppException(Exception):
    """Base class for all custom application exceptions."""

    def __init__(self, message: str, original_exception: Exception | None = None):
        super().__init__(message)
        self.message = message
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.message} (caused by {self.original_exception.__str__()})"
        return self.message


class DatabaseException(AppException):
    """Exception raised for database access errors."""

    def __init__(self, message: str, original_exception: Exception | None = None):
        super().__init__(message)
        self.original_exception = original_exception
