class AirQuality:
    """
    Represents air quality
    """
    def __init__(self, data: dict) -> None:
        """
        Represents air quality

        :param data: Dict of data to be parsed
        :type data: dict
        """
        self.co = data["co"]                            #: Carbon Monoxide concentration (μg/m3)
        self.no2 = data["no2"]                          #: Nitrogen Dioxide concentration (μg/m3)
        self.o3 = data["o3"]                            #: Ozone concentration (μg/m3)
        self.so2 = data["so2"]                          #: Sulfur Dioxide concentration (μg/m3)
        self.pm2_5 = data["pm2_5"]                      #: PM2.5 PM2.5 (μg/m3)
        self.pm10 = data["pm10"]                        #: PM10 (μg/m3)
        self.us_epa_index = data["us-epa-index"]        #: US - EPA standard 
        self.gb_defra_index = data["gb-defra-index"]    #: UK Defra Index