import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from src.app import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- THE FIX ---
        # 1. Get the absolute path to the directory where main.py lives
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Build the exact path to your image (adjust "img/drone.png" if your folder is named differently)
        image_path = os.path.join(current_dir, "img", "drone.png")
        
        # 3. Force the label to load the image from the absolute path
        self.ui.app_logo.setPixmap(QPixmap(image_path))

# --- NEW: The Application Engine ---
if __name__ == "__main__":
    # 1. Create the PyQt application instance
    app = QApplication(sys.argv)
    
    # 2. Create an instance of your custom window
    window = MainWindow()
    
    # 3. Tell the window to physically display itself on the screen
    window.show()
    
    # 4. Start the application's event loop (keeps the app running until you click 'X')
    sys.exit(app.exec())