# the titles determine which lines of code need to be in their own shelf
"""binding the objects (shelf start)"""
import maya.cmds as m
#this part initialized all the functions and binds the two objects
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
def getcoords(objectName:str):
    return {
        "x":m.getAttr(f"{objectName}.translateX"),
        "y":m.getAttr(f"{objectName}.translateY"),
        "z":m.getAttr(f"{objectName}.translateZ")
    }
def calculateOffset(lead,follow):
    def getAxisOffset(leadCoord:float,followCoord:float):
        return followCoord - leadCoord

    leadcoords = getcoords(lead)
    folcoords = getcoords(follow)
    offset = {
        "x":getAxisOffset(leadcoords["x"],folcoords["x"]),
        "y":getAxisOffset(leadcoords["y"],folcoords["y"]),
        "z":getAxisOffset(leadcoords["z"],folcoords["z"])
    }
    print(f"the offsets are{offset}")
    return offset
def bindObjects():
    bind = {}
    selection = m.ls(sl=True)
    if len(selection) !=2:
        confirm("please select 2 objects","OK","selection ERROR")
        return
    else:
        leader=confirm("choose your leader",selection,"bind objects")
        bind["lead"] = selection.pop(selection.index(leader))
        bind["follow"]=selection.pop(0)
        print(f"the bound objects are {bind['lead']} and {bind['follow']}")
    # check if user wants to maintain offset
    if confirm("do you want to maintain the offset",["yes","no"],"maintain offset?") == "yes":
        bind["offset"] = calculateOffset(bind["lead"],bind["follow"])
    else:
        bind["offset"] = {
            "x":0,
            "y":0,
            "z":0
        }
    return bind
boundOBjs = bindObjects()
"""shelf end"""

"""realinging the bound objects (shelf start)"""# realigning the follower with the offset
def dropClone(obj:str):
    m.duplicate(obj,st=True,n=f"{obj}.crumb")
    return None
def reAlignFollower(bind:dict):
    followercoords = getcoords(bind["follow"])
    leadercoords = getcoords(bind["lead"])
    offset = bind["offset"]
    alignedx = followercoords["x"] == leadercoords["x"] + offset["x"]
    alignedy = followercoords["y"] == leadercoords["y"] + offset["y"]
    alignedz = followercoords["z"] == leadercoords["z"] + offset["z"]

    if alignedx & alignedy & alignedz:
        confirm("follower already aligned","ok","follower aligner")
    else:
        dropClone(bind["follow"])
        m.move(leadercoords["x"]+offset["x"],leadercoords["y"]+offset["y"],leadercoords["z"]+offset["z"],bind["follow"])
        confirm("follower alinged","ok","follower aligner")
reAlignFollower(boundOBjs)
"""shelf end"""