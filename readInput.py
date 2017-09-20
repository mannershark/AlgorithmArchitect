import rhinoscriptsyntax as rs

def cornersToBox(x, y):
    return [(x[0],x[1],x[2]),(y[0],x[1],x[2]),(y[0],y[1],x[2]),(x[0],y[1],x[2]),(x[0],x[1],y[2]),(y[0],x[1],y[2]),(y[0],y[1],y[2]),(x[0],y[1],y[2])]

f = open('test1.txt', 'r')
for line in f:
    if(line == 'Building\n'):
        print(type(f.readline))
        x = f.readline().rstrip().split(",")
        y = f.readline().rstrip().split(",")
        print(x)
        print(rs.IsPoint(x))
        box = cornersToBox(x,y)
        center = rs.PointDivide(rs.PointAdd(x,y), 2)
        xform = rs.XformRotation2(45, (0,0,1), center)
        newBox = []
        for point in box:
            newBox.append(rs.PointTransform(point, xform))
        rs.AddBox(newBox)
f.close()

