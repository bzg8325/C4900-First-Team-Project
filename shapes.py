import math

def closest_point(points, p):
        min_distance = 999999
        closest = Point(0, 0)
        for i in range(len(points)):
            distance = Point(points[i]).distance(Point(p))
            if distance < min_distance:
                min_distance = distance
                closest = Point(points[i])
        return closest

#create a point class that has x and y coordinates
class Point:
    #constructor
    def __init__(self, *args):
        if len(args) > 1:
            self.p = [args[0], args[1]]
        else:
            self.p = args[0]

    def __getitem__(self,index):
        return self.p[index]
    #get point x coordinate
    def get_x(self):
        return self.p[0]
    #get point y coordinate
    def get_y(self):
        return self.p[1]
    #calculate distance between two points
    def distance(self, p):
        return math.sqrt((self.p[0] - p.p[0])**2 + (self.p[1] - p.p[1])**2)
    
#create a line class that has a start and end point
class Line:
    #constructor
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    #get line start point
    def get_p1(self):
        return self.p1
    #get line end point
    def get_p2(self):
        return self.p2
    #get line length
    def get_length(self):
        return self.p1.distance(self.p2)
    

#create a circle class with a point center, and an int radius
class Circle:
    #constructor
    def __init__(self, p, r):
        self.p = p
        self.r = r   
    #get circle center
    def get_p(self):
        return self.p
    #get circle radius
    def get_radius(self):
        return self.r
    #check if a point is within a circle
    def contains(self, p):
        return self.p.distance(p) <= self.r



#method that creates a list of points from a list of ints
def create_points(points):
    p = []
    for i in range(0, len(points)-1, 2):
        p.append(Point([points[i], points[i+1]]))
    return p

#get the radius and center of a circle from 3 points
def get_circle(p1, p2, p3):
    #get the slope of the line between p1 and p2
    m1 = (p2.y - p1.y)/(p2.x - p1.x)
    #get the slope of the line between p2 and p3
    m2 = (p3.y - p2.y)/(p3.x - p2.x)

    #get the center of the circle
    x = (m1*m2*(p1.y - p3.y) + m2*(p1.x + p2.x) - m1*(p2.x + p3.x))/(2* (m2 - m1))
    y = (-1*(x - (p1.x + p2.x)/2)/m1) + (p1.y + p2.y)/2

    #get the radius of the circle
    r = math.sqrt((x - p1.x)**2 + (y - p1.y)**2)

    return Circle(Point(x, y), r)