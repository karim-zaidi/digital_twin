from DividerList import DividerList
from Floor import Floor
from Wall import Wall
import matplotlib.pyplot as plt

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

    def visualize(self):
        n = len(self.floors)
        f, axes = plt.subplot(n, 1, figsize=(15*n, n), sharey = True)

        for i, ax in enumerate(axes.flat):
            floor = self.floors[i]
            ax.title('Floor %s ' % floor.name)

            # display dividers
            for div in floor.dividers :
                # display only walls
                if isinstance(div, Wall):
                    ax.plot(div.p1, div.p2)


