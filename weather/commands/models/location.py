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
        self.name = data["name"]                                                #: Location name
        self.region = data["region"]                                            #: Region or state of the location, if available
        try:
            self.country = data["country"]                                      #: Location country
        except KeyError:
            self.country = self.name
        self.latitude = self.lat                                                #: Latitude in decimal degree
        self.lat = data["lat"]                                                  #: Alias for latitude
        self.longitude = self.long                                              #: Longitude in decimal degree
        self.long = data["lon"]                                                 #: Alias for longitude
        try:
            self.timezone_id = data["tz_id"]                                    #: Time zone name
            self.localtime_epoch = data["localtime_epoch"]                      #: Local date and time in unix time
            self.localtime = dt.strptime(data["localtime"], "%Y-%m-%d %H:%M")   #: Local date and time
        except KeyError:
            self.timezone_id = None
            self.localtime_epoch = None
            self.localtime = None