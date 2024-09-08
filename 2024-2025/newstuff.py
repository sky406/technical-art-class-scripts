import maya.cmds as m
import random as r
m.polyCube(h=6,w=6,d=6,n="idkman#")
m.rotate(r.uniform(0,360.0),r.uniform(0,360.0),r.uniform(0,360.0))
m.move(r.uniform(0,30.0),r.uniform(0,30.0),r.uniform(0,30.0))