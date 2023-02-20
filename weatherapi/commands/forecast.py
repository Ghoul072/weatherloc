from datetime import datetime as dt

from . import Current
from .models import Location, Day, Astro, Hour


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
        self.date = dt.strptime(data["date"], "%Y-%m-%d")   #: Forecast date
        self.date_epoch = data["date_epoch"]                #: Forecast date as unix time
        self.day = Day(data["day"])                         #: Instance of :class:`~weather.commands.models.day.Day`
        self.astro = Astro(data["astro"])                   #: Instance of :class:`~weather.commands.models.astro.Astro`
        self.hours = [Hour(hour) for hour in data["hour"]]  #: Instance of :class:`~weather.commands.models.hour.Hour`


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
        self.location = Location(data["location"])                              #: :class:`~weather.commands.models.location.Location` object
        
        try:
            current = data["current"]
        except KeyError:
            pass
        else:
            self.current = Current(current)                                     #: Current weather. Instance of :class:`~weather.commands.current.Current` object
        
        forecast = data["forecast"]
        self.forecast = [ForecastDay(day) for day in forecast["forecastday"]]   #: List of :class:`~weather.commands.forecast.ForecastDay` objects. Each represents weather forecast for a single day
        
        # ToDo: Create Alert class and update. If this is uploaded now, migrating to new version will be difficult
        # try:
        #     alerts = data["alerts"]
        # except KeyError:
        #     self.alets = []
        # else:
        #     #self.alerts = alerts["alert"]                                       #: List of alert dicts. To be migrated to a python class in next version