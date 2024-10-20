import maya.cmds as m
from random import uniform as randF
#=====Window=====================
if m.window("primgen",ex=1):
    m.deleteUI("primgen")
mainwindow = m.window("primgen",t="super primitive creator",s=1,wh=(400,250))

m.columnLayout(cat=("both",5),rs=10,cw=399)
m.button(l="cube", c="gencube()")
m.button(l="cone", c="gencone()")
m.button(l="sphere", c="gensphere()")
m.button(l="cylinder",c="gencylinder()")
m.button(l="delete all",c="emptyscene()")
m.setParent("..")

# m.setParent("..")

m.showWindow()

def randomVals():
    xval = randF(-1000,1000)
    yval = randF(-1000,1000)
    zval = randF(-1000,1000)
    m.move(xval,yval,zval)
    xval = randF(-100,100)
    yval = randF(-100,100)
    zval = randF(-100,100)
    m.scale(xval,yval,zval)
    xval = randF(-100,100)
    yval = randF(-100,100)
    zval = randF(-100,100)
    m.rotate(xval,yval,zval)
    m.ls(d=1)

def emptyscene():
    m.select(m.ls())
    m.delete()

def gencube():
    m.polyCube()
    randomVals() 

def gencone():
    m.polyCone()
    randomVals()

def gensphere():
    m.polySphere()
    randomVals()

def gencylinder():
    m.polyCylinder()
    randomVals()