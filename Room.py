from Area import Area

class Room(Area):
    
    def __init__(self, name, wall_list):
        super().__init__(name, wall_list)