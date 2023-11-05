import maya.cmds as m
from random import uniform as randF
from random import randint as randI
import time

# ==================default variables
LowE_varX=0
LowE_varY=0
LowE_varZ=0
HighE_varX=0
HighE_varY=0
HighE_varZ=0
allcomponents=[]
# ===================================
# """basically window boilerplate"""
# check if windowexists
if m.window("rockGen",ex=True):
    m.deleteUI("rockGen")
mainwindow=m.window("rockGen",t="Rock Object Generator",s=False,wh=(400,250))
m.columnLayout()
m.text(l="choose the low end of the noise")
UIlowE=m.floatSliderGrp(f=1,min=-5,max=5,v=1)
m.text(l="choose the high end of the noise")
UIhighE=m.floatSliderGrp(f=1,min=-5,max=5,v=1)
m.button(l="X",c="XRange()",w=50)
m.button(l="Y",c="YRange()",w=50)
m.button(l="Z",c="ZRange()",w=50)
m.setParent("..")
m.separator(w=400)
m.checkBox(l="with soft select",onc="m.softSelect(sse=1)",ofc="m.softSelect(sse=0)")
# UISoftness=m.intSliderGrp(l="choose softness level",f=1,min=1,max=100,v=1)
m.separator(w=400)
m.button(l="make it happen",c="genrock()")
m.showWindow() #should end in this

selectedComponents=m.ls(sl=1,fl=1)

# functions 
def XRange():
    global LowE_varX
    global HighE_varX
    LowE_varX = m.floatSliderGrp(UIlowE,q=True,v=True)
    HighE_varX = m.floatSliderGrp(UIhighE,q=1,v=1)
    print(LowE_varX)
    

def YRange():
    global LowE_varY
    global HighE_varY
    LowE_varY = m.floatSliderGrp(UIlowE,q=True,v=True)
    HighE_varY = m.floatSliderGrp(UIhighE,q=1,v=1)

def ZRange():
    global LowE_varZ
    global HighE_varZ
    LowE_varZ = m.floatSliderGrp(UIlowE,q=True,v=True)
    HighE_varZ = m.floatSliderGrp(UIhighE,q=1,v=1)

def genrock():
    global selectedComponents
    curFrame=1
    for i in selectedComponents:
        randomx = randF(LowE_varX,HighE_varX)
        randomy = randF(LowE_varY,HighE_varY)
        randomz = randF(LowE_varZ,HighE_varZ)
        m.move(randomx,randomy,randomz,r=1)
        m.currentTime(curFrame)
        curFrame+=1
        time.sleep(0.1)

#TODO modify this to make more rocks 
# note rememenber to use faces when modifying rocks 
# m.ConvertSelectionToFaces()
# m.polyPlatonic()
# note: try to make a mountain wiht changign the selection

# placing rocks on terain
m.matchTransform()#this would make aligning objects together
# or just match the the x and y values of the point of a vertex
# check where we figured out avoiding duplication
# learn to move pivot then make function to controle points rleative to pivot