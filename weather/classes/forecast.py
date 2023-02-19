from datetime import datetime as dt

from . import Current
from .subclasses import Location, Day, Astro, Hour


class ForecastDay:
    """
    Represents forecast for a single day
    """
    def __init__(self, data: dict) -> None:
        """
        Represents forecast for a single day

        :param data: Dict of data to be parsed
        :type data: dict
        """
        self.date = dt.strptime(data["date"], "%Y-%m-%d")
        self.date_epoch = data["date_epoch"]
        self.day = Day(data["day"])
        self.astro = Astro(data["astro"])
        self.hours = [Hour(hour) for hour in data["hour"]]


class Forecast:
    """
    Represents a forecast result
    """
    def __init__(self, data: dict) -> None:
        """
        Represents a forecast result

        :param data: Dict of data to be parsed. Must be a result from http://api.weatherapi.com/v1/forecast.json
        :type data: dict
        """
        
        self.location = Location(data["location"])
        self.current = Current(data["current"])
        
        forecast = data["forecast"]
        self.forecast = [ForecastDay(day) for day in forecast["forecastday"]]
        
        try:
            alerts = data["alerts"]
        except KeyError:
            self.alets = []
        else:
            self.alerts = alerts["alert"]