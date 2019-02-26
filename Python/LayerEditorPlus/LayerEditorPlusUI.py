import maya.cmds as mc
import LayerEditorPlusFunctions
from PySide2 import QtCore, QtWidgets, QtGui

class LayerEditorPlusUI():
	def __init__(self):
		self.funcs = LayerEditorPlusFunctions
		
		#Core Window Setup
		self.mainWindow = QtWidgets.QWidget()
		self.mainWindow.setWindowTitle('Layer Editor +')
		self.mainWindow.resize(400, 600) 

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
		
		#sig = Signal(int)

		#FONTS
		self.mainHeaderFont = QtGui.QFont()
		self.mainHeaderFont.setPointSize(24)
		self.mainHeaderFont.setBold(True)
		self.subHeaderFont = QtGui.QFont()
		self.subHeaderFont.setPointSize(18)
		self.subHeaderFont.setBold(True)

		######  DisplayLayer Selector and Header  ######
		self.mainHeader = self.AddHeader('Please Choose a Layer', self.mainHeaderFont)
		self.layerSelector = QtWidgets.QComboBox()
		self.displayLayers = mc.ls(type='displayLayer')
		tempVal = ''

		for i in range(0, len(self.displayLayers)):
			if self.displayLayers[i] == 'defaultLayer':
				 tempValue = self.displayLayers[i]
				 del self.displayLayers[i]
				 break

		self.displayLayers.insert(0, tempValue) 

		for layer in self.displayLayers:
			self.layerSelector.addItem(layer) 

		###### General Settings ######
		self.generalHeader = self.AddHeader('General Settings', self.subHeaderFont)
		self.visToggleBox = self.AddOption('checkbox', 'Visible')

		#####  FINALIZE UI SETUP  ####
		
		#Hookup Option Actions
		self.visToggleBox.clicked.connect(lambda: self.funcs('ToggleVisibility', self.layerSelector.currentText(), ''))		
		self.layerSelector.currentIndexChanged.connect(self.UpdateUI)
		
		self.mainLayout.addWidget(self.mainHeader)
		self.mainLayout.addWidget(self.layerSelector)
		self.mainLayout.addWidget(self.generalHeader)
		self.mainLayout.addWidget(self.visToggleBox)
		self.mainWindow.setLayout(self.mainLayout)
		
		self.RevealUI(self.mainWindow)
	
	#Update all option values in the UI when the displayLayer is changed
	def UpdateUI(self):
		visibilityState = self.funcs.DetectAttrState(self.layerSelector.currentText(), 'visibility')
		self.visToggleBox.setCheckState(2)
		

	def RevealUI(self, uiWindow):
		uiWindow.show()
		
	######  Helper Functions  ######
	#Adds a widget based on given type
	def AddOption(self, type, text):
		option = ''
		if type == 'checkbox':
			option = QtWidgets.QCheckBox(text)    
		return option

	#Adds a header with given text and font
	def AddHeader(self, headerText, headerFont):
		header = QtWidgets.QLabel(headerText)
		header.setAlignment(QtCore.Qt.AlignHCenter)
		header.setFont(headerFont)
		return header


	#Adds a layout based on given type    
	def AddContainer(self, type, itemToAdd):
		container = ''
		if type == "vertical":
			container = QtWidgets.QVBoxLayout()
			container.setAlignment(QtCore.Qt.AlignTop)
		elif type == "horizontal":
			container = QtWidgets.QHBoxLayout()
			container.setAlignment(QtCore.Qt.AlignTop)
		
		if itemToAdd[0] != "" and itemToAdd[1] != "":
			container.addWidget(itemToAdd[0])
			container.addWidget(itemToAdd[1])
		return container