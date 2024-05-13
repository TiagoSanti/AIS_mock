import os
import sys
from PySide6.QtWidgets import QApplication
from src.controller.deploy_controller import DeployController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeployController()
    window.show()
    app.exec()