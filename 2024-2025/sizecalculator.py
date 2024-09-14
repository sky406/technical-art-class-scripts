import maya.cmds as m
def confirmprompt(message:str,buttons:str|list,title:str = "confirm"):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )
"""measure start"""

def measure():
    selections = m.ls(sl=1)
    objects = {}
    for i in selections:
        objects[i] = m.ls(f"{i}.vtx[*]",fl=1)
    print(objects)

    if selections == []:
        confirmprompt("select something","ok","nothing selected")


    for i in objects.keys():
        vertices = objects[i]
        xyzmax = [0,0,0]
        xyzmin = [0,0,0]

        for vertex in vertices:
            position = m.pointPosition(vertex,l=1)
            print(position)
            count = 0
            for coordinate in position:
                if position[count]>xyzmax[count]:
                    xyzmax[count] = position[count]
                if position[count]<xyzmin[count]:
                    xyzmin[count] = position[count]
                count+=1
            
        print(f"xyz max = {xyzmax}  and xyz min = {xyzmin}")

        xsize = xyzmax[0]-xyzmin[0] * m.getAttr(f"""{i}.scaleX""")
        ysize = xyzmax[1]-xyzmin[1] * m.getAttr(f"""{i}.scaleY""")
        zsize = xyzmax[2]-xyzmin[2] * m.getAttr(f"""{i}.scaleZ""")

        print (f"""{i}'s dimensions are 
        \n height:{round(ysize,3)} 
        \n width(x):{round(xsize,3)} 
        \n depth(z):{round(zsize,3)}""")

measure()

"""measure end"""

"""ruler start"""

def placeruler():
    selections = m.ls(sl=1)
    objects = {}
    for i in selections:
        objects[i] = m.ls(f"{i}.vtx[*]",fl=1)
    print(objects)

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
        
placeruler()

"""ruleer end """