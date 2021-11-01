from Element import Element
from Window import Window
from Door import Door

class Wall(Element):

    def __init__(self, p1, p2, windows = [], doors = []):
        super().__init__(p1,p2)
        
        self.add_window(windows)
        self.add_door(doors)

    def __is_supporting(self, e):
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
            self.__windows.append(window)
        
        else:
            self.__windows = []
            
    
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
            self.__doors.append(door)
        
        else:
            self.__doors = []

