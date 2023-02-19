import requests

from .classes import Current, Forecast, autocomplete
from .classes.subclasses import Location


class Client:
    """
    Class representing a weather API client
    
    :param secret: API secret key. Get yours at https://www.weatherapi.com/my/
    :type id: str
    """
    def __init__(self, secret: str) -> None:
        """
        Constructor method
        
        :param secret: API secret key. Get yours at https://www.weatherapi.com/my/
        :type id: str
        """
        self.__secret = secret                              #: API secret ket
        self.__baseuri = "http://api.weatherapi.com/v1/"    #: Base URL for the API
        
    def current(self, query: str, aqi: bool = False) -> Current:
        """
        Request current weather

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        
        :param aqi: Include air quality data, defaults to False
        :type aqi: bool, optional
        
        :return: An instance of Current
        :rtype: Current
        """
        aqi = "yes"  if aqi else "no"
        data = requests.get(f"{self.__baseuri}current.json?key={self.__secret}&q={query}&aqi={aqi}").json()
        return Current(data)

    def forecast(self, query: str, days: int = 1, aqi: bool = False, alerts: bool = False) -> Forecast:
        """
        Request weather forecast

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param days: Number of days to fetch forecast for, defaults to 1
        :type days: int, optional
        :param aqi: Include air quality data, defaults to False
        :type aqi: bool, optional
        :param alerts: Include alerts, defaults to False
        :type alerts: bool, optional
        :return: An instance of Forecast
        :rtype: Forecast
        """
        aqi = "yes"  if aqi else "no"
        alerts = "yes"  if alerts else "no"
        data = requests.get(f"{self.__baseuri}forecast.json?key={self.__secret}&query={query}&days={days}&aqi={aqi}&alerts={alerts}").json()
        return Forecast(data)
    
    def search(self, query: str) -> list[Location]:
        """
        Searches for a given location

        :param query: Location or IP address to search for
        :type query: str
        :return: list of Location objects
        :rtype: list[Location]
        """
        data = requests.get(f"{self.__baseuri}search.json?key={self.__secret}&query={query}").json()
        return autocomplete(data)
        