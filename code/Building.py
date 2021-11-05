from Floor import Floor

from Area import Area

from Zone import Zone
from AtomicZone import AtomicZone
from CompositeZone import CompositeZone

from Wall import Wall
from Boundary import Boundary
from Window import Window
from Door import Door

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import random


class Building():

    def __init__(self, name):
        self.__name = name
        self.__floors = {}


    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str)
        self.__name = new_name


    # floors
    @property
    def floors(self):
        return self.__floors
    
    def check_availability(self, name):
        if name in self.floors.keys() :
            raise Exception("Sorry, a floor with this name already exists")
        return True
    
    def create_floor(self, name, dividers = [], areas = [], zones = []):
        if self.check_availability(name):
            floor = Floor(name, dividers, areas, zones)
            self.floors[name] = floor

    def rename_floor(self,floor_name,new_name):
        floor = self.floors[floor_name]
        floor.rename(self,new_name) 
    

    # Other methods
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
        """
        dividers can be an ID or list/tuple of IDS of already existing dividers on the floor
        """
        floor = self.floors[floor_name]

        div = []
        for d in dividers:
            div.append(floor.get_divider_by_id(d))
            
        area = Area(name, div)
        floor.add_area(area)


    def add_atomic_zone(self, floor_name, areas = [], polygon = []):
        """
        areas can be an ID or a list/tuple of IDs of already existing areas on the floor
        """
        assert len(areas)+len(polygon)>0, 'A new AtomicZone needs at least an area or a polygon'
        floor = self.floors[floor_name]

        if isinstance(areas,int):
            ar = floor.get_area_by_id(areas)
        elif isinstance(areas,(list,tuple)):
            ar = []
            for a in areas:
                ar.append(floor.get_area_by_id(a))

        atomic_zone = AtomicZone(ar,polygon)
        floor.add_zone(atomic_zone)

    
    def add_composite_zone(self, floor_name, zones):
        """
        zones can be an ID or a list/tuple of IDs of already existing zones on the floor
        """
        assert len(zones)>0, 'A new composite zone needs at least one component zone'
        floor = self.floors[floor_name]

        if isinstance(zones,int):
            zo = floor.get_zone_by_id(zones)
        elif isinstance(zones,(list,tuple)):
            zo = []
            for z in zones:
                zo.append(floor.get_zone_by_id(z))

        composite_zone = CompositeZone(zo)
        floor.add_zone(composite_zone)


    def merge_zone(self, zone, composite_zone):
        assert isinstance(zone,Zone)
        assert isinstance(composite_zone,CompositeZone)
        composite_zone.add(zone)


    @staticmethod
    def get_colors(n):
        """Generates a list of RGB values at random"""
        rgb = [] 
        r = int(random.random() * 256) 
        g = int(random.random() * 256) 
        b = int(random.random() * 256) 
        step = 256 / n 
        for _ in range(n): 
            r += step 
            g += step 
            b += step
            r = r % 256 
            g = g % 256 
            b = b % 256 
            rgb.append((r/256,g/256,b/256))  
        return rgb
    

    @staticmethod
    def __print_zone(zone, zone_id, axes, i, color):
        if isinstance(zone, AtomicZone):
            for area in zone.areas:
                x_min, x_max, y_min, y_max = area.get_bounding_box()
                left, bottom, width, height = (x_min, y_min, x_max - x_min, y_max - y_min)
                axes[i].add_patch(Rectangle((left, bottom), width, height, alpha=0.1, facecolor=color, label=zone_id))

            poly = zone.polygon  
            if len(poly) > 0:
                axes[i].add_patch(Polygon(zone.polygon_to_array(), fill=True, alpha=0.1, color=color, label=zone_id))
        
        elif isinstance(zone, CompositeZone):
            for z in zone.zones:
                Building.__print_zone(z, zone_id, axes, i, color)


    def visualize(self):
        n = len(self.floors)
        
        # creating the plot
        f, axes = plt.subplots(2, 1, sharey=True, figsize=(5, 5*n))

        for i, floor_name in enumerate(self.floors.keys()):
            floor = self.floors[floor_name]
            axes[i].set_title(f'Floor {floor.name}')

            # display dividers and their id
            for div in floor.dividers :
                
                xmin, xmax = div.get_x_coords()
                ymin, ymax = div.get_y_coords()

                # display id
                axes[i].text(0.1*xmin + 0.9*xmax, 0.1*ymin +0.9*ymax, str(div.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                
                # gray point line if boundary
                if isinstance(div, Boundary):
                    axes[i].plot((xmin, xmax), (ymin, ymax), color='gray', linestyle = ':') # --
                
                # black line if wall
                elif isinstance(div, Wall):
                    axes[i].plot((xmin, xmax), (ymin, ymax), color='black')

                    for window in div.windows :
                        x_min, x_max = window.get_x_coords()
                        y_min, y_max = window.get_y_coords()
                        axes[i].plot((x_min, x_max), (y_min, y_max), c='blue', linewidth = '2')

                        # display id
                        axes[i].text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(window.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                    
                    for door in div.doors :
                        x_min, x_max = door.get_x_coords()
                        y_min, y_max = door.get_y_coords()
                        axes[i].plot((x_min, x_max), (y_min, y_max), c='brown', linewidth = '2')    

                        # display id
                        axes[i].text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(window.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
            
            # name of the area
            for area in floor.get_areas():
                x_min, x_max, y_min, y_max = area.get_bounding_box()
                axes[i].text((x_min + x_max)/2, (y_min + y_max)/2, f'{area.get_name()}\n{area.get_id()}', c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')

            # zone
        
            # generating len(floor.zones) color at random
            colors = Building.get_colors(len(floor.zones))
            
            for zone, color in zip(floor.zones, colors):
                if not zone.is_component:
                    Building.__print_zone(zone, zone.id, axes, i, color)

        plt.legend()
        plt.show()