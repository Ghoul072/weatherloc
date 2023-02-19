import json
from datetime import datetime as dt

from .subclasses import Condition, Location

class Current:
    """
    Class representing an instance of current weather condition
    """
    def __init__(self, data: dict) -> None:
        """
        Class representing an instance of current weather condition

        :param data: Dict of data to be parsed. Must be a result from http://api.weatherapi.com/v1/current.json
        :type data: dict
        """
        
        current = data["current"]
        
        self.location = Location(data["location"])
        
        self.last_updated_epoch = current["last_updated_epoch"]
        self.last_updated = dt.strptime(current["last_updated"], "%Y-%m-%d %H:%M")
        
        self.temp_c = current["temp_c"]
        self.temp_f = current["temp_f"]
        
        self.is_day = bool(current["is_day"])
        self.condition = Condition(current["condition"])
        
        self.wind_mph = current["wind_mph"]
        self.wind_kph = current["wind_kph"]
        self.wind_degree = current["wind_degree"]
        self.wind_direction = current["wind_dir"]
        
        self.pressure_mb = current["pressure_mb"]
        self.pressure_in = current["pressure_in"]
        
        self.precip_mm = current["precip_mm"]
        self.precip_in = current["precip_in"]
        
        self.humidity = current["humidity"]
        self.cloud = bool(current["cloud"])
        
        self.feelslike_c = current["feelslike_c"]
        self.feelslike_f = current["feelslike_f"]
        
        self.visibility_km = current["vis_km"]
        self.visibility_miles = current["vis_miles"]
        
        self.uv = current["uv"]
        
        self.gust_mph = current["gust_mph"]
        self.gust_kph = current["gust_kph"]
        
        