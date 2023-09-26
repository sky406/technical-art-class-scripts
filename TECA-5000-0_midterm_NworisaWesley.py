#this part initialized all the functions and binds the two objects
"""------------------------------start here--------------------------------"""
import maya.cmds as m
def prompttxt(message:str,buttons:str|list,title:str,defaulttxt:str):
    m.promptDialog(
        m = message,
        t = title,
        buttons = buttons,
        tx= defaulttxt
    )
    return m.promptDialog(q=True,tx=True)

def confirm(message:str,buttons:str|list,title:str):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )

def bindObjects():
    global boundObjs
    # first check that the appropriate number of objects are selected
    selected = m.ls(sl=True)
    if len(selected) != 2:
        confirm("please slect two objects before running","OK","Selection error")
        return boundOBjs
    else:
        # check if a set is already bound
        if boundObjs != [] and type(boundOBjs) == list:
            choice=confirm("you are about to remove your original bind are you sure",["yes","no"],"objects already bound")
            if choice == "yes":
                global boundOBjs
                boundOBjs = []
                return bindObjects()
            else:
                # quit
                return boundOBjs
        else:
            leader = confirm("which object do you want to be the leader",selected,"choose you leader")
            newbind = []
            newbind.append(selected.pop(selected.index(leader)))
            newbind.append(selected.pop())
            print(f"the new order is {newbind}")
            return newbind
def getcoords(objectName:str):
    return {
        "x":m.getAttr("{objectName}.tx"),
        "y":m.getAttr("{objectName}.ty"),
        "z":m.getAttr("{objectName}.tz")
    }

def clculateOffset(lead,follow):
    def isAhead(leadCoord:float,followCoord:float):
        return leadCoord > followCoord

    def getAxisOffset(leadCoord:float,followCoord:float):
        match isAhead(leadCoord,followCoord):
            case True:
                # convert offset to negative
                return -abs(leadCoord-followCoord)
            case False:
                # convert offset to positive
                return abs(leadCoord-followCoord)

    leadcoords = getcoords(lead)
    folcoords = getcoords(follow)
    offset = {
        "x":getAxisOffset(lead["x"],follow["y"]),
        "y":getAxisOffset(lead["y"],follow["y"]),
        "z":getAxisOffset(lead["z"],follow["z"])
    }
    print(offset)

def dropClone(obj:str):
    m.duplicate(obj,st=True,n=f"{obj}.clone")
    return


# first clear memory 
boundOBjs = []
ofset = {}