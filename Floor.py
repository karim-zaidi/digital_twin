from DividerList import DividerList
from Area import Area
from Zone import Zone

class Floor():

    def __init__(self, name, dividers = DividerList([]), areas = [], zones = []):
        self.name = name
        self.dividers = dividers
        self.areas = areas
        self.zones = zones
