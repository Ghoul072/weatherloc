class LookupIP:
    def __init__(self, data: dict) -> None:
        
        self.ip_addr = data["ip"]
        self.type = data["type"]
        
        self.continent_code = data["continent_code"]
        self.continent_name = data["continent_name"]
        
        self.country_code = data["country_code"]
        self.country_name = data["country_name"]
        
        self.is_eu = False if data["is_eu"] == "false" else True
        self.geoname_id = data["geoname_id"]
        
        self.city = data["city"]
        self.region = data["region"]
        
        self.latitude = data["lat"]
        self.lat = self.latitude
        self.longitude = data["lon"]
        self.long = self.longitude
        self.timezone_id = data["tz_id"]
        
        self.localtime_epoch = data["localtime_epoch"]
        self.localtime = data["localtime"]
