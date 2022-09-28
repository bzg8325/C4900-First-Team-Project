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


def test_answer():
    x1 = 2
    x2 = -2
    y1 = 1
    y2 = -1

    #create two new point objects
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    #create a line object
    line1 = Line(p1, p2)

    x3 = 0
    x4 = 0
    y3 = -4
    y4 = 2

    #create two new point objects
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    #create a line object
    line2 = Line(p3, p4)

    pf = Point(0, 0)

    assert intersect(line1, line2).get_x() == pf.get_x()
    assert intersect(line1, line2).get_y() == pf.get_y()

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
    
#create a line class that has a start and end point
class Line:
    #constructor
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    