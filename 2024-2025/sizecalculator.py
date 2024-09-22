import maya.cmds as m
import math
def confirmprompt(message:str,buttons:str|list,title:str = "confirm"):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )
"""measure start"""
def distanceTo(point1:list,point2:list):
    #this is intende to work with the pointposition command and only really works with lists with a size of 3
    point1X = point1[0]
    point1Y = point1[1]
    point1Z = point1[2]

    point2X = point2[0]
    point2Y = point2[1]
    point2Z = point2[2]
    
    distX = (point2X-point1X)
    distY = (point2Y-point1Y)
    distZ = (point2Z-point1Z)

    distance = math.sqrt((distX**2)+(distY**2)+(distZ**2))
    return distance


def measure():
    selections = m.ls(sl=1)
    objects = {}
    for i in selections:
        objects[i] = m.ls(f"{i}.vtx[*]",fl=1)
    # print(objects)

    if selections == []:
        confirmprompt("select something","ok","nothing selected")

    for i in objects.keys():
        vertices = objects[i]
        xcoords = []
        ycoords = []
        zcoords = []

        for vertex in vertices:
            position = m.pointPosition(vertex,w=1)
            xcoords.append(position[0])
            ycoords.append(position[1])
            zcoords.append(position[2])
        # width is x depthis z
        width = max(xcoords)-min(xcoords)
        height = max(ycoords)-min(ycoords)
        depth  = max(zcoords)-min(zcoords)

        print(f"""{i} measurements: \n width {width} \n height {height} \n depth {depth}""")


measure()

def truemeasure():
    # this is just measuring without rotation or scale
    selections = m.ls(sl=1)
    if selections == []:
        confirmprompt("select something","ok","nothing selected")

    for i in selections:
        m.duplicate(i,n=f"noScale_noRotate_{i}")
        m.setAttr(f"noScale_noRotate_{i}.rotate",0,0,0)
        m.setAttr(f"noScale_noRotate_{i}.scale",1,1,1)
        measure()
        m.delete()

truemeasure()
        



"""measure end"""

"""ruler start"""

def placeruler():
    selections = m.ls(sl=1)
    objects = {}
    for i in selections:
        objects[i] = m.ls(f"{i}.vtx[*]",fl=1)
    # print(objects)

    if selections == []:
        confirmprompt("select something","ok","nothing selected")


    for i in objects.keys():
        vertices = objects[i]

        xcoords = []
        ycoords = []
        zcoords = []

        for vertex in vertices:
            position = m.pointPosition(vertex,w=1)
            xcoords.append(position[0])
            ycoords.append(position[1])
            zcoords.append(position[2])

        fc = [min(xcoords),min(ycoords),min(zcoords)]
        reach = [max(xcoords),max(ycoords),max(zcoords)]

        height = m.distanceDimension(sp=[fc[0],fc[1],fc[2]],ep=[fc[0],reach[1],fc[2]])
        width = m.distanceDimension(sp=[fc[0],fc[1],fc[2]],ep=[fc[0],fc[1],reach[2]])
        depth = m.distanceDimension(sp=[fc[0],fc[1],fc[2]],ep=[reach[0],fc[1],fc[2]])
        
    m.select(cl=1)
placeruler()

"""ruler end """