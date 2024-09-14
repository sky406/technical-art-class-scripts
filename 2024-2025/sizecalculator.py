import maya.cmds as m
def confirmprompt(message:str,buttons:str|list,title:str = "confirm"):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )

selections = m.ls(sl=1)
objects = {}
for i in selections:
    objects[i] = m.ls(f"{i}.vtx[*]",fl=1)
print(objects)

if selections == []:
    confirmprompt("select something","ok","nothing selected")

def measure():
    for i in objects.keys():
        vertices = objects[i]
        xyzmax = [0,0,0]
        xyzmin = [0,0,0]

        for vertex in vertices:
            position = m.pointPosition(vertex,l=1)
            # print(position)
            count = 0
            for coordinate in position:
                if position[count]>xyzmax[count]:
                    xyzmax[count] = position[count]
                if position[count]<xyzmin[count]:
                    xyzmin[count] = position[count]
                count+=1
            
        print(f"xyz max = {xyzmax}  and xyz min = {xyzmin}")

        xsize = xyzmax[0]-xyzmin[0]
        ysize = xyzmax[1]-xyzmin[1]
        zsize = xyzmax[2]-xyzmin[2]

        print (f"""{i}'s dimensions are 
        \n height:{round(ysize,2)} 
        \n width:{round(xsize,2)} 
        \n depth:{round(zsize,2)}""")

measure()