import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)
from fpdf import FPDF

class PersonalUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal User Security Scan")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()
        
        self.scan_description = QLabel("To ensure your system's security, please scan your laptop for any potential vulnerabilities.")
        self.layout.addWidget(self.scan_description)
        
        self.scan_button = QPushButton("Start Scan")
        self.scan_button.clicked.connect(self.start_scan)
        self.layout.addWidget(self.scan_button)
        
        self.scan_results = {
            "Password Policies": None,
            "Software Updates": None,
            "Firewall Settings": None,
            "Antivirus Protection": None
        }
        
        self.result_labels = {}
        for key in self.scan_results:
            label = QLabel(f"{key}: ...")
            self.result_labels[key] = label
            self.layout.addWidget(label)
        
        self.export_button = QPushButton("Export PDF")
        self.export_button.setEnabled(False)
        self.export_button.clicked.connect(self.export_pdf)
        self.layout.addWidget(self.export_button)
        
        self.setLayout(self.layout)
        self.scan_timer = QTimer(self)
        self.scan_timer.timeout.connect(self.update_scan_results)
        
        self.scan_steps = 0

    def start_scan(self):
        self.scan_button.setEnabled(False)
        self.scan_description.hide()
        self.scan_timer.start(1000)  # Start timer with 1 second intervals
        
    def update_scan_results(self):
        if self.scan_steps == 0:
            self.scan_results["Password Policies"] = True
        elif self.scan_steps == 1:
            self.scan_results["Software Updates"] = True
        elif self.scan_steps == 2:
            self.scan_results["Firewall Settings"] = False
        elif self.scan_steps == 3:
            self.scan_results["Antivirus Protection"] = True
            self.scan_timer.stop()
            self.export_button.setEnabled(True)
        
        self.update_labels()
        self.scan_steps += 1
    
    def update_labels(self):
        for key, result in self.scan_results.items():
            if result is None:
                self.result_labels[key].setText(f"{key}: ...")
            else:
                status = "✔ Safe" if result else "✖ Unsafe"
                self.result_labels[key].setText(f"{key}: {status}")
    
    def export_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Scan Results", ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        for key, result in self.scan_results.items():
            status = "Safe" if result else "Unsafe"
            pdf.cell(200, 10, txt=f"{key}: {status}", ln=True)
            
            if key == "Firewall Settings" and not result:
                pdf.ln(5)
                pdf.multi_cell(0, 10, txt="The firewall is disabled, which makes your system vulnerable to external attacks. "
                                          "Mitigation Strategy: Enable the firewall through your system settings to block unauthorized access.")
        
        pdf.output("Scan_Results.pdf")
        
        self.export_button.setText("PDF Exported!")
