from .subclasses import Astro, Location

class Astronomy(Astro):
    """
    Same as Astro class but with a location attribute
    """
    def __init__(self, data: dict) -> None:
        """
        Constructor class

        :param data: Dict of data to be parsed
        :type data: dict
        """
        super().__init__(data["astronomy"]["astro"])
        self.location = Location(data["location"])
