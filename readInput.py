import rhinoscriptsyntax as rs

buildings = [] #Set of buildings
plot = [] #Plot points

##
# Translate 2 diagonal points into the 8 box coordinates
def cornersToBox(p1, p2):
    return [(p1[0],p1[1],p1[2]),(p2[0],p1[1],p1[2]),(p2[0],p2[1],p1[2]),(p1[0],p2[1],p1[2]),(p1[0],p1[1],p2[2]),(p2[0],p1[1],p2[2]),(p2[0],p2[1],p2[2]),(p1[0],p2[1],p2[2])]

##
# Read from file and draw it's contents
def readFile():
    f = open('test1.txt', 'r')
    for line in f:
        if(line == 'Building\n'): #Buildings have 2 3D points and a rotation in degrees
            p1 = f.readline().rstrip().split(",")
            p2 = f.readline().rstrip().split(",")
            rot = f.readline().rstrip()
            drawBox(p1, p2, rot)
        if(line == "Plot\n"): #Plot has 2 3D points
            p1 = f.readline().rstrip().split(",")
            p2 = f.readline().rstrip().split(",")
            plot.append(p1)
            plot.append(p2)
            drawPlot(p1, p2)
    f.close()

##
# Draw a box given 2 diagonal points and rotation in degrees
def drawBox(p1, p2, rot):
    box = cornersToBox(p1,p2)
    center = rs.PointDivide(rs.PointAdd(p1,p2), 2)
    xform = rs.XformRotation2(float(rot), (0,0,1), center)
    newBox = []
    for point in box:
        newBox.append(rs.PointTransform(point, xform))
    rs.AddBox(newBox)
    buildings.append(newBox)

##
# Draw a rectangle given 2 points
def drawPlot(p1, p2):
    rs.AddLine(p1, (p1[0], p2[1], p1[2]))
    rs.AddLine(p1, (p2[0], p1[1], p1[2]))
    rs.AddLine(p2, (p1[0], p2[1], p1[2]))
    rs.AddLine(p2, (p2[0], p1[1], p1[2]))

#def findClosestEdges(p1, p2):
#    for building in buildings:
#        for point in building:
#            

readFile()
