from numpy.lib.arraysetops import isin


class P():

    def __init__(self,x,y):
        assert isinstance(x,(int,float)) and (isinstance(y,(int,float))), 'x and y must be int or float'
        self.__x = x
        self.__y = y

    
    # x
    @property
    def x(self):
        return self.__x

    # y
    @property
    def y(self):
        return self.__y

    
    # Methods
    def get_coords(self):
        return (self.x,self.y)


    @staticmethod
    def equal(p1,p2):
        assert isinstance(p1,P) and isinstance(p2,P)
        return p1.x == p2.x and p1.y == p2.y