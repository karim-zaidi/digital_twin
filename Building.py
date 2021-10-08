from DividerList import DividerList
from Floor import Floor

class Building():

    def __init__(self, name):
        self.name = name
        self.floors = []

    def create_floor(self, name, dividers = DividerList([]), areas = [], zones = []):
        if self.check_availability(name):
            floor = Floor(name, dividers, areas, zones)
            self.floors.append(floor)

    def check_availability(self, name):
        for floor in self.floors:
            if name == floor.name :
                raise Exception("Sorry, a floor with this name has already been created!")
        return True
