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
        
        self.maxtemp_c = data["maxtemp_c"]                              #: Maximum temperature in celsius for the day
        self.maxtemp_f = data["maxtemp_f"]                              #: Maximum temperature in fahrenheit for the day
        self.mintemp_c = data["mintemp_c"]                              #: Minimum temperature in celsius for the day
        self.mintemp_f = data["mintemp_f"]                              #: Minimum temperature in fahrenheit for the day
        self.avgtemp_c = data["avgtemp_c"]                              #: Average temperature in celsius for the day
        self.avgtemp_f = data["avgtemp_f"]                              #: Average temperature in fahrenheit for the day
        
        self.maxwind_mph = data["maxwind_mph"]                          #: Maximum wind speed in miles per hour
        self.maxwind_kph = data["maxwind_kph"]                          #: Maximum wind speed in kilometer per hour
        
        self.totalprecip_mm = data["totalprecip_mm"]                    #: Total precipitation in milimeter
        self.totalprecip_in = data["totalprecip_in"]                    #: Total precipitation in inches
        
        try:
            self.totalsnow_cm = data["totalsnow_cm"]                    #: Total snow in centimeter
        except KeyError:
            self.totalsnow_cm = None
        
        self.avgvisibility_km = data["avgvis_km"]                       #: Average visibility in kilometer
        self.avgvisibility_miles = data["avgvis_miles"]                 #: Average visibility in miles
        self.avghumidity = data["avghumidity"]                          #: Average humidity as percentage
        
        try:
            self.will_it_rain = bool(data["daily_will_it_rain"])        #: Prediction whether it will rain or not. True if will rain
            self.chance_of_rain = data["daily_chance_of_rain"]/100      #: Chance of rain as a decimal (0-1)
            self.will_it_snow = bool(data["daily_will_it_snow"])        #: Prediction whether it will snow or not. True if will rain
            self.chance_of_snow = data["daily_chance_of_snow"]/100      #: Chance of snow as a decimal (0-1)
        except KeyError:
            self.will_it_rain = None
            self.chance_of_rain = None
            self.will_it_snow = None
            self.chance_of_snow = None
        
        self.condition = Condition(data["condition"])                   # Weather condition as a :class:`~weather.models.condition.Condition` object
        
        self.uv = data["uv"]
        
        try:
            aqi = data["air_quality"]
        except KeyError:
            self.air_quality = None
        else:
            self.air_quality = AirQuality(aqi)                          #: Air quality as a :class:`~weather.models.aqi.AirQuality` object
