import math

def intersect(line1, line2):
    #calculate intersection point
    a1 = line1.p2.y - line1.p1.y
    b1 = line1.p1.x - line1.p2.x
    c1 = a1*(line1.p1.x) + b1*(line1.p1.y)
 
    a2 = line2.p2.y - line2.p1.y
    b2 = line2.p1.x - line2.p2.x
    c2 = a2*(line2.p1.x)+ b2*(line2.p1.y)
 
    determinant = a1*b2 - a2*b1

    if (determinant == 0):
        #no intersection
        return Point(-999, -999)
    else:
        #finalize point
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant

    p = Point(x, y)
    return p

#method that given a list of points, finds the two points closest togeather
def closest_pair(points):
    #initialize variables
    min_distance = 999999
    p1 = Point(0, 0)
    p2 = Point(0, 0)

    #go through list of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            #calculate distance between points
            distance = points[i].distance(points[j])
            #check if distance is less than current minimum
            if distance < min_distance:
                min_distance = distance
                p1 = points[i]
                p2 = points[j]

    return Line(p1, p2)

#General Algorithim from https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
#Given a list of points find the convex hull
def convex_hull(points):

    return

#given a list of points find the largest circle within the points convex hull
# def largest_circle(points):
#     hull = convex_hull(points)

#     return Circle(Point(x, y), radius)


def test_answer():
    hull_points = [Point(0, 0), Point(1, 2), Point(-1, -2),
                   Point(-1, 2), Point(1, -2)]
    hull_points2 = [Point(0, 0), Point(2, 2), Point(2, 3), Point(3, 2),
                    Point(-12, 10), Point(12, 13)]
    correct_hull = [Point(1, 2), Point(-1, -2), Point(-1, 2), Point(1, -2)]
    correct_hull2 = [Point(-12, 10), Point(12, 13), ]

    assert convex_hull(hull_points) == correct_hull
    #should make some seperate test creation method to make this simpler looking
    #should make more test cases, and a method to generate test random test cases
    #line1 = create_line(2, 1, -2, -1)
    #line2 = create_line(0, -4, 0, 2)

    #pf = Point(0, 0)

    #assert intersect(line1, line2).get_x() == pf.get_x()
    #assert intersect(line1, line2).get_y() == pf.get_y()
    #should try if we can directly compare points rather than x and y

#method that creates a line from 4 ints
def create_line(x1, y1, x2, y2):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    return Line(p1, p2)

#method that creates a list of points from a list of ints
def create_points(points):
    p = []
    for i in range(0, len(points), 2):
        p.append(Point(points[i], points[i+1]))

    return p

#create a point class that has x and y coordinates
class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #get point x coordinate
    def get_x(self):
        return self.x
    #get point y coordinate
    def get_y(self):
        return self.y
    #calculate distance between two points
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    
    
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
    def get_center(self):
        return self.p
    #get circle radius
    def get_radius(self):
        return self.r



    