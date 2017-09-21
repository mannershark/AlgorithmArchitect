import rhinoscriptsyntax as rs

buildings = []
plot = []

def cornersToBox(x, y):
    return [(x[0],x[1],x[2]),(y[0],x[1],x[2]),(y[0],y[1],x[2]),(x[0],y[1],x[2]),(x[0],x[1],y[2]),(y[0],x[1],y[2]),(y[0],y[1],y[2]),(x[0],y[1],y[2])]

def readFile():
    f = open('test1.txt', 'r')
    for line in f:
        if(line == 'Building\n'):
            x = f.readline().rstrip().split(",")
            y = f.readline().rstrip().split(",")
            rot = f.readline().rstrip()
            drawBox(x, y, rot)
        if(line == "Plot\n"):
            x = f.readline().rstrip().split(",")
            y = f.readline().rstrip().split(",")
            plot.append(x)
            plot.append(y)
            drawBox(x, y, 0)
    f.close()

def drawBox(x, y, rot):
    box = cornersToBox(x,y)
    center = rs.PointDivide(rs.PointAdd(x,y), 2)
    xform = rs.XformRotation2(float(rot), (0,0,1), center)
    newBox = []
    for point in box:
        newBox.append(rs.PointTransform(point, xform))
    rs.AddBox(newBox)
    buildings.append(newBox)

readFile()
