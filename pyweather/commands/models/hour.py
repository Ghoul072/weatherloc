from datetime import datetime as dt


class Hour:
    """Represents weather condition for a single hour"""
    def __init__(self, data: dict) -> None:
        """
        Represents weather condition for a single hour

        :param data: Dict of data to be parsed
        :type data: dict
        """
        
        self.time_epoch = data["time_epoch"]                        #: Time as epoch
        self.time = dt.strptime(data["time"], "%Y-%m-%d %H:%M")     #: Date and time
        
        self.temp_c = data["temp_c"]                                #: Temperature in celsius
        self.temp_f = data["temp_f"]                                #: Temperature in fahrenheit
        
        self.wind_mph = data["wind_mph"]                            #: Maximum wind speed in miles per hour
        self.wind_kph = data["wind_kph"]                            #: Maximum wind speed in kilometer per hour
        self.wind_degree = data["wind_degree"]                      #: Wind direction in degrees
        self.wind_direction = data["wind_dir"]                      #: Wind direction as 16 point compass
        
        self.pressure_mb = data["pressure_mb"]                      #: Pressure in millibars
        self.pressure_in = data["pressure_in"]                      #: Pressure in inches
        
        self.precip_mm = data["precip_mm"]                          #: Precipitation amount in millimeters
        self.precip_in = data["precip_in"]                          #: Precipitation amount in inches
        
        self.humidity = data["humidity"]                            #: Humidity as percentage
        self.cloud = int(data["cloud"]) / 100                       #: Cloud cover as decimal (0-1)
        
        self.feelslike_c = data["feelslike_c"]                      #: Feels like temperature as celcius
        self.feelslike_f = data["feelslike_f"]                      #: Feels like temperature as fahrenheit
        
        self.windchill_c = data["windchill_c"]                      #: Windchill temperature in celcius
        self.windchill_f = data["windchill_f"]                      #: Windchill temperature in fahrenheit
        self.heatindex_c = data["heatindex_c"]                      #: Heat index in celcius
        self.heatindex_f = data["heatindex_f"]                      #: Heat index in fahrenheit
        self.dewpoint_c = data["dewpoint_c"]                        #: Dew point in celcius
        self.dewpoint_f = data["dewpoint_f"]                        #: Dew point in fahrenheit
        
        self.will_it_rain = bool(data["will_it_rain"])              #: Prediction if it will rain or not. True if will rain
        self.chance_of_rain = data["chance_of_rain"]/100            #: Chance of rain as a decimal (0-1)
        self.will_it_snow = bool(data["will_it_snow"])              #: Prediction if it will snow or not. True if will rain
        self.chance_of_snow = data["chance_of_snow"]/100            #: Chance of snow as a decimal (0-1)
        
        self.visibility_km = data["vis_km"]                         #: Visibility in kilometer
        self.visibility_miles = data["vis_miles"]                   #: Visibility in miles
        
        try:
            self.uv = data["uv"]                                    #: UV Index
        except KeyError:
            self.uv = None
        
        self.gust_mph = data["gust_mph"]                            #: Wind gust in miles per hour
        self.gust_kph = data["gust_kph"]                            #: Wind gust in kilometer per hour