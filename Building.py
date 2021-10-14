from DividerList import DividerList
from Floor import Floor
from Wall import Wall
from Boundary import Boundary
from Window import Window
from Door import Door

class Building():

    def __init__(self, name):
        self.name = name
        self.floors = {}

    def create_floor(self, name, dividers = DividerList([]), areas = [], zones = []):
        if self.check_availability(name):
            floor = Floor(name, dividers, areas, zones)
            self.floors[name] = floor

    def check_availability(self, name):
        if name in self.floors.keys() :
            raise Exception("Sorry, a floor with this name has already been created!")
        return True

    def add_wall(self, floor_name, p1, p2):
        floor = self.floors[floor_name]
        wall = Wall(p1, p2)
        floor.add_divider(wall)

    def add_boundary(self, floor_name, p1, p2):
        floor = self.floors[floor_name]
        boundary = Boundary(p1, p2)
        floor.add_divider(boundary)

    def add_window(self, floor_name, wall_id, p1, p2):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(wall_id)
        assert isinstance(wall, Wall), 'The id does not correspond to a wall but a boundary'
        window = Window(p1, p2)
        wall.windows.append(window)

    def add_door(self, floor_name, wall_id, p1, p2):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(wall_id)
        assert isinstance(wall, Wall), 'The id does not correspond to a wall but a boundary'
        door = Door(p1, p2)
        wall.doors.append(door)