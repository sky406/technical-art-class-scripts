objects = m.ls(sl=1,fl=1)
print(objects)
m.getAttr("idk.translateX")
for i in objects:
    #this getsthe position of verticies 
    print(m.pointPosition(i,l=1))