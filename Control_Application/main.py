#library imports 
import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread


#file imports 
from app import Ui_MainWindow
from worker import ClawWorker, DockWorker, ArmWorker, HoldWorker

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
        self.ui.dock_button.setEnabled(False)
        self.ui.toggle_claw_button.setEnabled(False)
        self.dock_worker = DockWorker()
        self.dock_thread = QThread()
        self.dock_worker.moveToThread(self.dock_thread)
        self.dock_thread.started.connect(self.dock_worker.toggle_dock)
        self.dock_worker.resultReady.connect(self.ui.log.append)
        self.dock_worker.finished.connect(self.dock_thread.quit)
        self.dock_thread.finished.connect(self.dock_thread.deleteLater)
        self.dock_thread.finished.connect(self.dock_worker.deleteLater)
        self.dock_thread.finished.connect(lambda: self.ui.dock_button.setEnabled(True))
        self.dock_thread.finished.connect(lambda: self.ui.toggle_claw_button.setEnabled(True))
        self.dock_thread.start()
        self.ui.log.append("Dock button clicked")
        
    

    def on_toggle_claw_clicked(self):

        #disabling button 
        self.ui.dock_button.setEnabled(False)
        self.ui.toggle_claw_button.setEnabled(False)

        #creatine instances
        self.claw_worker = ClawWorker()
        self.claw_thread = QThread()

        #moving instance to threada 
        self.claw_worker.moveToThread(self.claw_thread)

        #connecting thread start signal to worker function slot 
        self.claw_thread.started.connect(self.claw_worker.toggle_claw)

        #output 
        self.claw_worker.resultReady.connect(self.ui.log.append)

        #wrker thread quits after finish emitte
        self.claw_worker.finished.connect(self.claw_thread.quit)

        #cleanup after thread finishes
        self.claw_thread.finished.connect(self.claw_thread.deleteLater)
        self.claw_thread.finished.connect(self.claw_worker.deleteLater)
        
        #reenabling buttons after thread finishes
        self.claw_thread.finished.connect(lambda: self.ui.dock_button.setEnabled(True))
        self.claw_thread.finished.connect(lambda: self.ui.toggle_claw_button.setEnabled(True))

        #starting thread
        self.claw_thread.start()
        self.ui.log.append("Toggle Claw button clicked")


    def on_arm_clicked(self):
        self.ui.ARM_button.setEnabled(False)
        self.arm_worker = ArmWorker()
        self.arm_thread = QThread()
        self.arm_worker.moveToThread(self.arm_thread)
        self.arm_thread.started.connect(self.arm_worker.arm_drone)
        self.arm_worker.resultReady.connect(self.ui.log.append)
        self.arm_worker.finished.connect(self.arm_thread.quit)
        self.arm_thread.finished.connect(self.arm_thread.deleteLater)
        self.arm_thread.finished.connect(self.arm_worker.deleteLater)
        self.arm_thread.finished.connect(lambda: self.ui.ARM_button.setEnabled(True))
        self.arm_thread.start()
        self.ui.log.append("ARM button clicked")


    def on_hold_clicked(self):
        self.ui.HOLD_button.setEnabled(False)
        self.hold_worker = HoldWorker()
        self.hold_thread = QThread()
        self.hold_worker.moveToThread(self.hold_thread)
        self.hold_thread.started.connect(self.hold_worker.hold_drone)
        self.hold_worker.resultReady.connect(self.ui.log.append)
        self.hold_worker.finished.connect(self.hold_thread.quit)
        self.hold_thread.finished.connect(self.hold_thread.deleteLater)
        self.hold_thread.finished.connect(self.hold_worker.deleteLater)
        self.hold_thread.finished.connect(lambda: self.ui.HOLD_button.setEnabled(True))
        self.hold_thread.start()
        self.ui.log.append("HOLD button clicked")

    #persistent functions 
    def on_speak_clicked(self):
        self.ui.log.append("Speak button clicked")

#starting application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())