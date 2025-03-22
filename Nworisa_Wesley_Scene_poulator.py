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
    def pivCornerRadius(side):
        match side:    
            case "x":
                m.move(width,-0.5*height,0,scalepiv,rotpiv)
            
            case "z":
                m.move(0,-0.5*height,depth,scalepiv,rotpiv)
    def pivCorner(side):
        match side:    
            case "x":
                m.move(0.5*width,-0.5*height,0,scalepiv,rotpiv)
            
            case "z":
                m.move(0,-0.5*height,-0.5*depth,scalepiv,rotpiv)

    match position:
        case "bottom":
            pivDown()
        case "cornerradX":
            pivCornerRadius("x")
        case "cornerradZ":
            pivCornerRadius("z")
        case "cornerX":
            pivCorner("x")
        case "cornerZ":
            pivCorner("z")

def baseToCenter(shape,height):
    m.move(0,0.5*height,0,shape)

def coneToside(cone,height,radius):
    coneangle = mat.degrees(mat.atan(height/radius))
    rotangle = 180-coneangle
    pivotMove(cone,"cornerradX",height,radius,None)
    m.rotate(0,0,-rotangle,cone[0])
    resetRotation(cone)
    # baseToCenter(cone,height)

def resetRotation(shape):
    m.makeIdentity(shape[0],r=1,a=1)

def rot90(shape,axis:str,height,width,depth,isCube):
    if isCube:
        match axis:
            case "x":
                pivotMove(shape,"cornerX",height,width,depth)
                m.rotate(0,0,-90,shape[0])
                
            case "z":
                pivotMove(shape,"cornerZ",height,width,depth)
                m.rotate(-90,0,0,shape[0])
    else:
        match axis:
            case "x":
                pivotMove(shape,"cornerradX",height,width,depth)
                m.rotate(0,0,-90,shape[0])
                
            case "z":
                pivotMove(shape,"cornerradZ",height,width,depth)
                m.rotate(-90,0,0,shape[0])
                
    resetRotation(shape)


def CreateBlacklistdict(shape):
    bbox = m.exactWorldBoundingBox(shape[0])
    xmin = bbox[0]
    zmin = bbox[2]
    xmax = bbox[3]
    zmax = bbox[5]
    dict = {
        "xmin":xmin,
        "xmax":xmax,
        "zmin":zmin,
        "zmax":zmax,
    }
    return dict


def checkcollisions(shape,blacklist):
    collisionFound = False
    shapeBbox = CreateBlacklistdict(shape)
    def isbetween(target,lowerbound,upperbound):
        return target>=lowerbound and target<=upperbound
    for Bbox in blacklist:
        xPos = isbetween(shapeBbox["xmax"],Bbox["xmin"],Bbox["xmin"])
        xNeg = isbetween(shapeBbox["xmin"],Bbox["xmin"],Bbox["xmax"])
        zPos = isbetween(shapeBbox["zmax"],Bbox["zmin"],Bbox["zmax"])
        zNeg = isbetween(shapeBbox["zmin"],Bbox["zmin"],Bbox["zmax"])
        if (xPos or xNeg) and (zPos or zNeg) :
            collisionFound=True
            print(f"collision detected {shape[0]}")
            moveX = 0
            moveZ = 0
            # i know it is confusing but i've already commited to the poitive negative x, it caould be changed later if i have time 
            posXdistance = shapeBbox["xmax"]-Bbox["xmin"]
            negXdistance = Bbox["xmax"]-shapeBbox["xmin"]

            posZdistance = shapeBbox["zmax"]-Bbox["zmin"]
            negZdistance = Bbox["zmax"]-Bbox["zmin"]
            if xPos and xNeg:    
                if posXdistance < negXdistance:
                    moveX = -posXdistance
                else:
                    moveX = negXdistance
            elif xPos:
                moveX = -posXdistance
            else:
                moveX = negXdistance
            
            if zPos and zNeg:    
                if posXdistance < negZdistance:
                    moveZ = -posZdistance
                else:
                    moveZ = negZdistance
            elif xPos:
                moveZ = -posZdistance
            else:
                moveZ = negZdistance
            m.move(moveX*2,0,moveZ*2,shape[0],r=1)
    if collisionFound:
        checkcollisions(shape,blacklist)
    #probabbly not work working on maybe will reitterate later 
    
        


def createShapes(type:str,number:int,spreadRange,scaleRange,height,width,depth):
    collisionBlacklist = []
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
                rot90(shape,choice(["x","z"]),height,width,depth,True)
            else: 
                rot90(shape,"x",height,width,depth,False)
        else:
            pivotMove(shape,"bottom",height,width,depth)
        baseToCenter(shape,height)
        m.rotate(0,uniform(-360,360),0,shape[0])       
        

        #scale the shapes
        scale = uniform(1,scaleRange)
        m.scale(scale,scale,scale,shape[0])
        
        # scatter the shapes

        def randomposition():
            return uniform(-spreadRange,spreadRange)
        
        m.move(randomposition(),0,randomposition(),shape[0],r=1)
        if collisionBlacklist == []:
            collisionBlacklist.append(CreateBlacklistdict(shape))
            print("first bbox added")
        else:
            m.xform(shape[0],cp=1) #center pivots
            checkcollisions(shape,collisionBlacklist)
            collisionBlacklist.append(CreateBlacklistdict(shape))
        
        
#test call please ignore           
createShapes("cube",30,900,12,9,6,2)
