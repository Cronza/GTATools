import maya.cmds as cmds

##############FIND NGONS##################
mesh = cmds.ls(sl=True)
cmds.select("{0}.f[*]".format(cmds.ls(sl=True)[0]))
meshFaces = cmds.ls(sl=True, fl=True)
ngons = []

for faces in range(0,len(meshFaces)):    
    vtxCount = cmds.polyInfo(meshFaces[faces],fv=True)
    for vertex in vtxCount:
        if len(vertex.split(":",1)[-1].split()) > 4:
            ngons.append((meshFaces[faces]))            
            print "***NGon found***"        
                
cmds.select(cl=True)
if len(ngons) > 0:    
    for faces in range(0,len(ngons)):     
        #cmds.select(cmds.ls(ngons[faces]),add=True)
        cmds.select("{0}".format(ngons[faces]),add=True)



