from numpy.lib.arraysetops import isin
from sklearn.utils import _print_elapsed_time
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
from matplotlib.patches import Polygon, Patch
import random
import numpy as np
from sklearn.cluster import KMeans


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
    

    def create_floor(self, name):
        if self.check_availability(name):
            floor = Floor(name)
            self.floors[name] = floor


    def rename_floor(self,floor_name,new_name):
        floor = self.floors[floor_name]
        floor.rename(self,new_name) 
    

    # Elements

    ## Wall
    def add_wall(self, floor_name, p1, p2):
        floor = self.floors[floor_name]
        wall = Wall(p1, p2)
        floor.add_divider(wall)


    def remove_wall(self, floor_name, id):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(id)
        assert isinstance(wall, Wall), 'This ID does not correspond to a wall'
        assert not wall.is_used, 'This wall cannot be removed as it is used in an area'
        floor.remove_divider_by_id(id)


    ## Boundary
    def add_boundary(self, floor_name, p1, p2):
        floor = self.floors[floor_name]
        boundary = Boundary(p1, p2)
        floor.add_divider(boundary)


    def remove_boundary(self, floor_name, id):
        floor = self.floors[floor_name]
        boundary = floor.get_divider_by_id(id)
        assert isinstance(boundary, Boundary), 'This ID does not correspond to a boundary'
        assert not boundary.is_used, 'This boundary cannot be removed as it is used in an area'
        floor.remove_divider_by_id(id)


    ## Window
    def add_window(self, floor_name, wall_id, p1, p2):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(wall_id)
        assert isinstance(wall, Wall), 'The id does not correspond to a wall but a boundary'
        window = Window(p1, p2)
        wall.add_window(window)

    
    def remove_window(self, floor_name, id):
        floor = self.floors[floor_name]
        done = False
        for wall in floor.dividers:
            if isinstance(wall, Wall):
                for window in wall.windows:
                    if window.id == id:
                        wall.remove_element_by_id(id)
                        done = True
        if not done:
            raise ValueError(f'There is no window with such an id on this ({floor_name}) floor')


    ## Door
    def add_door(self, floor_name, wall_id, p1, p2):
        floor = self.floors[floor_name]
        wall = floor.get_divider_by_id(wall_id)
        assert isinstance(wall, Wall), 'The id does not correspond to a wall but a boundary'
        door = Door(p1, p2)
        wall.add_door(door)


    def remove_door(self, floor_name, id):
        floor = self.floors[floor_name]
        done = False
        for wall in floor.dividers:
            if isinstance(wall, Wall):
                for door in wall.doors:
                    if door.id == id:
                        wall.remove_element_by_id(id)
                        done = True
        if not done:
            raise ValueError(f'There is no door with such an id on this ({floor_name}) floor')


    # Area
    def add_area(self, floor_name, name, dividers = []):
        """
        dividers has to be a list/tuple of 4 IDs of already existing dividers on the floor
        """
        floor = self.floors[floor_name]

        div = []
        for d in dividers:
            divider = floor.get_divider_by_id(d)
            divider.is_now_used()
            div.append(divider)
            
        area = Area(name, div)
        floor.add_area(area)


    def remove_area(self, floor_name, id):
        floor = self.floors[floor_name]
        area = floor.get_area_by_id(id)
        assert not area.is_used, 'This area cannot be removed as it is used in a zone'
        for divider in area.walls+area.boundaries:
            divider.is_no_longer_used()
        floor.remove_area_by_id(id)


    # Zone
    def add_atomic_zone(self, floor_name, areas = [], polygon = []):
        """
        areas can be an ID or a list/tuple of IDs of already existing areas on the floor
        """
        assert len(list(areas))+len(polygon)>0, 'A new AtomicZone needs at least an area or a polygon'
        floor = self.floors[floor_name]

        if isinstance(areas,int):
            areas_temp = floor.get_area_by_id(areas)
            areas_temp.is_now_used()
        elif isinstance(areas,(list,tuple)):
            areas_temp = []
            for a in areas:
                area = floor.get_area_by_id(a)
                area.is_now_used()
                areas_temp.append(area)

        atomic_zone = AtomicZone(areas_temp,polygon)
        floor.add_zone(atomic_zone)


    def add_area_to_zone(self, floor_name, zone_id, areas_id):
        floor = self.floors[floor_name]
        zone = floor.get_zone_by_id(zone_id)
        if isinstance(areas_id,int):
            areas_temp = floor.get_area_by_id(areas_id)
            areas_temp.is_now_used()
        elif isinstance(areas_id,(list,tuple)):
            areas_temp = []
            for a in areas_id:
                area = floor.get_area_by_id(a)
                area.is_now_used()
                areas_temp.append(area)
        zone.add_area(areas_temp)


    def set_zone_polygon(self, floor_name, zone_id, polygon):
        floor = self.floors[floor_name]
        zone = floor.get_zone_by_id(zone_id)
        zone.polygon = polygon

    
    def add_composite_zone(self, floor_name, zones):
        """
        zones can be an ID or a list/tuple of IDs of already existing zones on the floor
        """
        assert zones != None and zones != [] and zones != (), 'A new composite zone needs at least one component zone'
        floor = self.floors[floor_name]

        if isinstance(zones,int):
            zones_temp = floor.get_zone_by_id(zones)
        elif isinstance(zones,(list,tuple)):
            zones_temp = []
            for z in zones:
                zones_temp.append(floor.get_zone_by_id(z))

        composite_zone = CompositeZone(zones_temp)
        floor.add_zone(composite_zone)


    def remove_zone(self, floor_name, id):
        floor = self.floors[floor_name]
        zone = floor.get_zone_by_id(id)
        assert not zone.is_used, 'This zone cannot be removed as it is a component of another zone'
        if isinstance(zone, CompositeZone):
            for z in zone.zones:
                z.is_no_longer_used()
        elif isinstance(zone, AtomicZone):
            for a in zone.areas:
                a.is_no_longer_used()
        floor.remove_zone_by_id(id)


    def merge_zone(self, floor_name, zone, composite_zone):
        floor = self.floors[floor_name]
        z = floor.get_zone_by_id(zone)
        composite_z = floor.get_zone_by_id(composite_zone)
        assert isinstance(z,Zone)
        assert isinstance(composite_z,CompositeZone)
        composite_z.add(z)


    def detach_zone_from_zone(self, floor_name, component_zone, composite_zone):
        floor = self.floors[floor_name]
        cpnt = floor.get_zone_by_id(component_zone)
        cpst = floor.get_zone_by_id(composite_zone)
        assert isinstance(cpst, CompositeZone), 'composite_zone has to be a CompositeZone'
        assert cpnt in cpst.zones, 'component_zone is not a component of composite_zone'
        cpnt.is_no_longer_used()
        cpst.remove(cpnt)


    # Other Methods
    # TODO: Make cluster work
    def __clusters(self, floor_name, data, zone_id, n_clusters = 4, ti = 0, tf = np.inf):
        # Keeping only relevant timestamps
        filtered_data = data[data[:,0] >= ti]
        filtered_data = filtered_data[filtered_data[:,0] <= tf]
        print(filtered_data)

        # Keeping only datapoints inside the zone
        floor = self.floors[floor_name]
        zone = floor.get_zone_by_id(zone_id)
        d = []
        for datapoint in filtered_data:
            if zone.contains(datapoint):
                d.append(datapoint)
        filtered_data = d

        x = filtered_data[:][1]
        print('x : '+str(x))
        y = filtered_data[:][2]
        X = np.zeros((len(x),2))
        for i in range(len(X)):
            X[i,0] = x[i][1]
            X[i,1] = y[i][2]
        print(X)

        km = KMeans(n_clusters=n_clusters, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)
        cluster = km.fit_predict(X)
        
        return x, y, cluster


    def visualize_clusters(self, floor_name, data, zone_id, n_clusters = 4, ti = 0, tf = np.inf):
        x, y, cluster = self.__clusters(floor_name, data, zone_id, n_clusters, ti , tf)
        self.__draw(True, floor_name, x, y, cluster)


    @staticmethod
    def __get_colors(n):
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
    def __print_zone(zone, zone_id, axes, i, color, legends):
        # updating the legend
        if (not Patch(color=color, label=zone_id) in legends) and (not zone.is_used):
            legends.append(Patch(color=color, label=zone_id))

        # drawing the zone
        if isinstance(zone, AtomicZone):
            for area in zone.areas:
                x_min, x_max, y_min, y_max = area.get_bounding_box()
                # using Polygon instead of Rectangle to have the same color
                axes[i].add_patch(Polygon(np.array([[x_min, y_min], [x_min, y_max], [x_max, y_max], [x_max, y_min]]), fill=True, alpha=0.3, color=color))

            poly = zone.polygon  
            if len(poly) > 0:
                axes[i].add_patch(Polygon(zone.polygon_to_array(), fill=True, alpha=0.3, color=color))
        
        elif isinstance(zone, CompositeZone):
            for z in zone.zones:
                Building.__print_zone(z, zone_id, axes, i, color, legends)


    def visualize(self):
        self.__draw(test=False, name=None, x=None, y=None, cluster_name=None)


    def __draw(self, test, name, x, y, cluster_name):
        n = len(self.floors)

        if n == 0:
            print('Building is empty!')
        
        else:
            show_legend = False

            # In the case of a single floor building, we can't loop over the axes of the subplot
            # so we are adding an additional floor to keep the code simple (and then we will delete it)
            n += 1
            
            # creating the plot with a good size and 
            # setting constrained_layout=True to have more freedom for the legend's localisation
            f, axes = plt.subplots(n, 1, sharey=True, figsize=(10, 10*n), constrained_layout=True)

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
                            axes[i].plot((x_min, x_max), (y_min, y_max), c='cyan')

                            # display id
                            axes[i].text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(window.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                        
                        for door in div.doors :
                            x_min, x_max = door.get_x_coords()
                            y_min, y_max = door.get_y_coords()
                            axes[i].plot((x_min, x_max), (y_min, y_max), c='chocolate')    

                            # display id
                            axes[i].text(0.1*x_min + 0.9*x_max, 0.1*y_min +0.9*y_max, str(door.id), c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')
                
                # name of the area
                for area in floor.areas:
                    x_min, x_max, y_min, y_max = area.get_bounding_box()
                    axes[i].text((x_min + x_max)/2, (y_min + y_max)/2, f'{area.name}\n{area.id}', c='black', style='italic', bbox={'facecolor': 'white'}, ha='center', va='center')

                # zone
                if len(floor.zones) > 0:
                    show_legend = True
                    legends = []
                    
                    # generating len(floor.zones) color at random
                    colors = Building.__get_colors(len(floor.zones))
                    
                    for zone, color in zip(floor.zones, colors):
                        if not zone.is_used:
                            Building.__print_zone(zone, zone.id, axes, i, color, legends)
                    
                if show_legend:

                    axes[i].legend(handles=legends, 
                                   bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure) # pushing the legend outside
            
                # setting the same scales for the x and y axes
                axes[i].set_aspect('equal', adjustable='box')

                if test and floor_name == name:
                    # number of color needed
                    m = len(set(cluster_name[4]))

                    # taking m different colors
                    c = [i for i in range(m)]
                    axes[i].scatter(x, y, c=[c[i] for i in cluster_name[4]])
                    
            # deleting the last (inexisting) floor
            f.delaxes(axes[n-1])

            plt.show()