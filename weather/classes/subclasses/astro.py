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
        self.sunrise = dt.strptime(data["sunrise"], "%I:%M %p").time()
        self.sunset = dt.strptime(data["sunset"], "%I:%M %p").time()
        self.moonrise = dt.strptime(data["moonrise"], "%I:%M %p").time()
        self.moonset = dt.strptime(data["moonset"], "%I:%M %p").time()
        self.moon_phase = data["moon_phase"]
        self.moon_illumination = data["moon_illumination"]
