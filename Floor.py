from DividerList import DividerList
from Area import Area
from Zone import Zone

class Floor():

    def __init__(self, name, dividers = DividerList([]), areas = [], zones = []):
        self.name = name
        self.dividers = dividers
        self.areas = areas
        self.zones = zones

    def get_divider_by_id(self, id):
        for d in self.dividers:
            if d.id == id:
                return d
        raise ValueError('There is no divider with such an id on this floor (%s)' %str(self.name))

    def add_divider(self, divider):
        self.dividers.add_divider(divider)
