from . import Condition, AirQuality

class Day:
    """
    Represents weather condition for a single day
    """
    def __init__(self, data: dict) -> None:
        """
        Represents weather condition of a single day

        :param data: Dict of data to be parsed
        :type data: dict
        """
        
        self.maxtemp_c = data["maxtemp_c"]
        self.maxtemp_f = data["maxtemp_f"]
        self.mintemp_c = data["mintemp_c"]
        self.mintemp_f = data["mintemp_f"]
        self.avgtemp_c = data["avgtemp_c"]
        self.avgtemp_f = data["avgtemp_f"]
        
        self.maxwind_mph = data["maxwind_mph"]
        self.maxwind_kph = data["maxwind_kph"]
        
        self.totalprecip_mm = data["totalprecip_mm"]
        self.totalprecip_in = data["totalprecip_in"]
        self.totalsnow_cm = data["totalsnow_cm"]
        
        self.avgvisibility_km = data["avgvis_km"]
        self.avgvisibility_miles = data["avgvis_miles"]
        self.avghumidity = data["avghumidity"]
        
        self.will_it_rain = bool(data["daily_will_it_rain"])
        self.chance_of_rain = data["daily_chance_of_rain"]/100
        self.will_it_snow = bool(data["daily_will_it_snow"])
        self.chance_of_snow = data["daily_chance_of_snow"]/100
        
        self.condition = Condition(data["condition"])
        
        self.uv = data["uv"]
        
        try:
            aqi = data["air_quality"]
        except KeyError:
            self.air_quality = None
        else:
            self.air_quality = AirQuality(aqi)
