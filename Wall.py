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

    
    # Windows
    @property
    def windows(self):
        return self.__windows  

    def add_window(self, window):
        """Add single window or multiple windows in a list/tuple"""
        assert isinstance(window, (Window, list, tuple)), f'add_window function takes a window or list/tuple of windows as argument, no {type(window).__name__}'

        if isinstance(window, (list, tuple)):
            for w in window:
                self.add_window(w)

        elif isinstance(window, Window):
            assert self.__is_supporting(window), 'The window is not on the wall'
            assert self.__has_room_for(window), 'There is a conflict with some elements of the wall or the wall itself'

            self.windows.append(window)
    

    # Doors
    @property
    def doors(self):
        return self.__doors

    def add_door(self, door):
        """Add single door or multiple doors in a list/tuple"""
        assert isinstance(door, (Door, list, tuple)), f'add_door function takes a door or list/tuple of doors as argument, no {type(door).__name__}'

        if isinstance(door, (list, tuple)):
            for d in door:
                self.add_door(d)

        elif isinstance(door, Door):
            assert self.__is_supporting(door), 'The door is not on the wall'
            assert self.__has_room_for(door), 'There is a conflict with some elements of the wall'

            self.doors.append(door)


    # Methods
    @staticmethod
    def is_inside_element(e1, e2):
        """Check if e1 has a coordinate inside e2"""
        e1_x_min, e1_x_max = e1.get_x_coords()
        e1_y_min, e1_y_max = e1.get_y_coords()

        e2_x_min, e2_x_max = e2.get_x_coords()
        e2_y_min, e2_y_max = e2.get_y_coords()

        # if it's parallel to the y axis
        if e1_y_max == e1_y_min:
            if e1_x_max >= e2_x_min and e1_x_max <= e2_x_max:
                return True
            elif e1_x_min >= e2_x_min and e1_x_min <= e2_x_max:
                return True
        
        # elif it's parallel to the x axis
        elif e1_x_max == e1_x_min:
            if e1_y_max >= e2_y_min and e1_y_max <= e2_y_max:
                return True
            elif e1_y_min >= e2_y_min and e1_y_min <= e2_y_max:
                return True
        return False


    def __has_room_for(self, e):
        elements = self.windows + self.doors

        for element in elements:
            # check if the e has a coordinate inside element
            if self.is_inside_element(e, element) or self.is_inside_element(element, e):
                return False
        return True


    def __is_supporting(self, e):
        """Verify if element e is aligned with the wall"""
        assert isinstance(e, Window) or isinstance(e, Door), f'Only a door or a window can be placed on a wall, no {type(e).__name__}.'

        wall_x1,wall_x2 = self.get_x_coords()
        wall_y1,wall_y2 = self.get_y_coords()
        e_x1,e_x2 = e.get_x_coords()
        e_y1,e_y2 = e.get_y_coords()

        return (e_x1 >= wall_x1 and e_x2 <= wall_x2) and (e_y1 >= wall_y1 and e_y2 <= wall_y2)


