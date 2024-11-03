import maya.cmds as m
#########################################################################
'''good ol window boilerplate'''
if m.window("cubegen",ex=1):
    m.deleteUI("cubegen")
mainwindow = m.window("cubegen",t="ultra cube creator",s=1,wh=(400,250))
#########################################################################
"""window content"""
m.columnLayout(cat=("both",5),rs=10,cw=399)

boxname= m.textFieldGrp(l="box name",tx="box")
boxsize= m.floatFieldGrp(nf=3,l="box dimensions",v1=1,v2=1,v3=1)
boxres = m.intSliderGrp(l="cube resolution",min=0,max=10,v=0, f=1)
m.button(l="make cube",c= "makecube()")
m.setParent( '..' )
m.showWindow()
#########################################################################
def makecube():
    name = m.textFieldGrp(boxname,q=1,tx=1)
    width = m.floatFieldGrp(boxsize,q=1,v1=1)
    height = m.floatFieldGrp(boxsize,q=1,v2=1)
    depth = m.floatFieldGrp(boxsize,q=1,v3=1)
    res = m.intSliderGrp(boxres,q=1,v=1)
    m.polyCube(n=name,w=width,h=height,d=depth,sx=res,sy=res,sz=res)