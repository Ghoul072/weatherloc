from datetime import datetime as dt

from .models import Location

class Astronomy:
    """
    Represents astronomical status for a single day. This is similar to :class:`~weather.commands.models.astro.Astro` class but has a location attribute
    """
    def __init__(self, data: dict) -> None:
        """
        Astronomy class constructor

        :param data: Dict of data to be parsed. Must be a result from http://api.weatherapi.com/v1/astronomy.json
        :type data: dict
        """
        self.location = Location(data["location"])                          #: Instance of :class:`~weather.commands.models.location.Location`
        data = data["astronomy"]["astro"]
        self.sunrise = dt.strptime(data["sunrise"], "%I:%M %p").time()      #: Sunrise time as a datetime object
        self.sunset = dt.strptime(data["sunset"], "%I:%M %p").time()        #: Sunset time as a datetime object
        self.moonrise = dt.strptime(data["moonrise"], "%I:%M %p").time()    #: Moonrise time as a datetime object
        self.moonset = dt.strptime(data["moonset"], "%I:%M %p").time()      #: Moonset time as a datetime object
        self.moon_phase = data["moon_phase"]                                #: Name of moon phase
        self.moon_illumination = int(data["moon_illumination"]) / 100       #: Moon illumination as a decimal (0-1)