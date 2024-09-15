import maya.cmds as m
from random import uniform as randf

m.polyCube(h=6,w=6,d=6,n="idkman#")
m.rotate(randf(0,360.0),randf(0,360.0),randf(0,360.0))
m.move(randf(0,30.0),randf(0,30.0),randf(0,30.0))
m.select(cl=1)