from PyQt5.QtWidgets import *
import os, sys

class RenameFileWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.Title = "Rename File"
        self.setupUI()
    
    def setupUI(self,Path = os.getcwd()):
        self.setWindowTitle(self.Title)
        self.resize(700,500)

        self.curdirLabel = QLabel(Path)
        self.listFile = QListWidget()
        self.files = os.listdir(Path)
        for f in self.files:
            if os.path.isfile(os.path.join(Path,f)):
                self.listFile.addItem(f)

        FindLabel = QLabel("Find")
        self.FindFile = QLineEdit()
        ReplaceLabel = QLabel("Replace")
        self.Replace = QLineEdit()

        self.ButtonBrowse = QPushButton("Browse",clicked = self.BrowseFolder)
        self.ButtonReplace = QPushButton("Replace",clicked = self.ReplaceName)

        grid = QGridLayout()
        grid.addWidget(self.ButtonBrowse,1,0)
        grid.addWidget(FindLabel,2,0)
        grid.addWidget(self.FindFile,2,1,1,2)
        grid.addWidget(ReplaceLabel,3,0)
        grid.addWidget(self.Replace,3,1,1,2)
        grid.addWidget(self.ButtonReplace,4,1,1,2)

        DisplayWidget = QVBoxLayout()
        DisplayWidget.addWidget(self.curdirLabel)
        DisplayWidget.addWidget(self.listFile)
        DisplayWidget.addLayout(grid)

        self.setLayout(DisplayWidget)
    
    def BrowseFolder(self):
        self.fname = QFileDialog.getExistingDirectory(self,"Open Folder","C:\\")
        if self.fname == "":
            self.fname = os.getcwd()
            
        self.curdirLabel.setText(self.fname)
        
        self.listFile.clear()

        self.files = os.listdir(self.fname)
        for f in self.files:
            if os.path.isfile(os.path.join(self.fname,f)):
                self.listFile.addItem(f)

    def ReplaceName(self):
        Target = self.FindFile.text()
        Repl = self.Replace.text()

        os.chdir(self.fname)

        for f in self.files:
            replaceName = f.replace(Target,Repl)
            os.rename(f,replaceName)

App = QApplication(sys.argv)
Window = RenameFileWindows()
Window.show()
App.exec()