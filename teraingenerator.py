import maya.cmds as m
from random import uniform as randF
from random import randint as randInt
from random import choice
from math import floor
from statistics import mean
import time

# default vars ===================#
"""terain variables"""
planeSizeX=100.0
planeSizeY=100.0
terainRes=30
editPerc=100

"""rock variables"""
rockRes = 3
rockGroups = []
defaultRockGroupName = "rocks"

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
planesmoothness=m.floatSliderGrp(l="smoothness",min=0.0,max=10)
randperc=m.intSliderGrp(l="% affected",min=1,max=100,f=1)
terRangeY_upper=m.floatSliderGrp(l="upperY",v=10,min=-10,max=10,f=1)
terRangeY_lower=m.floatSliderGrp(l="lowerY",v=-10,min=-10,max=10,f=1)

m.button(l="randomize",c="randomizeTerrain()")

m.setParent( '..' )

rocktab = m.rowColumnLayout()
UIrockName = m.textFieldGrp(l="general rock name",tx=defaultRockGroupName)
UIrocknum = m.intSliderGrp(f=1,l="number of rocks gnerated",v=10,min=1,max=100)
m.separator()
UIrockres = m.floatSliderGrp(f=1,min=3,max=10,l="rock resolution" v=3)
UIrocktypes = m.checkBoxGrp(ncb=3,l="what type of rocks are you using",l1="boulders",l2="river rocks",l3="bricks",v1=1)
m.separator() 
UIrockscale = m.floatSliderGrp(f=1,l="rock scale",v=1,min=1,max=10)
UIrockscaleisRange = m.checkBoxGrp(l="is range",ncb=1,v1=1)

UIXupper = m.floatSliderGrp(f=1,min=-10,max=10,l="upper x value")
UIXlower = m.floatSliderGrp(f=1,min=-10,max=10,l="lower x value")

UIYupper = m.floatSliderGrp(f=1,min=-10,max=10,l="upper y value")
UIYlower = m.floatSliderGrp(f=1,min=-10,max=10,l="lower y value")

UIZupper = m.floatSliderGrp(f=1,min=-10,max=10,l="upper z value")
UIZlower = m.floatSliderGrp(f=1,min=-10,max=10,l="lower Z value")
m.button(l="generate rocks",c="generaterocks()")

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
        m.select(i)
        shiftx = randF(lowE_varX,highE_varX)
        shifty = randF(lowE_varY,highE_varY)
        shiftz = randF(lowE_varZ,highE_varZ)
        m.move(shiftx,shifty,shiftz,r=1)
        if animateProcess:
            m.currentTime(curFrame)
            curFrame+=1
            time.sleep(animationSpeed)


def randomizeTerrain():
    global lowE_varX,lowE_varY,lowE_varZ,highE_varX,highE_varY,highE_varZ,editPerc,smoothness,terainRes
    
    
    m.select(f"{currentTerrain[0]}.f[*]")
    faces = m.ls(sl=1,fl=1)
    editPerc = m.intSliderGrp(randperc,q=1,v=1)
    selpoints=[]
    for i in range(0,floor(len(faces)*(editPerc/100))):
        selpoints.append(faces.pop(randInt(0,len(faces)-1)))
    lowE_varX = 0
    lowE_varY = m.floatSliderGrp(terRangeY_lower,q=1,v=1)
    lowE_varZ = 0

    highE_varX = 0
    highE_varY = m.floatSliderGrp(terRangeY_upper,q=1,v=1)
    highE_varZ = 0
    smoothness = m.floatSliderGrp(planesmoothness,q=1,v=1) 
    falloff = mean([m.polyPlane( currentTerrain,q=1,h=1)/terainRes, m.polyPlane(currentTerrain,q=1,w=1)/terainRes]) * smoothness
    print(f"the falloff is {falloff}")
    m.softSelect(sse=1,ssd=falloff)
    randomizefaces(selpoints)

def generaterrocks():
    