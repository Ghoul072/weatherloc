import math

# from modules import current

class Client:
    """
    Class represending a weather API client
    """
    def __init__(self, id: str) -> None:
        self.id = id
        self.baseuri = "http://api.weatherapi.com/v1/"
        
    def current(self, query: str, aqi: bool = False):
        pass
