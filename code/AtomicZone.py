import numpy as np

from Area import Area
from Point import P
from Zone import Zone


class AtomicZone(Zone):

    def __init__(self, area=[], polygon=[]):
        super().__init__()
        self.__areas = []
        self.add_area(area)
        self.polygon = polygon


    # areas
    @property
    def areas(self):
        return self.__areas

 
    def add_area(self, area):
        assert isinstance(area, (Area,list,tuple))
        if isinstance(area,(list,(tuple))):
            for a in area:
                self.add_area(a)
        elif isinstance(area,Area):
            assert area.is_valid_area(), 'This area is not valid, in that it does not define a rectangle'
            self.areas.append(area)


    # polygon
    @property
    def polygon(self):
        return self.__polygon


    @polygon.setter
    def polygon(self, polygon):
        assert isinstance(polygon, (list,tuple))
        for p in polygon:
            assert isinstance(p, P)
        assert AtomicZone.is_valid_polygon(polygon), 'The polygon is not valid'
        self.__polygon = polygon

    # TODO: add_polygon
    # TODO: put public method in private when necessary


    # Other methods
    def polygon_to_array(self):
        n = len(self.polygon)
        array = np.zeros((n,2))
        for i in range(n):
            array[i,0], array[i,1] = self.polygon[i].get_coords()
        return array


    @staticmethod
    def is_valid_polygon(pts):
        n = len(pts)

        if n==1 or n==2:
            return False

        # Checking that no 3 consecutive vertices define a null angle
        for i in range(n):
            if AtomicZone.angle(pts[i-2],pts[i-1],pts[i]) == 0:
                return False

        # Testing each segment against the others (except its two neighbors) for an intersection point, which is forbidden
        segments = [(pts[i-1],pts[i]) for i in range(n)]
        for i in range(n-2):
            for j in range(i+2,n): # Tests for j<i have already been done (symmetry of the test)
                if (i,j) != (0,n-1): # So as not to test the first segment against the last one, since they are neighbors
                    if AtomicZone.check_secant(segments[i],segments[j]):
                        print('Invalid polygon: these two segments are secant: '+str((segments[i],segments[j])))
                        return False
        return True


    @staticmethod
    def check_secant(s1,s2):
        """Returns if the two segments have any point in common (ie. shared vertex, itersection point, etc.)"""
        #xij = x coord for segment i, point j 
        x11 = s1[0].x
        x12 = s1[1].x
        if x11 > x12:
            x11,x12 = x12,x11
        x21 = s2[0].x
        x22 = s2[1].x
        if x21 > x22:
            x21,x22 = x22,x21

        # Checking is s1 and s2 even share x values
        if x12 < x21:
            return False
        if x22 < x11:
            return False

        # Checking if either s1 or s2 is vertical and handling such cases
        if x11 == x12: # If s1 is vertical
            y11 = min(s1[0].y,s1[1].y)
            y12 = max(s1[0].y,s1[1].y)
            if x21 == x22: # If s2 is vertical
                if x11 != x21: # If they're not aligned
                    return False
                # If they are aligned, let's test if they share y values
                y21 = min(s2[0].y,s2[1].y)
                y22 = max(s2[0].y,s2[1].y)
                return y21<=y12<=y22 or y11<=y22<=y12
            else: #s2 is not vertical
                t = (x11-x21)/(x22-x21)
                y2 = t*s2[1].y + (1-t)*s2[0].y
                return y11<=y2<=y12
        if x21 == x22: # Uf s2 is vertical (and we know that s1 isn't)
            y21 = min(s2[0].y,s2[1].y)
            y22 = max(s2[0].y,s2[1].y)
            t = (x21-x11)/(x12-x11)
            y1 = t*s1[1].y + (1-t)*s1[0].y
            return y21<=y1<=y22

        # We now know that s1 and s2 share x values and that neither is vertical
        if x11 >= x21:
            y11 = s1[0].y
            t = (x11-x21)/(x22-x21)
            y21 = t*s2[1].y + (1-t)*s2[0].y
        else:
            y21 = s2[0].y
            t = (x21-x11)/(x12-x11)
            y11 = t*s1[1].y + (1-t)*s1[0].y

        if x12 <= x22:
            y12 = s1[1].y
            t = (x22-x12)/(x22-x21)
            y22 = t*s2[0].y + (1-t)*s2[1].y
        else:
            y22 = s2[1].y
            t = (x12-x22)/(x12-x11)
            y12 = t*s1[0].y + (1-t)*s1[1].y

        return (y11>=y21 and y12<=y22) or (y11<=y21 and y12>=y22)


    @staticmethod
    def angle(p1, p2, p3):
        """Return the oriented angle p1-p2-p3, ie the oriented angle between vectors p1-p2 and p3-p2
        
        param: p1 (P): first point
        param: p2 (P): second point
        param: p3 (P): third point

        returns: angle p1-p2-p3 (float): in degrees, in [-180;180]
        """
        point1 = P(p1.x-p2.x, p1.y-p2.y) # p1-p2 ie vector from p2 to p1
        point2 = P(p3.x-p2.x, p3.y-p2.y) # p3-p2 ie vector from p2 to p3

        a1 = np.arctan2(point1.y, point1.x)
        a2 = np.arctan2(point2.y, point2.x)

        ang = (a2-a1)*180/np.pi

        if ang < -180:
            return ang+360
        elif ang > 180:
            return ang-360
        else:
            return ang

    
    def polygon_contains(self, p):
        """Return True if point p is contained in the polygon defined by consecutive vertices in pts list
        
        param: p (P): point p to check if it is inside the polygon
        
        returns: if it's inside (boolean)
        """
        pts = self.polygon
        if any(P.equal(p,pt) for pt in pts): # If p is one of the vertices, then it is 'inside' the polygon
            return True 
        epsilon = 1
        sum = 0
        for i in range(len(pts)):
            ang = AtomicZone.angle(pts[i-1], p, pts[i])
            if ang in (-180,180): # If p is between two consecutive vertices, then it is 'inside' the polygon
                return True
            sum += ang
            # print(ang)
        # print('sum of angles: %f' %s)
        return 360-epsilon<=sum<=360+epsilon or -360-epsilon<=sum<=-360+epsilon # epsilon just in case of rounding errors


    def contains(self, datapoint):
        # TODO: specify and explain the size of datapoint
        x, y = datapoint[1], datapoint[2]
        p = P(x,y)
        if any(a.contains(datapoint) for a in self.areas):
            return True
        return self.polygon_contains(p)
