import shapes
from scipy.spatial import Voronoi

#TODO 
#User input/interaction needs to be added
#Potentially give a list of methods to choose from
#Then ask for the input int by int in order to 
#populate the data structure needed for each method

#Fully functional and finalized method ✓
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
        return shapes.Point(-999, -999)
    else:
        #finalize point
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant

    p = shapes.Point(x, y)
    return p

#TODO
def convex_hull(points):
    return points

#Temp
def closest_pair(points):
    #initialize variables
    min_distance = 999999
    p1 = shapes.Point(0, 0)
    p2 = shapes.Point(0, 0)

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

    return shapes.Line(p1, p2)

#Seems functional however needs convex hull method to be tested thoroughly
def largest_circle(points):
    voronoi = Voronoi(points)
    max_radius = 0
    for i in range(len(voronoi.vertices)):
        #create circle from point and check if all other points are outside of circle
        temp_radius = shapes.closest_point(points, voronoi.vertices[i]).distance(shapes.Point(voronoi.vertices[i]))
        c = shapes.Circle(shapes.Point(voronoi.vertices[i]), temp_radius)
        for p in points:
            if c.contains(shapes.Point(p)) == True:
                continue
        if convex_hull(points).contains(c.p) == False:
            continue
        #check if circle is larger than current max
        if (c.r > max_radius):
            max_radius = c.r
            max_circle = c
    return max_circle

#Placeholder test, currently only tests the intersect method
#TODO
#Add merged test cases for each method | Add more test cases
#Intersect      ✓ | X
#Convex Hull    X | X
#Closest Pair   ✓ | X
#Largest Circle X | X
def test_answer():
    x1 = 2
    x2 = -2
    y1 = 1
    y2 = -1

    #create two new point objects
    p1 = shapes.Point(x1, y1)
    p2 = shapes.Point(x2, y2)

    #create a line object
    line1 = shapes.Line(p1, p2)

    x3 = 0
    x4 = 0
    y3 = -4
    y4 = 2

    #create two new point objects
    p3 = shapes.Point(x3, y3)
    p4 = shapes.Point(x4, y4)

    #create a line object
    line2 = shapes.Line(p3, p4)

    pf = shapes.Point(0, 0)

    assert intersect(line1, line2).get_x() == pf.get_x()
    assert intersect(line1, line2).get_y() == pf.get_y()

    points = shapes.create_points([100, 0, -100, 1, 50, 2])
    assert closest_pair(points).get_p1().get_x() == points[0].get_x()
    assert closest_pair(points).get_p1().get_y() == points[0].get_y()
    assert closest_pair(points).get_p2().get_x() == points[2].get_x()
    assert closest_pair(points).get_p2().get_y() == points[2].get_y()

    # if multiple pairs have the same closest distance, choose the first pair
    points = shapes.create_points([0, 0, 0, 1, 1, 0])
    assert closest_pair(points).get_p1().get_x() == points[0].get_x()
    assert closest_pair(points).get_p1().get_y() == points[0].get_y()
    assert closest_pair(points).get_p2().get_x() == points[1].get_x()
    assert closest_pair(points).get_p2().get_y() == points[1].get_y()
