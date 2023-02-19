import requests

from .classes import Current, Forecast


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
        
        :return: An instance of class `weather.modules.current.Current` which represents current weater condition
        :rtype: Current
        """
        aqi = "yes"  if aqi else "no"
        data = requests.get(f"{self.__baseuri}current.json?key={self.__secret}&q={query}&aqi={aqi}").json()
        return Current(data)

    def forecast(self, query: str, days: int = 1, aqi: bool = False, alerts: bool = False):
        aqi = "yes"  if aqi else "no"
        alerts = "yes"  if alerts else "no"
        data = requests.get(f"{self.__baseuri}forecast.json?key={self.__secret}&query={query}&days={days}&aqi={aqi}&alerts={alerts}").json()
        return Forecast(data)
        