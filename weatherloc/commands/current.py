from datetime import datetime as dt

from .models import Condition, Location, AirQuality

class Current:
    """
    Represents an instance of current weather condition
    """
    def __init__(self, data: dict) -> None:
        """
        Represents an instance of current weather condition

        :param data: Dict of data to be parsed. Must be a result from http://api.weatherapi.com/v1/current.json
        :type data: dict
        """
        
        try:
            current = data["current"]
        except KeyError:
            current = data
        else:
            self.location = Location(data["location"])                              # :class:`~weather.commands.models.location.Location` object
        
        self.last_updated_epoch = current["last_updated_epoch"]                     #: Local time when the real time data was updated in unix time.
        self.last_updated = dt.strptime(current["last_updated"], "%Y-%m-%d %H:%M")  #: Local time when the real time data was updated.
        
        self.temp_c = current["temp_c"]                                             #: Temperature in celsius
        self.temp_f = current["temp_f"]                                             #: Temperature in fahrenheit
        
        self.is_day = bool(current["is_day"])                                       #: Whether the current condition is day or night. True if day
        self.condition = Condition(current["condition"])                            #: :class:`~weather.commands.models.condition.Condition` object
        
        self.wind_mph = current["wind_mph"]                                         #: Wind speed in miles per hour
        self.wind_kph = current["wind_kph"]                                         #: Wind speed in kilometer per hour
        self.wind_degree = current["wind_degree"]                                   #: Wind direction in degrees
        self.wind_direction = current["wind_dir"]                                   #: Wind direction as 16 point compass
        
        self.pressure_mb = current["pressure_mb"]                                   #: Pressure in millibars
        self.pressure_in = current["pressure_in"]                                   #: Pressure in inches
        
        self.precip_mm = current["precip_mm"]                                       #: Precipitation amount in millimeters
        self.precip_in = current["precip_in"]                                       #: Precipitation amount in inches
        
        self.humidity = current["humidity"] / 100                                   #: Humidity as a decimal (0-1 scale)
        self.cloud = bool(current["cloud"]) / 100                                   #: Cloud cover as a decimal (0-1 scale)
        
        self.feelslike_c = current["feelslike_c"]                                   #: Feels like temperature in celsius
        self.feelslike_f = current["feelslike_f"]                                   #: Feels like temperature in fahrenheit
        
        self.visibility_km = current["vis_km"]                                      #: Visibility in kilometer
        self.visibility_miles = current["vis_miles"]                                #: Visibility in miles
        
        self.uv = current["uv"]                                                     #: UV Index
        
        self.gust_mph = current["gust_mph"]                                         #: Wind gust in miles per hour
        self.gust_kph = current["gust_kph"]                                         #: Wind gust in kilometer per hour
        
        try:
            aqi = current["air_quality"]
        except KeyError:
            self.air_quality = None
        else:
            self.air_quality = AirQuality(aqi)                                      #: :class:`~weather.commands.models.aqi.AirQuality` object
        