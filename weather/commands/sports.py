from datetime import datetime as dt

class Activity:
    """
    Represents an activity
    """
    def __init__(self, data: dict) -> None:
        """
        Represents an acitivity

        :param data: Dict of data to be parsed
        :type data: dict
        """
        self.stadium = data["stadium"]
        self.country = data["country"]
        self.region = data["region"]
        self.tournament = data["tournament"]
        self.start = dt.strptime(data["start"], "%Y-%m-%d %H:%M")
        self.match = data["match"]

class Sports:
    """
    Represents a container for sports, each sport has a list of :class:`~weather.commands.sports.Activity` objects
    """
    def __init__(self, data: dict) -> None:
        """
        Represents a container for sports, each sport has a list of :class:`~weather.commands.sports.Activity` objects

        :param data: Dict of data to be parsed. Must be a result from http://api.weatherapi.com/v1/sports.json 
        :type data: dict
        """
        self.football = [Activity(sport) for sport in data["football"]]     #: Football results. This is a list of :class:`~weather.commands.sports.Activity` objects
        self.cricket = [Activity(sport) for sport in data["cricket"]]       #: Cricket results. This is a list of :class:`~weather.commands.sports.Activity` objects
        self.golf = [Activity(sport) for sport in data["golf"]]             #: Golf results. This is a list of :class:`~weather.commands.sports.Activity` objects