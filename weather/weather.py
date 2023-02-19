import requests
from datetime import date
from datetime import datetime as dt

from .classes import Current, Forecast, Astronomy, autocomplete
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
    
    def future(self, query: str, day: str | date) -> Forecast:
        """
        Checked predicted weather in a future date, max 300 days from now

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param day: Any date upto 300 days in the future. Encouraged formats DD-MM-YYY and YYYY-MM-DD. Other formats may yield unexpected results
        :type day: str | date
        :raises ValueError: If date provided in an unrecognised format or day is more than 300 days from now
        :return: An instance of Forecast
        :rtype: Forecast
        """
        if type(day) == str:
            formats = ("%d-%m-%Y", "%Y-%m-%d", "%m-%d-%Y", "%Y-%d-%m")
            for format in formats:
                try:
                    day = dt.strptime(day, format)
                except:
                    pass
                else:
                    break
            else:
                raise ValueError("Day must be in format YYYY-MM-DD or provided as a `datetime.date` object")
        day = day.strftime("%Y-%m-%d")
        data = requests.get(f"{self.__baseuri}future.json?key={self.__secret}&query={query}&dt={day}").json()
        return Forecast(data)
    
    def astronomy(self, query: str, day: str | date) -> Astronomy:
        """
        Get up-to-date information for sunrise, sunset, moonrise, moonset, and moon phase

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param day: Any date upto 300 days in the future. Encouraged formats DD-MM-YYY and YYYY-MM-DD. Other formats may yield unexpected results
        :type day: str | date
        :raises ValueError: If date provided in an unrecognised format
        :return: An instance of Forecast
        :rtype: Forecast
        """
        if type(day) == str:
            formats = ("%d-%m-%Y", "%Y-%m-%d", "%m-%d-%Y", "%Y-%d-%m")
            for format in formats:
                try:
                    day = dt.strptime(day, format)
                except:
                    pass
                else:
                    break
            else:
                raise ValueError("Day must be in format YYYY-MM-DD or provided as a `datetime.date` object")
        day = day.strftime("%Y-%m-%d")
        data = requests.get(f"{self.__baseuri}astronomy.json?key={self.__secret}&query={query}&dt={day}").json()
        return Astronomy(data)
