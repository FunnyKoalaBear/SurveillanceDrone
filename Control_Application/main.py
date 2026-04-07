#library imports 
import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

#file imports 
from app import Ui_MainWindow
from worker import * 

class MainWindow(QMainWindow):

    def __init__(self):
        #loading ui
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #loading asset files 


        #setting varaiables
        self.claw_open = False
        self.speaking = False
        self.armed = False
        self.hold = False

        self.ui.log.clear()
        
        #loading button functions
        self.ui.dock_button.clicked.connect(self.on_dock_clicked)
        self.ui.toggle_claw_button.clicked.connect(self.on_toggle_claw_clicked)
        self.ui.speak_button.clicked.connect(self.on_speak_clicked)
        self.ui.ARM_button.clicked.connect(self.on_arm_clicked)
        self.ui.HOLD_button.clicked.connect(self.on_hold_clicked)

    
    #button functions
    def on_dock_clicked(self):
        self.ui.log.append("Dock button clicked")


    def on_toggle_claw_clicked(self):
        self.ui.log.append("Toggle Claw button clicked")

    def on_speak_clicked(self):
        self.ui.log.append("Speak button clicked")

    def on_arm_clicked(self):
        self.ui.log.append("ARM button clicked")

    def on_hold_clicked(self):
        self.ui.log.append("HOLD button clicked")



#starting application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())