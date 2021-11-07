from Area import Area
from Zone import Zone
from Wall import Wall
from Boundary import Boundary

class Floor():

    def __init__(self, name):
        # We only allow to create an empty floor, 
        # everything is handled from the Building class
        self.__name = name

        self.__dividers = []
        self.__areas = []
        self.__zones = []


    # name
    @property
    def name(self):
        return self.__name


    def rename(self, building, new_name):
        assert isinstance(new_name,(int,str))
        if building.check_availability(new_name):
            self.__name = new_name


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
            

    def get_divider_by_id(self, id):
        for d in self.dividers:
            if d.id == id:
                return d
        raise ValueError(f'There is no divider with such an id on this ({self.name}) floor')


    def remove_divider_by_id(self, id):
        divider = self.get_divider_by_id(id)
        self.dividers.remove(divider)  


    # areas
    @property
    def areas(self):
        return self.__areas
    

    def add_area(self, area):
        assert isinstance(area, (Area, list, tuple)), f'New area has to be a (or a list/tuple of) area, no {type(area).__name__}'
        if isinstance(area, (list, tuple)):
            for a in area:
                self.add_area(a)
        
        elif isinstance(area, Area):
            self.areas.append(area)
    

    def get_area_by_id(self, id):
        for a in self.areas:
            if a.id == id:
                return a
        raise ValueError(f'There is no area with such an id on this ({self.name}) floor')


    def remove_area_by_id(self, id):
        area = self.get_area_by_id(id)
        self.areas.remove(area)


    # zones
    @property
    def zones(self):
        return self.__zones
    

    def add_zone(self, zone):
        assert isinstance(zone, (Zone, list, tuple)), f'New zone has to be a (or a list/tuple of) zone, no {type(zone).__name__}'
        if isinstance(zone, (list, tuple)):
            for z in zone:
                self.add_zone(z)
        
        elif isinstance(zone, Zone):
            self.zones.append(zone)


    def get_zone_by_id(self, id):
        for z in self.zones:
            if z.id == id:
                return z
        raise ValueError(f'There is no zone with such an id on this ({self.name}) floor')


    def remove_zone_by_id(self, id):
        zone = self.get_zone_by_id(id)
        self.zones.remove(zone)