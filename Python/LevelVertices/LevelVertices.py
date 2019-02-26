import maya.cmds as cmds
vertList = cmds.ls(sl=True, fl=True)
axis = "X"

if(axis == "X"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[0]
elif(axis == "Y"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[1]
elif(axis == "Z"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[2]

for vert in vertList:
    baseX = cmds.xform(vert, q=True, ws=True, t=True)[0]
    baseY = cmds.xform(vert, q=True, ws=True, t=True)[1]
    baseZ = cmds.xform(vert, q=True, ws=True, t=True)[2]

    cmds.xform(vert, ws=True, t=( 
        targetPos,
        baseY,
        baseZ
        ))

