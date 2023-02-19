from datetime import datetime as dt

class Location:
    """
    Represents a location object
    """
    def __init__(self, data: dict) -> None:
        """_summary_

        :param data: _description_
        :type data: dict
        """
        self.name = data["name"]
        self.region = data["region"]
        self.lat = data["lat"]
        self.latitude = self.lat
        self.long = data["lon"]
        self.longitude = self.long
        self.timezone_id = data["tz_id"]
        self.localtime_epoch = data["localtime_epoch"]
        self.localtime = dt.strptime(data["localtime"], "%Y-%m-%d %H:%M")