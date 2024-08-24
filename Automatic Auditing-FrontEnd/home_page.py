from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class HomePage(QWidget):
    navigate_to_personal = pyqtSignal()
    navigate_to_organization = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Home Page")
        self.setGeometry(100, 100, 800, 600)  # Adjust size as needed
        
        layout = QVBoxLayout()
        
        self.title = QLabel("Welcome to Our Audit Tool", self)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        layout.addWidget(self.title)
        
        self.subtitle = QLabel("Please select your role to proceed:", self)
        self.subtitle.setStyleSheet("font-size: 16px; text-align: center;")
        layout.addWidget(self.subtitle)
        
        self.personal_button = QPushButton("Personal Use", self)
        self.personal_button.clicked.connect(self.navigate_to_personal.emit)
        layout.addWidget(self.personal_button)
        
        self.organization_button = QPushButton("Organization Use", self)
        self.organization_button.clicked.connect(self.navigate_to_organization.emit)
        layout.addWidget(self.organization_button)
        
        self.setLayout(layout)
