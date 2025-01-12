import maya.cmds as m
# ruler placer
def confirmprompt(message:str,buttons:str|list,title:str = "confirm"):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )
# places rulers around the bounding box of a shape 
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