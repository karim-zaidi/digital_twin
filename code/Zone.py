class Zone():

    __id = 0

    def __init__(self):
        self.__id = Zone.__id
        Zone.__id += 1
        self.__is_used = 0

   
    # id
    @property
    def id(self):
        return self.__id


    # is_used
    @property
    def is_used(self):
        return self.__is_used
    

    def is_now_used(self):
        self.__is_used += 1


    def is_no_longer_used(self):
        self.__is_used -= 1