import shapes

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




    