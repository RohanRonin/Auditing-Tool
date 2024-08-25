import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Example")
        self.setGeometry(100, 100, 300, 200)

        # Create buttons
        self.button_personal = QPushButton("Personal", self)
        self.button_organization = QPushButton("Organization", self)

        # Connect buttons to their slot methods
        self.button_personal.clicked.connect(self.show_personal_message)
        self.button_organization.clicked.connect(self.show_organization_message)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button_personal)
        layout.addWidget(self.button_organization)

        # Central widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_personal_message(self):
        QMessageBox.information(self, "Button Clicked", "Personal button clicked")

    def show_organization_message(self):
        QMessageBox.information(self, "Button Clicked", "Organization button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
