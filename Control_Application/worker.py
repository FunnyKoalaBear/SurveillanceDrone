from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from Drone_Scripts.toggle_claw import toggle
from Drone_Scripts.dock import toggle_dock
from Drone_Scripts.hold import hold
from Drone_Scripts.voice import voice
from Drone_Scripts.arm import arm_drone

#worker 1, video, persistent declaration 



#worker 2, voice, persistent declaration



#worker 3, claw, one-time declaration
class ClawWorker(QObject):
    resultReady = pyqtSignal(str)
    finished = pyqtSignal()

    @pyqtSlot()
    def toggle_claw(self):
        result_msg = toggle()

        self.resultReady.emit(result_msg)
        self.finished.emit()


#worker 4, Dock worker, one-time declaration
class DockWorker(QObject):

    resultReady = pyqtSignal(str)
    finished = pyqtSignal()

    @pyqtSlot()
    def toggle_dock(self):
        result_msg = toggle_dock()

        self.resultReady.emit(result_msg)
        self.finished.emit()
    

#worker 5, enviromental sensors, persistent declaration 


#worker 6, drone sensors, persistent declaration



#worker 7, telem, persistent declaration


#worked 8, arm, persistent declaration
class ArmWorker(QObject):

    resultReady = pyqtSignal(str)
    finished = pyqtSignal()

    @pyqtSlot()
    def arm_drone(self):
        result_msg = arm_drone()

        self.resultReady.emit(result_msg)
        self.finished.emit()


#worker 9, hold, persisttent declaration
class HoldWorker(QObject):
    resultReady = pyqtSignal(str)
    finished = pyqtSignal()

    @pyqtSlot()
    def hold_drone(self):
        result_msg = hold()

        self.resultReady.emit(result_msg)
        self.finished.emit()