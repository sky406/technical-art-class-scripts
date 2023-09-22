import maya.cmds as m
# a few functions to make this cleaner
def txtprompt(message,buttons,title,defaulttxt="n/a"):
    # this simply makes prompt dialogue quickly, 
    # small reminder, buttons can be a liist
    m.promptDialog(
        m=message,
        b=buttons,
        t=title,
        tx=defaulttxt
    )
    return m.promptDialog(q=True,tx=True)

def confirmprompt(message,buttons,title):
    # same as txt prompt but uses a confirm dialogue that returns just the button clicked
    return m.confirmDialog(
        m=message,
        b=buttons,
        t=title
    )

"""part 1 making the primitive"""

# the part makes the primitive and marks its values
discName = txtprompt("please name your torus","next","torus maker",defaulttxt="donut")
discRad  = float(txtprompt("what is the radius of this torus","next","torus maker",defaulttxt="1"))
discSecRad = float(txtprompt("what is the inner radius of your torus","next","torus maker",defaulttxt="0.5"))
discSubDivX = int(txtprompt("how many x subdividions does this have","Done","torus maker",defaulttxt="1"))
discSubDivY = int(txtprompt("how many y subdividions does this have","Done","torus maker",defaulttxt="1"))

disc = m.polyTorus(
    n=discName,
    r=discRad,
    sr=discSecRad,
    sx=discSubDivX,
    sy=discSubDivY
    )
#### get postitions and store them
def getattributes():
    attributes = {
        "xpos":float(m.getAttr(f"{discName}.translateX")),
        "ypos":float(m.getAttr(f"{discName}.translateY")),
        "zpos":float(m.getAttr(f"{discName}.translateZ")),
        "xrot":float(m.getAttr(f"{discName}.rotateX")),
        "yrot":float(m.getAttr(f"{discName}.rotateY")),
        "zrot":float(m.getAttr(f"{discName}.rotateZ"))
    }
    return attributes
discAttributes = getattributes()



"""part 2 manipulating the torus"""

# this part moves the primitive (this part only needs to be run once)
def moveDisk(attributes,primitive):
    direction = confirmprompt("what direction do you want to move the torus",["x","y","z"],"torus mover")
    ammount = float(txtprompt("how much do you want to move the torus","Done","torus mover",defaulttxt="0"))

    if direction == "x":
        m.move(ammount+attributes["xpos"],attributes["ypos"],attributes["zpos"],primitive)
    elif direction == "y":
        m.move(attributes["xpos"],ammount+attributes["ypos"],attributes["zpos"],primitive)
    else:
        m.move(attributes["xpos"],attributes["ypos"],ammount+attributes["zpos"],primitive)
    newAttributes = (getattributes())
    return newAttributes

discAttributes = moveDisk(discAttributes,discName) #once the function is in memory you can just run this part

# this part rotates the primitive

def rotateDisk(attributes,primitive):
    direction = confirmprompt("what axis do you want to rotate the torus on",["x","y","z"],"torus rotater")
    ammount = float(txtprompt("how much do you want to rotate the torus","Done","torus mover",defaulttxt="0"))

    if direction == "x":
        m.rotate(ammount+attributes["xrot"],attributes["yrot"],attributes["zrot"],primitive)
    elif direction == "y":
        m.rotate(attributes["xrot"],ammount+attributes["yrot"],attributes["zrot"],primitive)
    else:
        m.rotate(attributes["xrot"],attributes["yrot"],ammount+attributes["zrot"],primitive)
    return getattributes()

discAttributes = rotateDisk(discAttributes,discName) #once the function is in memory you can just run this part
