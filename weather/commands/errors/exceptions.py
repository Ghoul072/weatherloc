class WeatherBaseException(BaseException):
    """Base exception class from which all other exceptions are derived from"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        Base exception class from which all other exceptions are derived from

        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(*args)
        self.code = code
        self.message = message
        
    def __str__(self) -> str:
        """
        Return exception in string format

        :return: Text description of the exception with included error code
        :rtype: str
        """
        return f" Error {self.code}. {self.message}"
    
class MissingAPIKey(WeatherBaseException):
    """This exception is raised if API key is missing"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if API key is missing
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class LocationNotFound(WeatherBaseException):
    """This exception is raised if an invalid location is passed"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if an invalid location is passed
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class InvalidAPIKey(WeatherBaseException):
    """This exception is raised if provided API key is invalid"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if provided API key is invalid
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class LimitReached(WeatherBaseException):
    """This exception is raised if API Key has reached query limit"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if API Key has reached query limit
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class DisabledAPIKey(WeatherBaseException):
    """This exception is raised if provided API key is disabled"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if provided API key is disabled
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class PermissionDenied(WeatherBaseException):
    """This exception is raised if the API key does not have permission for a certain query"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if the API key does not have permission for a certain query
        
        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)
        
class InternalError(WeatherBaseException):
    """This exception is raised if there is an internal error in weatherapi server"""
    def __init__(self, code: int, message: str, *args: object) -> None:
        """
        This exception is raised if there is an internal error in weatherapi server

        :param code: Error code
        :type code: int
        :param message: Error message
        :type message: str
        """
        super().__init__(code, message, *args)