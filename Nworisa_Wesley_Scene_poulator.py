import maya.cmds as m
from random import uniform, randrange, choice
import math as mat


def pivotMove(shape,position,height,width,depth):
    # m.select(f"{shape[0]}.scalePivot",f"{shape[0]}.rotatePivot")
    # moves the pivot to a more convienient position for controllign the rotation
    scalepiv = f"{shape[0]}.scalePivot"
    rotpiv = f"{shape[0]}.rotatePivot"
    def pivDown():
        m.move(0,-0.5*height,0,scalepiv,rotpiv,r=1)
        print("moved")
    def pivSide():
        m.move(0.5*width,0,0,scalepiv,rotpiv,r=1)
        print("moved side")
    def pivCorner(side):
        match side:    
            case "x":
                m.move(width,-0.5*height,0,scalepiv,rotpiv)
            
            case "z":
                m.move(0,-0.5*height,depth,scalepiv,rotpiv)

    match position:
        case "bottom":
            pivDown()
        case "side":
            pivSide()
        case "cornerX":
            pivCorner("x")
        case "cornerZ":
            pivCorner("z")

def baseToCenter(shape,height):
    m.move(0,0.5*height,0,shape)

def coneToside(cone,height,radius):
    coneangle = mat.degrees(mat.atan(height/radius))
    rotangle = 180-coneangle
    pivotMove(cone,"cornerX",height,radius,None)
    m.rotate(0,0,-rotangle,cone[0])
    resetRotation(cone)
    # baseToCenter(cone,height)

def resetRotation(shape):
    m.makeIdentity(shape[0],r=1,a=1)

def rot90(shape,axis:str,height,width,depth):
    match axis:
        case "x":
            pivotMove(shape,"cornerX",height,width,depth)
            m.rotate(0,0,-90,shape[0])
            
        case "z":
            pivotMove(shape,"cornerZ",height,width,depth)
            m.rotate(-90,0,0,shape[0])
            
    resetRotation(shape)

def createArray(arrayrange:int):
    array = []
    for x in range(-arrayrange,arrayrange,1):
        for y in range(-arrayrange,arrayrange,1):
            array.append([x,y])
    print(array)
    return array

def addToCollisionBlacklist(shape,blacklist:list):
    bbox = m.exactWorldBoundingBox(shape[0])
    xmin = bbox[0]
    zmin = bbox[2]
    xmax = bbox[3]
    zmax = bbox[5]
    print(f"{int(xmax)}<>{int(xmin)} , {int(zmax)}<>{int(zmin)}")
    for x in range(int(xmin),int(xmax)):
        for y in range(int(zmin),int(zmax)):
            if [x,y] not in blacklist:
                blacklist.append([x,y])
    return blacklist

def isColliding():
    pass




def createShapes(type:str,number:int,spreadRange,scaleRange,height,width,depth):
    for i in range(number):
        match type:
            case "cube":
                shape = m.polyCube(n="box",h=height,w=width,d=depth)
            case "cone":
                shape = m.polyCone(n="cone",h=height,r=width)
            case "cylinder":
                shape = m.polyCylinder(n="cylinder",h=height,r=width)
        # setting the rotations
        rotatestate = choice(["side","upright"])
        if rotatestate == "side":
            if type =="cone":
                coneToside(shape,height,width)
            elif type =="cube":
                rot90(shape,choice(["x","z"]),height,width,depth)
            else: 
                rot90(shape,"x",height,width,depth)
        else:
            pivotMove(shape,"bottom",height,width,depth)
        baseToCenter(shape,height)
        m.rotate(0,uniform(-360,360),0,shape[0])       
        

        #scale the shapes
        scale = uniform(1,scaleRange)
        m.scale(scale,scale,scale,shape[0])
        
        # scatter the shapes
        collisionBlacklist = []

        def randomposition():
            return uniform(-spreadRange,spreadRange)
        m.move(randomposition(),0,randomposition(),shape[0],r=1)
        collisionBlacklist = addToCollisionBlacklist(shape,collisionBlacklist)
        
#test call please ignore           
createShapes("cylinder",30,900,12,9,6,2)