from Element import Element
from Window import Window
from Door import Door

class Wall(Element):

    def __init__(self, p1, p2, windows = [], doors = []):
        super().__init__(p1,p2)
        
        # Initializing windows
        self.__windows = []
        self.add_window(windows)

        # Initializing doors
        self.__doors = []
        self.add_door(doors)

    @staticmethod
    def is_inside_element(e1, e2):
        """Check if e1 has a coordinate inside e2"""
        e1_x_min, e1_x_max = e1.get_x_coords()
        e1_y_min, e1_y_max = e1.get_y_coords()

        e2_x_min, e2_x_max = e2.get_x_coords()
        e2_y_min, e2_y_max = e2.get_y_coords()

        if e1_x_max < e2_x_min or e1_x_max > e2_x_max:
            return False
        elif e1_x_min < e2_x_min or e1_x_min > e2_x_max:
            return False
        elif e1_y_max < e2_y_min or e1_y_max > e2_y_max:
            return False
        elif e1_y_min < e2_y_min or e1_y_min > e2_y_max:
            return False
        return True


    def __has_space(self, e):
        elements = self.windows + self.doors

        for element in elements:
            # check if the e has a coordinate inside element
            if self.is_inside_element(e, element) or self.is_inside_element(element, e):
                return False
        
        # check if e is inside the wall
        return self.is_inside_element(e, self)


    def __is_supporting(self, e):
        """Verify if element e is aligned with the wall"""
        assert isinstance(e, Window) or isinstance(e, Door), f'Only a door or a window can be placed on a wall, no {type(e).__name__}.'

        wall_x_coords = self.get_x_coords()
        wall_y_coords = self.get_y_coords()
        e_x_coords = e.get_x_coords()
        e_y_coords = e.get_y_coords()

        # If the wall is parallel to the y axis, ie. if its two x coords are the same
        if wall_x_coords[0] == wall_x_coords[1]: 
            # If the element isn't parallel to the y axis return False
            if e_x_coords[0] != e_x_coords[1]: 
                return False
            # If the element isn't aligned with the wall return False
            elif e_x_coords[0] != wall_x_coords[0]: 
                return False
            return True
        # If the wall is parallel to the x axis, ie. if its two y coords are the same
        elif wall_y_coords[0] == wall_y_coords[1]: 
            # If the element isn't parallel to the x axis return False
            if e_y_coords[0] != e_y_coords[1]: 
                return False
            
            # If the element isn't aligned with the wall return False
            elif e_y_coords[0] != wall_y_coords[0]: 
                return False
            return True
        else:
            print('Somehow the wall is not aligned to the x axis nor the y axis. It cannot support a door/window')
            exit(1)

    # Windows
    @property
    def windows(self):
        return self.__windows  

    def add_window(self, window):
        """Add single window or multiple windows in a list/tuple"""
        assert isinstance(window, (Window,list, tuple)), f'add_window function takes a window or list/tuple of windows as argument, no {type(window).__name__}'

        if isinstance(window, (list, tuple)) and len(window)>0:
            for w in window:
                self.add_window(w)

        elif isinstance(window, Window):
            assert self.__is_supporting(window), 'The window is not on the wall'
            assert self.__has_space(window), 'There is a conflict with some elements of the wall or the wall itself'

            self.__windows.append(window)
    
    # Doors
    @property
    def doors(self):
        return self.__doors

    def add_door(self, door):
        """Add single door or multiple doors in a list/tuple"""
        assert isinstance(door, (Door, list, tuple)), f'add_door function takes a door or list/tuple of doors as argument, no {type(door).__name__}'

        if isinstance(door, (list, tuple)) and len(door)>0:
            for d in door:
                self.add_door(d)

        elif isinstance(door, Door):
            assert self.__is_supporting(door), 'The door is not on the wall'
            assert self.__has_space(door), 'There is a conflict with some elements of the wall or the wall itself'

            self.__doors.append(door)
        
        else:
            self.__doors = []

