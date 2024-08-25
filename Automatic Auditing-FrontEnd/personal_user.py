import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox

class PersonalPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel("Select OS Version:", self)
        layout.addWidget(self.label)

        # Create a dropdown box (combo box) for OS versions
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["Windows 10", "Windows 11", "Ubuntu 20.04", "Ubuntu 22.04", "Red Hat Enterprise Linux 8", "Red Hat Enterprise Linux 9"])
        layout.addWidget(self.combo_box)

        # Create a Scan button
        self.scan_button = QPushButton("Scan", self)
        self.scan_button.clicked.connect(self.scan)
        layout.addWidget(self.scan_button)

        # Set the layout
        self.setLayout(layout)

    def scan(self):
        selected_os = self.combo_box.currentText()

        # Send request to Django backend
        response = requests.post("http://127.0.0.1:8000/run_audit/", data={'os_version': selected_os})

        if response.status_code == 200:
            result = response.text
            QMessageBox.information(self, "Scan Result", result)
        else:
            QMessageBox.warning(self, "Scan Failed", "Failed to execute scan. Please try again.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Page Example")
        self.setGeometry(100, 100, 400, 200)

        # Create an instance of PersonalPage
        self.personal_page = PersonalPage()
        self.setCentralWidget(self.personal_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
