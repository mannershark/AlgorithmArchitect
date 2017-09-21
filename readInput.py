import rhinoscriptsyntax as rs
from itertools import izip, islice

buildings = [] #Set of buildings
plot = [] #Plot points
closestEdges = [] #Closest edge for each building to the plot

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
            createBox(p1,p2,rot)
        if(line == "Plot\n"): #Plot has 2 3D points
            p1 = f.readline().rstrip().split(",")
            p2 = f.readline().rstrip().split(",")
            plot.append(p1)
            plot.append(p2)
            drawPlot(p1, p2)
    f.close()

##
# Translate 2 points and rotation to 8 box coordinates
def createBox(p1,p2,rot):
    box = cornersToBox(p1,p2)
    center = rs.PointDivide(rs.PointAdd(p1,p2), 2)
    xform = rs.XformRotation2(float(rot), (0,0,1), center)
    newBox = []
    for point in box:
        newBox.append(rs.PointTransform(point, xform))
    buildings.append(newBox)
    return newBox

##
# Draws set of buildings
def drawBuildings(buildings):
    for box in buildings:
        rs.AddBox(box)


##
# Draw a rectangle given 2 points
def drawPlot(p1, p2):
    rs.AddLine(p1, (p1[0], p2[1], p1[2]))
    rs.AddLine(p1, (p2[0], p1[1], p1[2]))
    rs.AddLine(p2, (p1[0], p2[1], p1[2]))
    rs.AddLine(p2, (p2[0], p1[1], p1[2]))

##
# Finds the closest edge for all buildings and adds it to closestEdges
def findClosestEdges(p1, p2):
    for building in buildings:
        for edge in getEdges(building):
            min = float("Inf")
            dist = rs.LineMinDistanceTo(edge, rs.PointDivide(rs.PointAdd(p1, p2),2))
            closest = None
            if(dist < min):
                min = dist
                closest = edge
            closestEdges.append(edge)

##
# Returns 4 lines that define the base of the building
def getEdges(building):
    edges = []
    for bp1,bp2 in izip(building, islice(building,1,4)): #only take edges from base
        edges.append([bp1, bp2])
    edges.append([building[3], building[0]])
    return edges

readFile()
drawBuildings(buildings)
findClosestEdges(plot[0],plot[1])
