import maya.cmds as cmds
'''
********* TOOL INFO **********
Name: VertLeveler
Author: Garrett Fredley
Purpose: Taking in a selected group of vertices, attempt to force them all to the same position on
the given axis.

TO-DO: 
- Add verification step for checking if selection contains only verts
- Refactor the axis steps to avoid manual edits
- Add a basic tool interface with PySide2
******************************
'''

#Collect a flattened list of selected vertices
vertList = cmds.ls(sl=True, fl=True)

#Define the axis to level the vertices to
axis = "X"

#Based on axis, query the first vert and collect its position information
if(axis == "X"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[0]
elif(axis == "Y"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[1]
elif(axis == "Z"):
    targetPos = cmds.xform(vertList[0], q=True, ws=True, t=True)[2]

#Loop through all selected vertices and set their positions
for vert in vertList:
    baseX = cmds.xform(vert, q=True, ws=True, t=True)[0]
    baseY = cmds.xform(vert, q=True, ws=True, t=True)[1]
    baseZ = cmds.xform(vert, q=True, ws=True, t=True)[2]

    cmds.xform(vert, ws=True, t=( 
        targetPos,
        baseY,
        baseZ
        ))

