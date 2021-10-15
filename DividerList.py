from Wall import Wall
from Boundary import Boundary

class DividerList():

    def __init__(self, list = []):
        self.list = list

    def add_divider(self, divider):
        assert isinstance(divider, Wall) or isinstance(divider, Boundary), 'The new divider has to be a wall or a boundary'
        self.list.append(divider)