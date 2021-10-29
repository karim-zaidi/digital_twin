from DividerList import DividerList
from Area import Area
from Zone import Zone
from Wall import Wall
from Boundary import Boundary

class Floor():

    def __init__(self, name, dividers = [], areas = [], zones = []):
        self.name = name
        self.add_divider(dividers)
        self.add_area(areas)
        self.zones = zones
    
    def get_dividers(self):
        return self.dividers
    
    def get_areas(self):
        return self.areas
    
    def get_zones(self):
        return self.zones
    
    def get_divider_by_id(self, id):
        for d in self.dividers:
            if d.id == id:
                return d
        raise ValueError('There is no divider with such an id on this floor (%s)' %str(self.name))

    def add_divider(self, divider):
        if isinstance(divider[0], list): # If divider is actually (or seems to be) a list of dividers to be added
            for d in divider:
                self.add_divider(d)
        assert isinstance(divider, Wall) or isinstance(divider, Boundary), 'New divider has to be a wall or a boundary'
        self.dividers.append(divider)

    def add_area(self, area):
        if isinstance(area[0], Area): # If area is actually (or seems to be) a list of areas to be added:
            for a in area:
                self.add_area(a)
        assert isinstance(area, Area), 'New area has to be an Area'
        self.areas.append(area)