import maya.cmds as m
from random import uniform as randF
from random import randint as randInt
from random import choice
from math import floor
import time

# default vars ===================#
"""terain variables"""
planeSizeX=10.0
planeSizeY=10.0
terainRes=10
editPerc=100

"""rock variables"""
rockRes = 3

"""randomizer variables"""
lowE_varX = 0
lowE_varY = 0 
lowE_varZ = 0 
lowE_varSize = 1 
highE_varX = 0 
highE_varY = 0 
highE_varZ = 0
highE_varSize = 1

smoothness = 0

"""selection variables"""
selectedcomponents = []
allcomponents = []

"""default names"""
terrainName = "terrain"
rockName = "OBJ_rock1"

"""additional variables"""
currentTerrain=None
animateProcess = False
animationSpeed = 0.5
maxAnimTime = 10
# ==============================#

#=====Window=====================
if m.window("terrainGen",ex=1):
    m.deleteUI("terrainGen")
mainwindow = m.window("terrainGen",t="terrainGen V0.1",s=1,wh=(400,250))
form = m.formLayout()
tabs = m.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
m.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

terraintab = m.rowColumnLayout()
"""terrain"""
terrName=m.textFieldGrp(l="terrain name",tx=terrainName)
UIterrRes = m.intSliderGrp(f=1,min=3,max=100,v=terainRes,l="resolution")
terrSize = m.floatFieldGrp(l="terrain size",v1=planeSizeX,v2=planeSizeY,nf=2)
m.button(l="generate terrain",c="generate_terrain()")
m.separator()
m.text(l="randomize terrain")
randperc=m.intSliderGrp(l="how much of the terrain should this effect",min=1,max=100)
terRangeX_upper=m.floatSliderGrp(l="upperX",v=1,min=-10,max=10)
terRangeX_lower=m.floatSliderGrp(l="lowerX",v=0,min=-10,max=10)

terRangeY_upper=m.floatSliderGrp(l="upperY",v=1,min=-10,max=10)
terRangeY_lower=m.floatSliderGrp(l="lowerY",v=0,min=-10,max=10)

terRangeZ_upper=m.floatSliderGrp(l="upperZ",v=1,min=-10,max=10)
terRangeZ_lower=m.floatSliderGrp(l="lowerZ",v=0,min=-10,max=10)

m.button(l="make random",c="randomizeTerrain()")

m.setParent( '..' )

rocktab = m.rowColumnLayout(numberOfColumns=2)
# TODO ADD rock generator here
m.setParent( '..' )

m.tabLayout( tabs, edit=True, tabLabel=((terraintab, 'Terrain'), (rocktab, 'Rocks')) )
m.showWindow()

def confirmprompt(message:str,buttons:str|list,title:str = "confirm"):
    return m.confirmDialog(
        m = message,
        b = buttons,
        t = title
    )

def generate_terrain():
    global currentTerrain
    global planeSizeX
    global planeSizeY
    global terainRes
    global terrainName

    planeSizeX = m.floatFieldGrp(terrSize,q=1,v1=1)
    planeSizeY = m.floatFieldGrp(terrSize,q=1,v2=1)
    terrainName = m.textFieldGrp(terrName,q=1,tx=1)
    terainRes = m.intSliderGrp(UIterrRes,q=1,v=1)
    # this just keeps the faces relatively square
    xres = terainRes
    yres = terainRes
    if planeSizeX != planeSizeY:
        match planeSizeX > planeSizeY:
            case True:
                yres = floor(xres*(planeSizeX/planeSizeY))
                # assert yres!=xres,"x and y res are the same"
            case False:
                xres = floor(yres*(planeSizeY/planeSizeX))
    
    if currentTerrain != None:
        delprev = confirmprompt("WARNING this action will delete your previous terrain. do you want to proceed",["yes","no"],title="delete terrain?")
        if delprev == "yes":
            m.delete(currentTerrain)
            currentTerrain = None
        else:
            return
    
    currentTerrain = m.polyPlane(w=planeSizeY,h=planeSizeX,sx=xres,sy=yres,n=terrainName)

def correctAnimtime(itteraions:int=1): #this just makes sure the animation time doesn't surpass the max animation time
    global animationSpeed
    if len(selectedcomponents)*animationSpeed*itteraions > maxAnimTime:
        animationSpeed = maxAnimTime/(len(selectedcomponents)*itteraions)
    # note to self may remove this to just have it work in randomize faces 

def randomizefaces(selected:list):
    # TODO make this use a choice of selections
    correctAnimtime()
    curFrame = 1
    for i in selected:
        # print(i)
        # m.select(i)
        shiftx = randF(lowE_varX,highE_varX)
        shifty = randF(lowE_varY,highE_varY)
        shiftz = randF(lowE_varZ,highE_varZ)
        m.move(shiftx,shifty,shiftz,i,r=1)
        if animateProcess:
            m.currentTime(curFrame)
            curFrame+=1
            time.sleep(animationSpeed)

def setrange(rangeparam:str):
    match rangeparam:
        case "X":
            global lowE_varX
            global highE_varX
            # TODO add a slider group for this
            return
        case "Y":
            global lowE_varY
            global highE_varY
            # TODO add a slider group for this
            return
        case "Z":
            global lowE_varZ
            global highE_varZ
            # TODO add a slider group for this
            return
        case"size":
            pass
def randomizeTerrain():
    global lowE_varX,lowE_varY,lowE_varZ,highE_varX,highE_varY,highE_varZ,editPerc

    m.select(f"{currentTerrain[0]}.f[*]")
    faces = m.ls(sl=1,fl=1)
    editPerc = m.intSliderGrp(randperc,q=1,v=1)
    selpoints=[]
    for i in range(0,floor(len(faces)*editPerc/100)):
        selpoints.append(faces.pop(randInt(0,len(faces)-1)))
    # TODO add softselect to make this more functional
    
    lowE_varX = m.floatSliderGrp(terRangeX_lower,q=1,v=1)
    lowE_varY = m.floatSliderGrp(terRangeY_lower,q=1,v=1)
    lowE_varZ = m.floatSliderGrp(terRangeZ_lower,q=1,v=1)

    highE_varX = m.floatSliderGrp(terRangeX_upper,q=1,v=1)
    highE_varY = m.floatSliderGrp(terRangeY_upper,q=1,v=1)
    highE_varZ = m.floatSliderGrp(terRangeZ_upper,q=1,v=1)
    # TODO clean these functions a bit 

    randomizefaces(selpoints)