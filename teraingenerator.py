import maya.cmds as m
from random import uniform as randF
from random import randint as randInt
import time

# default vars ===================#
"""terain variables"""
planeSizeX=10
planeSizeY=10
terainRes=10

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
maxAnimTime = 60
# ==============================#

#=====Window=====================
if m.window("terrainGen",ex=1):
    m.deleteUI("terrainGen")
mainwindow = m.window("terrainGen",t="terrainGen V0.1",s=False,wh=(400,250))
form = m.formLayout()
tabs = m.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
m.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

terraintab = m.rowColumnLayout(numberOfColumns=2)
# TODO ADD terrain settings here
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
    if currentTerrain != None:
        delprev = confirmprompt("you already have a terrain generated and this action will delete the previous one, do you want to proceed.",["yes","no"],title="delete terrain?")
        if delprev == "yes":
            m.delete(currentTerrain)
            return
    
    currentTerrain = m.polyPlane(w=planeSizeY,h=planeSizeX,sx=terainRes,sy=terainRes)

def correctAnimtime(): #this just makes sure the animation time doesn't surpass the max animation time
    global animationSpeed
    if len(selectedcomponents)*animationSpeed > maxAnimTime:
        animationSpeed = len(selectedcomponents)/maxAnimTime
    # note to self may remove this to just have it work in randomize faces 

def randomizefaces():
    correctAnimtime()
    curFrame = 1
    for i in selectedcomponents:
        shiftx = randF(lowE_varX,highE_varX)
        shifty = randF(lowE_varY,highE_varY)
        shiftz = randF(lowE_varZ,highE_varZ)
        m.move(shiftx,shifty,shiftz,r=1)
        if animateProcess:
            curFrame+=1
            time.sleep(animationSpeed)

def setrange(axis:str):
    match axis:
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