""" Custom Error types for RX Gemini"""


class MissingConfigError(Exception):
    """
    Missing Configuration file in working directory
    """

    def __init__(self):
        self.message = "Configuration file not found/missing."
        super().__init__(self.message)


class ScopeGetterException(Exception):
    """
    Custom exception for fetching stack trace.

    Args:
        Exception (class): Base Class for Exceptions
    """

    def __init__(self):
        self.message = "Scope Getter"
        super().__init__(self.message)
