import math
import shapes
from scipy.spatial import Voronoi

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

#method that given a list of points, finds the two points closest togeather
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

#given a list of points find the convex hull
def convex_hull(points):
    return points

#given a list of points find the largest empty circle within a list of points 
def largest_circle(points):
    #max_radius = 0
    #loop through all possible combinations of 3 points and create a circle from them, then check if none of the other points are in the circle
    # for i in range(len(points)):
    #     for j in range(i+1, len(points)):
    #         for k in range(j+1, len(points)):
    #             #create circle from 3 points
    #             c = get_circle(points[i], points[j], points[k])
    #             #check if all other points are outside of circle
    #             for p in points:
    #                 if c.contains(p) == True:
    #                     return -1
    #             if convex_hull(points).contains(c.p) == False:
    #                 return -1
    #             if c.r > max_radius:
    #                 max_radius = c.r
    #                 max_circle = c
    #return max_circle
    voronoi = Voronoi(points)
    #loop through each point in the list voronoi.vertices and find the largest circle that contains none of the points

    max_radius = 0
    for i in range(len(voronoi.vertices)):
        #create circle from point and check if all other points are outside of circle
        temp_radius = closest_point(points, voronoi.vertices[i]).distance(shapes.Point(voronoi.vertices[i]))
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

def closest_point(points, p):
    min_distance = 999999
    closest = shapes.Point(0, 0)
    for i in range(len(points)):
        distance = shapes.Point(points[i]).distance(shapes.Point(p))
        if distance < min_distance:
            min_distance = distance
            closest = shapes.Point(points[i])
    return closest

def test_answer():
    #should make some seperate test creation method to make this simpler looking 
    #should make more test cases, and a method to generate test random test cases
    line1 = shapes.create_line(2, 1, -2, -1)
    line2 = shapes.create_line(0, -4, 0, 2)

    pf = shapes.Point(0, 0)

    print(largest_circle(shapes.create_points([0,2,2,0,-2,0,2,2,-2,2,-2,-2,-3,2,3,0,-3,-2])).p.get_x())
    print(largest_circle(shapes.create_points([0,2,2,0,-2,0,2,2,-2,2,-2,-2,-3,2,3,0,-3,-2])).p.get_y())
    print(largest_circle(shapes.create_points([0,2,2,0,-2,0,2,2,-2,2,-2,-2,-3,2,3,0,-3,-2])).r)

    assert largest_circle(shapes.create_points([0,2,2,0,-2,0,2,2,-2,2,-2,-2,-3,2,3,0,-3,-2])) == shapes.Circle(shapes.Point(0, 0), 2)

    assert intersect(line1, line2).get_x() == pf.get_x()
    assert intersect(line1, line2).get_y() == pf.get_y()
    #should try if we can directly compare points rather than x and y






    