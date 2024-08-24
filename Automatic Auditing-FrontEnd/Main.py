import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from home_page import HomePage
from personal_user import PersonalUser
from organization_use import OrganizationPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audit Tool")
        self.setGeometry(100, 100, 800, 600)  # Adjust size as needed
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.home_page = HomePage(self)
        self.personal_user_page = PersonalUser()
        self.organization_page = OrganizationPage()
        
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.personal_user_page)
        self.stack.addWidget(self.organization_page)
        
        self.home_page.navigate_to_personal.connect(self.show_personal_user_page)
        self.home_page.navigate_to_organization.connect(self.show_organization_page)
    
    def show_personal_user_page(self):
        self.stack.setCurrentWidget(self.personal_user_page)
    
    def show_organization_page(self):
        self.stack.setCurrentWidget(self.organization_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
