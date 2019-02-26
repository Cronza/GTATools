import maya.cmds as cmds
from PySide2 import QtCore, QtWidgets, QtGui

'''
---------------UI CLASS------------------
The class that will "own" the UI
-----------------------------------------
'''
class SceneScannerUI():
    
    #Initialization Method. Let's create our UI here
    def __init__(self):
        #Declare some variables
        self.funcs = SceneScannerFunctions(self)
        self.optionList = []
        
        #Create a 'QWidget' to be our main window, then alter its title and size
        self.mainWindow = QtWidgets.QWidget()
        self.mainWindow.setWindowTitle('Scene Scanner Tool')
        self.mainWindow.resize(400, 100)
        
        #Create our core layout, using 'QVBoxLayout' which uses vertical arrangement
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.optionLayout = QtWidgets.QGridLayout()
        self.optionLayout.setAlignment(QtCore.Qt.AlignTop)
        
        #Create the fonts that will be used by our U.I
        self.mainHeaderFont = QtGui.QFont()
        self.mainHeaderFont.setPointSize(24)
        self.mainHeaderFont.setBold(True)
        self.subHeaderFont = QtGui.QFont()
        self.subHeaderFont.setPointSize(18)
        self.subHeaderFont.setBold(True) 
        
        #Add a Header to state the immediate purpose of the tool
        self.mainHeader = QtWidgets.QLabel("Welcome to the Scene Scanner")
        self.mainHeader.setAlignment(QtCore.Qt.AlignHCenter)
        self.mainHeader.setFont(self.mainHeaderFont)               
        self.mainLayout.addWidget(self.mainHeader)
        
        #Add some options for scanning, add the layout to the mainLayout, then add everything to a list
        self.option1 = QtWidgets.QCheckBox("Geo")
        self.option2 = QtWidgets.QCheckBox("Materials")
        self.option3 = QtWidgets.QCheckBox("Joints")
        self.optionLayout.addWidget(self.option1, 0, 0)
        self.optionLayout.addWidget(self.option2, 0, 1)
        self.optionLayout.addWidget(self.option3, 0, 2)
        self.mainLayout.addLayout(self.optionLayout)
        self.optionList.append(self.option1)
        self.optionList.append(self.option2)
        self.optionList.append(self.option3)
        
        #Add the final "Scan" button
        self.scanButton = QtWidgets.QPushButton("Scan")
        self.scanButton.clicked.connect(self.funcs.DetermineObjectsToScan)
        self.mainLayout.addWidget(self.scanButton)        

        #Add our mainLayout to our mainWindow
        self.mainWindow.setLayout(self.mainLayout)
    
    #Using a passed in reference to a U.I window, invoke the "show" command to reveal it to the user (Argument is expected to be a window reference)
    def RevealUI(self, uiWindow):        
        uiWindow.show()
'''
-------------------FUNCTION CLASS---------------------
The class that will "own" the tools core functionality
------------------------------------------------------
'''
class SceneScannerFunctions():
    
    #Initialization Method
    def __init__(self, uiRef):
        #Declare some variables
        self.ssui = uiRef 
        self.objectsToScan = []
        
    #Taking in the list of options from the U.I check if any are checked, then grab their text and pass it off to another function 
    def DetermineObjectsToScan(self):        
        #Loop through the list of options and check if they are checked        
        for option in self.ssui.optionList:
            if(option.isChecked() == True):
                self.objectsToScan.append(option.text())
        
        #Check if theres at least one checked option. If so, perform the actual scan function
        if (len(self.objectsToScan) > 0):
            self.ScanAndSelect(self.objectsToScan)
            
    #Taking a list of terms (geo, materials, etc), scan the scene for things of that type and print them out
    def ScanAndSelect(self, foundTerms):
        foundItemLists = {}
        foundItem = []
        
        print "\n**********Scene Scanning in progress...*******"
        
        #Loop through the terms and add them to a dictionary for easy output printing later on
        for term in foundTerms:
            if(term == "Geo"):
                foundItemLists["Geo"] = cmds.ls(g=True)
            elif(term == "Materials"):
                foundItemLists["Material"] = cmds.ls(mat=True)
            elif(term == "Joints"):
                foundItemLists["Joint"] = cmds.ls(type="joint")
        
        #For every key in the dictionary (term), take the list of items in the value and print them individually
        print "**********Scanning Complete! Results Below******"
        for key in foundItemLists:
            print "\nScan for: '" + key + "'"
            for value in foundItemLists[key]:                
                print ("    -" + value)
         
         
#Spawn the UI and assign the instance to a variable
ssui = SceneScannerUI()

#Reveal the UI
ssui.RevealUI(ssui.mainWindow)      
        
#----------ONLINE PYSIDE / PYQT RESOURCES--------------
'''
QCheckBox Class Reference - http://pyqt.sourceforge.net/Docs/PyQt4/qcheckbox.html
QtCore Class Reference - http://pyqt.sourceforge.net/Docs/PyQt5/QtCore.html
QtWidgets Class Reference - http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html#PyQt5-QtWidgets
QtGui Class Reference - http://pyqt.sourceforge.net/Docs/PyQt5/QtGui.html#PyQt5-QtGui
Diff between PyQt 4 and 5 - http://pyqt.sourceforge.net/Docs/PyQt5/pyqt4_differences.html
'''