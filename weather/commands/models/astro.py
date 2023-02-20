from datetime import datetime as dt

class Astro:
    """
    Represents astronomical status for a single day
    """
    def __init__(self, data: dict) -> None:
        """
        Represents astronomical status for a single day

        :param data: Dict of data to be parsed
        :type data: dict
        """
        self.sunrise = dt.strptime(data["sunrise"], "%I:%M %p").time()      #: Sunrise time as a datetime object
        self.sunset = dt.strptime(data["sunset"], "%I:%M %p").time()        #: Sunset time as a datetime object
        self.moonrise = dt.strptime(data["moonrise"], "%I:%M %p").time()    #: Moonrise time as a datetime object
        self.moonset = dt.strptime(data["moonset"], "%I:%M %p").time()      #: Moonset time as a datetime object
        self.moon_phase = data["moon_phase"]                                #: Name of moon phase
        self.moon_illumination = int(data["moon_illumination"]) / 100       #: Moon illumination as a decimal (0-1)
