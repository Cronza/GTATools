import maya.cmds as mc
from PySide2 import QtCore, QtWidgets

class LayerEditorPlusFunctions():
	def __init__(self, function, displayLayer, attribute):		
		self.displayLayer = displayLayer
		functionToCall = getattr(self, function)
		functionToCall(self.displayLayer)

	
		
	######  Action Functions  ######
	def ToggleVisibility(self, displayLayer):
		visibility = self.DetectAttrState(displayLayer, 'visibility')
		if visibility:
			mc.setAttr(displayLayer+'.visibility',False)
		else:
			mc.setAttr(displayLayer+'.visibility',True)		
	
	######  Detection Functions  ######
	def DetectAttrState(self, displayLayer, attribute):
		state = mc.getAttr(displayLayer+'.'+attribute)
		return state