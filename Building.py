from DividerList import DividerList
from Floor import Floor
from Wall import Wall
from Boundary import Boundary
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

        # creating the plot
        plt.figure(figsize=(5, 5*n))

        for i in range(n):
            floor = self.floors[i]
            plt.title(f'Floor {floor.name}')

            # display dividers and their id
            for div in floor.dividers :
                # black line if wall
                if isinstance(div, Wall):
                    x1, y1, x2, y2 = div.p1, div.p2
                    plt.plot((x1,x2), (y1, y2), color='black')

                    for window in div.windows:
                        x1, y1, x2, y2 = window.p1, window.p2
                        plt.plot((x1,x2), (y1, y2), c='blue', linewidth = '2')
                    
                    for door in div.doors:
                        x1, y1, x2, y2 = door.p1, door.p2
                        plt.plot((x1,x2), (y1, y2), c='brown', linewidth = '2')    
            
                # gray point line if boundary
                if isinstance(div, Boundary):
                    x1, y1, x2, y2 = div.p1, div.p2
                    plt.plot((x1,x2), (y1, y2), color='gray', linestyle = ':') # --
                
            plt.show()


"""            
plt.figure(figsize=(5,5*n))

for i in range(n):
    
    plt.subplot(n+1, 1, i+1)
    
    plt.title('Floor %d' %i)
    p1, p2 = [-1, 12], [1, 4]
    plt.plot(p1, p2)
plt.show()
"""
