import maya.cmds as m
from random import uniform as randF
from random import randint as randInt
import time

# default vars ===================#
"""terain variables"""
planeSizeX=10
planeSizeY=10
terainRes=10

"""randomizer variables"""
lowE_varX = 0
lowE_varY = 0 
lowE_varZ = 0 

highE_varX = 0 
highE_varY = 0 
highE_varZ = 0

"""selection variables"""
selectedcomponents = []
allcomponents = []

"""default names"""
terrainName = "terrain"
rockName = "OBJ_rock1"

"""additional variables"""
currentTerrain=""
# ==============================#
#=====Window=====================
if m.window("terrainGen",ex=1):
    m.deleteUI("terrainGen")
mainwindow = m.window("terrainGen",t="terrainGen V0.1",s=False,wh=(400,250))
form = m.formLayout()
tabs = m.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
m.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

terraintab = m.rowColumnLayout(numberOfColumns=2)

m.setParent( '..' )

rocktab = m.rowColumnLayout(numberOfColumns=2)

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
    if currentTerrain!= "":
        delprev = confirmprompt("you already have a terrain generated and this action will delete the previous one, do you want to proceed.",["yes","no"],title="delete terrain?")
        if delprev == "yes":
            m.delete(currentTerrain)
            return
    
    currentTerrain = m.polyPlane(w=planeSizeY,h=planeSizeX,sx=terainRes,sy=terainRes)
        
    