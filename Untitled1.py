import numpy
import matplotlib
import cv2
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

form_class = uic.loadUiType("imageprocessing_main.ui")[0]

def showImageToLabel(imagepath,label):
        
        pixmap = QPixmap(imagepath)
        
        viewHeight = label.height()
        ratio = viewHeight / pixmap.height()
        
        label.setPixmap(pixmap.scaled( pixmap.width() * ratio , viewHeight))
      
class DirManager():
    #path를 지정해서 해당 Dir
    def __init__(self,path):
        self.path = path


class OpenFileDialog(QDialog):
    def __init__(self):
        super(OpenFileDialog,self).__init__()
        self.filepath = QFileDialog.getOpenFileName(self)
          
    
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.openImage.clicked.connect(self.openImage_clicked)
        self.is_image_loaded=False
         
    def openImage_clicked(self):
        dlg = OpenFileDialog()
        #dlg.exec_()
        
        self.filepath = dlg.filepath[0]
        self.is_image_loaded = True
        showImageToLabel(self.filepath,self.imageView)
    
    def keyPressEvent(self,e):
        key = e.key()
        self.keydict 
        
        
        
if __name__ == "__main__":
    
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    myWindow = MainWindow()
    myWindow.show()
    myWindow.raise_()
    app.exec_()
