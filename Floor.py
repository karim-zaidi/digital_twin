from DividerList import DividerList
from Area import Area
from Zone import Zone
from Wall import Wall
from Boundary import Boundary

class Floor():

    def __init__(self, name, dividers = [], areas = [], zones = []):
        self.name = name
        self.dividers = dividers # Dividers can either be walls or boundaries
        self.areas = areas
        self.zones = zones

    def get_divider_by_id(self, id):
        for d in self.dividers:
            if d.id == id:
                return d
        raise ValueError('There is no divider with such an id on this floor (%s)' %str(self.name))

    def add_divider(self, divider):
        assert isinstance(divider, Wall) or isinstance(divider, Boundary), 'The new divider has to be a wall or a boundary'
        self.dividers.append(divider)
