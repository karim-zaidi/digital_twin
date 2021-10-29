from Element import Element
from Window import Window
from Door import Door

class Wall(Element):

    def __init__(self, p1, p2, windows = [], doors = []):
        super().__init__(p1,p2)
        self.add_window(windows)
        self.add_door(doors)

    def is_supporting(self, e):
        assert isinstance(e, Window) or isinstance(e, Door), 'Only a door or a window can be placed on a wall'

        wall_x_coords = self.get_x_coords()
        wall_y_coords = self.get_y_coords()
        e_x_coords = e.get_x_coords()
        e_y_coords = e.get_y_coords()

        if wall_x_coords[0] == wall_x_coords[1]: # If the wall is parallel to the y axis, ie. if its two x coords are the same
            if e_x_coords[0] != e_x_coords[1]: # If the element isn't parallel to the y axis return False
                return False
            elif e_x_coords[0] != wall_x_coords[0]: # If the element isn't aligned with the wall return False
                return False
            return True
        elif wall_y_coords[0] == wall_y_coords[1]: # If the wall is parallel to the x axis, ie. if its two y coords are the same
            if e_y_coords[0] != e_y_coords[1]: # If the element isn't parallel to the x axis return False
                return False
            elif e_y_coords[0] != wall_y_coords[0]: # If the element isn't aligned with the wall return False
                return False
            return True
        else:
            print('Somehow the wall is not aligned to the x axis nor the y axis. It cannot support a door/window')
            exit(1)

    def add_window(self, window):
        if isinstance(window, (list, tuple)):
            for w in window:
                self.add_window(w)
        assert isinstance(window, Window), 'add_window function takes a window/list of windows as argument'
        assert self.is_supporting(window), 'The window is not on the wall'
        self.windows.append(window)

    def add_door(self, door):
        if isinstance(door, (list, tuple)):
            for d in door:
                self.add_door(d)
        assert isinstance(door, Door), 'add_door function takes a door/list of doors as argument'
        assert self.is_supporting(door), 'The door is not on the wall'
        self.doors.append(door)
    
    def get_doors(self):
        return self.doors
    
    def get_windows(self):
        return self.windows

