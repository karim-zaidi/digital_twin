from Element import Element
from Window import Window
from Door import Door

class Wall(Element):

    def __init__(self, p1, p2, windows = [], doors = []):
        super().__init__(p1,p2)
        self.windows = windows
        self.doors = doors

    def is_on_top_of(self, e):
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
        if wall_y_coords[0] == wall_y_coords[1]: # If the wall is parallel to the x axis, ie. if its two y coords are the same
            if e_y_coords[0] != e_y_coords[1]: # If the element isn't parallel to the x axis return False
                return False
            elif e_y_coords[0] != wall_y_coords[0]: # If the element isn't aligned with the wall return False
                return False
            return True

    def add_window(self, window):
        assert isinstance(window, Window), 'add_window function takes a window as argument'
        assert self.is_on_top_of(window), 'The window is not on the wall'
        self.windows.append(window)

    def add_door(self, door):
        assert isinstance(door, Door), 'add_door function takes a door as argument'
        assert self.is_on_top_of(door), 'The door is not on the wall'
        self.doors.append(door)

