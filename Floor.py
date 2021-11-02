from DividerList import DividerList
from Area import Area
from Zone import Zone
from Wall import Wall
from Boundary import Boundary

class Floor():

    def __init__(self, name, dividers = [], areas = [], zones = []):
        self.__name = name

        self.__dividers = []
        self.add_divider(dividers)

        self.__areas = []
        self.add_area(areas)

        self.__zones = zones
    
    # name
    @property
    def name(self):
        return self.__name

    # TODO: condition for new_name = int ?
    # @name.setter
    # def name(self, new_name):
    #     assert isinstance(new_name, int)
    #     self.__name = new_name

    # dividers
    @property
    def dividers(self):
        return self.__dividers
    
    def add_divider(self, divider):
        assert isinstance(divider, (Wall, Boundary, list, tuple)), f'New divider has to be a (or a list/tuple of) wall or a boundary, no {type(divider).__name__}'
        
        if isinstance(divider, (list, tuple)) and len(divider)>0: 
            for d in divider:
                self.add_divider(d)
    
        elif isinstance(divider, (Wall, Boundary)):
            self.dividers.append(divider)
        

    # areas
    @property
    def areas(self):
        return self.__areas
    
    def add_area(self, area):
        assert isinstance(area, (Area, list, tuple)), f'New divider has to be a (or a list/tuple of) area, no {type(area).__name__}'
        if isinstance(area, (list, tuple)):
            for a in area:
                self.add_area(a)
        
        elif isinstance(area, Area):
            self.areas.append(area)
    
    # zones
    @property
    def zones(self):
        return self.__zones
    
    # Methods
    def get_divider_by_id(self, id):
        for d in self.dividers:
            if d.id == id:
                return d
        raise ValueError(f'There is no divider with such an id on this ({self.name}) floor')

