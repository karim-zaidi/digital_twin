from DividerList import DividerList
from Floor import Floor
from Wall import Wall
from Boundary import Boundary
from Window import Window
from Door import Door
from Area import Area

import matplotlib.pyplot as plt

class Building():

    def __init__(self, name):
        self.name = name
        self.floors = {}

    def create_floor(self, name, dividers = [], areas = [], zones = []):
        if self.check_availability(name):
            floor = Floor(name, dividers, areas, zones)
            self.floors[name] = floor

    def check_availability(self, name):
        if name in self.floors.keys() :
            raise Exception("Sorry, a floor with this name already exists")
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
        wall.add_window(window)

    def add_door(self, floor_name, wall_id, p1, p2):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(wall_id)
        assert isinstance(wall, Wall), 'The id does not correspond to a wall but a boundary'
        door = Door(p1, p2)
        wall.add_door(door)

    def add_area(self, floor_name, name, dividers = []):
        floor = self.floors[floor_name]
        area = Area(name, dividers)
        floor.add_area(area)

        

    def visualize(self):
        n = len(self.floors)
        
        # creating the plot
        plt.figure(figsize=(5, 5*n))

        for floor_name in self.floors.keys():
            floor = self.floors[floor_name]
            plt.title(f'Floor {floor.name}')

            # display dividers and their id
            for div in floor.get_dividers() :
                
                x1, x2 = div.get_x_coords()
                y1, y2 = div.get_y_coords()

                # display id
                xmin, xmax = min(x1,x2), max(x1,x2)
                ymin, ymax = min(y1,y2), max(y1,y2)
                plt.text(0.1*xmin + 0.9*xmax, 0.1*ymin +0.9*ymax, str(div.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                
                # gray point line if boundary
                if isinstance(div, Boundary):
                    plt.plot((x1,x2), (y1, y2), color='gray', linestyle = ':') # --
                
                # black line if wall
                elif isinstance(div, Wall):
                    plt.plot((x1,x2), (y1, y2), color='black')

                    for window in div.get_windows() :
                        x_1, x_2 = window.get_x_coords()
                        y_1, y_2 = window.get_y_coords()
                        x_1, y_1, x_2, y_2 = window.p1, window.p2
                        plt.plot((x1,x2), (y1, y2), c='blue', linewidth = '2')

                        # display id
                        x_min, x_max = min(x_1,x_2), max(x_1,x_2)
                        y_min, y_max = min(y_1,y_2), max(y_1,y_2)
                        plt.text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(window.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                    
                    for door in div.get_doors() :
                        x_1, x_2 = door.get_x_coords()
                        y_1, y_2 = door.get_y_coords()
                        plt.plot((x_1,x_2), (y_1, y_2), c='brown', linewidth = '2')    

                        # display id
                        x_min, x_max = min(x_1,x_2), max(x_1,x_2)
                        y_min, y_max = min(y_1,y_2), max(y_1,y_2)
                        plt.text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(window.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
            
            # name of the area
            for area in floor.get_areas():
                xmin, xmax, ymin, ymax = area.get_corners()
                plt.text((x_min + x_max)/2, (y_min + y_max)/2, f'{area.get_name()}\n{area.get_id()}', c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')


        plt.show()
