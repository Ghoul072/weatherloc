class Condition:
    """
    Represents a weather condition object
    """
    def __init__(self, data: dict) -> None:
        """
        Construct method

        :param data: Dict of data to be parsed
        :type data: dict
        """
        self.text = data["text"]    #: Text description of weather condition
        self.icon = data["icon"]    #: Image representation of weather condition
        self.code = data["code"]    #: Weather code used by the API
        
    def __str__(self) -> str:
        return self.text
        