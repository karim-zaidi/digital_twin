class Zone():

    __id = 0

    def __init__(self):
        self.__id = Zone.__id
        Zone.__id += 1
        self.is_component = False

   
    # id
    @property
    def id(self):
        return self.__id