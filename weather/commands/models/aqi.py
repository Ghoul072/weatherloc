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
        self.co = data["co"]
        self.no2 = data["no2"]
        self.o3 = data["o3"]
        self.so2 = data["so2"]
        self.pm2_5 = data["pm2_5"]
        self.pm10 = data["pm10"]
        self.us_epa_index = data["us-epa-index"]
        self.gb_defra_index = data["gb-defra-index"]