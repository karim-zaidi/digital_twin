from abc import abstractmethod
from Zone import Zone
from Area import Area
import numpy as np

class AtomicZone(Zone):

    def __init__(self):
        self.areas = []
        self.polygon = []

    def get_areas(self):
        return self.areas

    def get_polygon(self):
        return self.polygon

    def add_area(self, area):
        assert isinstance(area, Area)
        self.areas.append(area)

    def set_polygon(self, polygon):
        assert isinstance(polygon, (list,tuple))
        for p in polygon:
            assert isinstance(p, (list,tuple))
            for coord in p:
                assert isinstance(coord, (float,int))
        assert AtomicZone.check_valid(polygon), 'The polygon is not valid'
        self.polygon = polygon

    @staticmethod
    def check_valid(pts):
        n = len(pts)
        for i in range(n):
            if AtomicZone.angle(pts[i-2],pts[i-1],pts[i]) == 0:
                return False
        segments = [(pts[i-1],pts[i]) for i in range(n)]
        # Testing each segment against the others (except its two neighbors) for an intersection point, which are forbidden
        for i in range(n-2):
            for j in range(i+2,n): # Tests for j<i have already been done (symmetry of the test)
                if (i,j) != (0,n-1): # So as not to test the first segment against the last one, since they are neighbors
                    if AtomicZone.check_secant(segments[i],segments[j]):
                        print('Forbidden: these two segments are secant: '+str((segments[i],segments[j])))
                        return False
        return True

    @staticmethod
    def check_secant(s1,s2):
        """Returns if the two segments have any point in common (ie. shared vertex, itersection point, etc...)"""
        #xij = x coord for segment i, point j 
        x11 = s1[0][0]
        x12 = s1[1][0]
        if x11 > x12:
            x11,x12 = x12,x11
        x21 = s2[0][0]
        x22 = s2[1][0]
        if x21 > x22:
            x21,x22 = x22,x21

        # Checking is s1 and s2 even share x values
        if x12 < x21:
            return False
        if x22 < x11:
            return False

        # Checking if either s1 or s2 is vertical and handling such cases
        if x11 == x12: # If s1 is vertical
            y11 = min(s1[0][1],s1[1][1])
            y12 = max(s1[0][1],s1[1][1])
            if x21 == x22: # If s2 is vertical
                if x11 != x21: # If they're not aligned
                    return False
                # If they are aligned, let's test if they share y values
                y21 = min(s2[0][1],s2[1][1])
                y22 = max(s2[0][1],s2[1][1])
                return y21<=y12<=y22 or y11<=y22<=y12
            else: #s2 is not vertical
                t = (x11-x21)/(x22-x21)
                y2 = t*s2[1][1] + (1-t)*s2[0][1]
                return y11<=y2<=y12
        if x21 == x22: # Uf s2 is vertical (and we know that s1 isn't)
            y21 = min(s2[0][1],s2[1][1])
            y22 = max(s2[0][1],s2[1][1])
            t = (x21-x11)/(x12-x11)
            y1 = t*s1[1][1] + (1-t)*s1[0][1]
            return y21<=y1<=y22

        # We now know that s1 and s2 share x values and that neither is vertical
        if x11 >= x21:
            y11 = s1[0][1]
            t = (x11-x21)/(x22-x21)
            y21 = t*s2[1][1] + (1-t)*s2[0][1]
        else:
            y21 = s2[0][1]
            t = (x21-x11)/(x12-x11)
            y11 = t*s1[1][1] + (1-t)*s1[0][1]

        if x12 <= x22:
            y12 = s1[1][1]
            t = (x22-x12)/(x22-x21)
            y22 = t*s2[0][1] + (1-t)*s2[1][1]
        else:
            y22 = s2[1][1]
            t = (x12-x22)/(x12-x11)
            y12 = t*s1[0][1] + (1-t)*s1[1][1]

        return (y11>=y21 and y12<=y22) or (y11<=y21 and y12>=y22)

    @staticmethod
    def angle(p1, p2, p3):
        """Return the oriented angle p1-p2-p3, ie the oriented angle between vectors p1-p2 and p3-p2
        
        param: p1 (tuple of two floats): first point
        param: p2 (tuple of two floats): second point
        param: p3 (tuple of two floats): third point

        returns: angle p1-p2-p3 (int): in degrees, in [-180;180]
        """
        point1 = np.subtract(p1, p2) # p1-p2 ie vector from p2 to p1
        point2 = np.subtract(p3, p2) # p3-p2 ie vector from p2 to p3
        a1 = np.arctan2(point1[1], point1[0])
        a2 = np.arctan2(point2[1], point2[0])
        ang = (a2-a1)*180/np.pi
        if ang < -180:
            return ang+360
        elif ang > 180:
            return ang-360
        else:
            return ang

    