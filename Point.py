class P():

    def __init__(self,x,y):
        assert isinstance(x,(int,float)) and (isinstance(y,(int,float))), 'x and y must be int or float'
        self.__x = x
        self.__y = y

    
    @property
    def x(self):
        return self.__x


    @property
    def y(self):
        return self.__y

    
    # Methods
    def get_coords(self):
        return (self.x,self.y)