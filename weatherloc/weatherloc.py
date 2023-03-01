import requests
from datetime import date
from datetime import datetime as dt

from .commands import Current, Forecast, Astronomy, Sports, LookupIP, autocomplete
from .commands.models import Location

from .commands import errors


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
        
    def __send_get_request(self, url: str) -> dict:
        """
        Send a get request and retrieve json data. Checks if returned data is an error before passing back
        

        :param url: url to send get request to
        :type url: str
        
        :raises errors.MissingAPIKey: If API key is not provided
        :raises errors.LocationNotFound: If an unrecognised location is passed
        :raises errors.InvalidAPIKey: If an invalid API key is provided
        :raises errors.LimitReached: If API key has reached query limit
        :raises errors.DisabledAPIKey: If API key is disabled
        :raises errors.PermissionDenied: If API key lacks the permissions for a command
        :raises errors.InternalError: If there is an internal error in weatherapi server
        :raises ValueError: Handle for all unrecognised errors
        
        :return: json data received from get request
        :rtype: dict
        """
        data = requests.get(url).json()
        try:
            error = data["error"]
        except KeyError:
            return data
        else:
            code = error["code"]
            message = error["message"]
            match code:
                case 1002:
                    raise errors.MissingAPIKey(code, message)
                case 1006:
                    raise errors.LocationNotFound(code, message)
                case 2006:
                    raise errors.InvalidAPIKey(code, message)
                case 2007:
                    raise errors.LimitReached(code, message)
                case 2008:
                    raise errors.DisabledAPIKey(code, message)
                case 2009:
                    raise errors.PermissionDenied(code, message)
                case 9999:
                    raise errors.InternalError(code, message)
                case other:
                    raise ValueError(f"Error {code}. {message}")
                                
    def current(self, query: str, aqi: bool = False) -> Current:
        """
        Request current weather

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        
        :param aqi: Include air quality data, defaults to False
        :type aqi: bool, optional
        
        :return: An instance of :class:`~weather.commands.current.Current`
        :rtype: Current
        """
        aqi = "yes"  if aqi else "no"
        data = self.__send_get_request(f"{self.__baseuri}current.json?key={self.__secret}&q={query}&aqi={aqi}")
        return Current(data)

    #ToDo: Add alerts
    """
    :param alerts: Include alerts, defaults to False
    :type alerts: bool, optional
    """
    def forecast(self, query: str, days: int = 1, aqi: bool = False, alerts: bool = False) -> Forecast:
        """
        Request weather forecast

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param days: Number of days to fetch forecast for, defaults to 1
        :type days: int, optional
        :param aqi: Include air quality data, defaults to False
        :type aqi: bool, optional
        :return: An instance of :class:`~weather.commands.forecast.Forecast`
        :rtype: Forecast
        """
        aqi = "yes"  if aqi else "no"
        alerts = "yes"  if alerts else "no"
        data = self.__send_get_request(f"{self.__baseuri}forecast.json?key={self.__secret}&query={query}&days={days}&aqi={aqi}&alerts={alerts}")
        return Forecast(data)
    
    def search(self, query: str) -> list[Location]:
        """
        Searches for a given location

        :param query: Location or IP address to search for
        :type query: str
        :return: list of :class:`~weather.commands.models.location.Location` objects
        :rtype: list[Location]
        """
        data = self.__send_get_request(f"{self.__baseuri}search.json?key={self.__secret}&query={query}")
        return autocomplete(data)
    
    def future(self, query: str, day: str | date) -> Forecast:
        """
        Checked predicted weather in a future date, max 300 days from now

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param day: Any date upto 300 days in the future. Encouraged formats DD-MM-YYY and YYYY-MM-DD. Other formats may yield unexpected results
        :type day: str | date
        :raises ValueError: If date provided in an unrecognised format or day is more than 300 days from now
        :return: An instance of :class:`~weather.commands.forecast.Forecast`
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
        data = self.__send_get_request(f"{self.__baseuri}future.json?key={self.__secret}&query={query}&dt={day}")
        return Forecast(data)
    
    def astronomy(self, query: str, day: str | date = dt.now().date()) -> Astronomy:
        """
        Get up-to-date information for sunrise, sunset, moonrise, moonset, and moon phase

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :param day: Any date upto 300 days in the future. Encouraged formats DD-MM-YYY and YYYY-MM-DD. Other formats may yield unexpected results. Defaults to current date
        :type day: str | date, optional
        :raises ValueError: If date provided in an unrecognised format
        :return: An instance of :class:`~weather.commands.astronomy.Astronomy`
        :rtype: Astronomy
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
        data = self.__send_get_request(f"{self.__baseuri}astronomy.json?key={self.__secret}&query={query}&dt={day}")
        return Astronomy(data)
    
    def timezone(self, query: str) -> Location:
        """
        Check location and timezone

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :return: An instance of :class:`~weather.commands.models.location.Location`
        :rtype: Location
        """
        data = self.__send_get_request(f"{self.__baseuri}timezone.json?key={self.__secret}&query={query}")
        return Location(data["location"])
    
    def sports(self, query: str) -> Sports:
        """
        Get listing of all upcoming sports events for football, cricket and golf.

        :param query: Query parameter. Allowed types: (Latitude and Longitude, City/Country name, US Zip code, UK Postcode, Canada Postal Code, Metar Code, Iata 3 digit airport code, IP address)
        :type query: str
        :return: An instance of :class:`~weather.commands.sports.Sports`
        :rtype: Sports
        """
        data = self.__send_get_request(f"{self.__baseuri}sports.json?key={self.__secret}&query={query}")
        return Sports(data)
    
    def ip_lookup(self, ip_addr: str) -> LookupIP:
        """
        Get up-to-date information for an IP address

        :param ip_addr: IP Address
        :type ip_addr: str
        :return: An instance of :class:`~weather.commands.ip_lookup.LookupIP`
        :rtype: LookupIP
        """
        data = self.__send_get_request(f"{self.__baseuri}ip.json?key={self.__secret}&q={ip_addr}")
        return LookupIP(data)
