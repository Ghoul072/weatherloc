from datetime import datetime as dt

from . import Condition

class Hour:
    """Represents weather condition for a single hour"""
    def __init__(self, data: dict) -> None:
        """
        Represents weather condition for a single hour

        :param data: Dict of data to be parsed
        :type data: dict
        """
        
        self.time_epoch = data["time_epoch"]
        self.time = dt.strptime(data["time"], "%Y-%m-%d %H:%M")
        
        self.temp_c = data["temp_c"]
        self.temp_f = data["temp_f"]
        
        self.wind_mph = data["wind_mph"]
        self.wind_kph = data["wind_kph"]
        self.wind_degree = data["wind_degree"]
        self.wind_direction = data["wind_dir"]
        
        self.pressure_mb = data["pressure_mb"]
        self.pressure_in = data["pressure_in"]
        
        self.precip_mm = data["precip_mm"]
        self.precip_in = data["precip_in"]
        
        self.humidity = data["humidity"]
        self.cloud = bool(data["cloud"])
        
        self.feelslike_c = data["feelslike_c"]
        self.feelslike_f = data["feelslike_f"]
        
        self.windchill_c = data["windchill_c"]
        self.windchill_f = data["windchill_f"]
        self.heatindex_c = data["heatindex_c"]
        self.heatindex_f = data["heatindex_f"]
        self.dewpoint_c = data["dewpoint_c"]
        self.dewpoint_f = data["dewpoint_f"]
        
        self.will_it_rain = bool(data["will_it_rain"])
        self.chance_of_rain = data["chance_of_rain"]/100
        self.will_it_snow = bool(data["will_it_snow"])
        self.chance_of_snow = data["chance_of_snow"]/100
        
        self.visibility_km = data["vis_km"]
        self.visibility_miles = data["vis_miles"]
        
        self.uv = data["uv"]
        
        self.gust_mph = data["gust_mph"]
        self.gust_kph = data["gust_kph"]