import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLabel, QCheckBox, QFileDialog, QScrollArea
from PyQt5.QtCore import QTimer

# Data from data.py
cis_rules = [
    {"check": "Account Management", "isSafe": False, "detail": "Ensure accounts are properly managed."},
    {"check": "Access Control", "isSafe": True, "detail": "Implement proper access controls for sensitive data."},
    {"check": "Audit Logs", "isSafe": False, "detail": "Audit logs should be enabled and properly managed."},
    {"check": "Backup Procedures", "isSafe": True, "detail": "Regular backups should be performed and tested."},
    {"check": "Firewall Configuration", "isSafe": False, "detail": "Firewalls should be configured to block unauthorized access."},
    {"check": "Multi-factor Authentication", "isSafe": False, "detail": "Multi-factor authentication should be enforced."},
    {"check": "Patch Management", "isSafe": True, "detail": "Apply patches and updates regularly to all systems."},
    {"check": "Data Encryption", "isSafe": True, "detail": "Encrypt sensitive data both in transit and at rest."},
    {"check": "Intrusion Detection Systems", "isSafe": False, "detail": "Implement intrusion detection systems to monitor suspicious activity."},
    {"check": "Security Policies", "isSafe": True, "detail": "Document and enforce security policies."},
    {"check": "Network Segmentation", "isSafe": True, "detail": "Segment networks to limit access to sensitive information."},
    {"check": "Vulnerability Management", "isSafe": False, "detail": "Regularly scan for and address vulnerabilities."},
    {"check": "Endpoint Protection", "isSafe": True, "detail": "Use endpoint protection tools to secure devices."},
    {"check": "Incident Response Plan", "isSafe": False, "detail": "Develop and maintain an incident response plan."},
    {"check": "User Training", "isSafe": True, "detail": "Provide regular security training to users."},
    {"check": "Secure Configuration", "isSafe": False, "detail": "Ensure systems are securely configured and hardened."},
    {"check": "Remote Access", "isSafe": True, "detail": "Secure remote access methods to protect from unauthorized access."},
    {"check": "Physical Security", "isSafe": True, "detail": "Implement physical security controls to protect hardware."},
    {"check": "System Monitoring", "isSafe": False, "detail": "Monitor systems for abnormal activities and threats."},
    {"check": "Data Loss Prevention", "isSafe": True, "detail": "Implement data loss prevention measures to protect sensitive data."},
    {"check": "Application Security", "isSafe": False, "detail": "Ensure applications are secure and free from vulnerabilities."},
    {"check": "Third-party Risk Management", "isSafe": True, "detail": "Assess and manage risks associated with third-party vendors."},
    {"check": "Cloud Security", "isSafe": True, "detail": "Secure cloud resources and ensure data protection."}
]

industry_checks = {
    "finance": [
        {"check": "Encryption Policies", "isSafe": True, "detail": "Encryption policies are in place to protect sensitive data during storage and transmission. Mitigation Strategy: Regularly review and update encryption protocols to ensure they meet current security standards."},
        {"check": "Data Backup Procedures", "isSafe": True, "detail": "Data backup procedures are established and regularly performed to ensure data recovery in case of loss. Mitigation Strategy: Implement automated backups and regularly test restore processes to ensure data integrity."},
        {"check": "Firewall Configuration", "isSafe": False, "detail": "The firewall is disabled, making your system vulnerable to external attacks. Mitigation Strategy: Enable the firewall through your system settings to block unauthorized access."},
        {"check": "Access Controls", "isSafe": True, "detail": "Access controls are implemented to restrict unauthorized users from accessing sensitive systems and data. Mitigation Strategy: Regularly review and update access permissions based on role changes and audits."},
        {"check": "Multi-factor Authentication", "isSafe": False, "detail": "Multi-factor authentication is not enabled, increasing the risk of unauthorized access. Mitigation Strategy: Enable multi-factor authentication for an added layer of security."},
        {"check": "Intrusion Detection Systems", "isSafe": True, "detail": "Intrusion Detection Systems (IDS) are in place to detect and respond to suspicious activities. Mitigation Strategy: Continuously update IDS signatures and rules to improve threat detection."},
        {"check": "Audit Logs", "isSafe": True, "detail": "Audit logs are maintained to track and review user activities and system changes. Mitigation Strategy: Regularly review audit logs and implement alerting mechanisms for suspicious activities."},
        {"check": "Third-party Risk Management", "isSafe": True, "detail": "Third-party risk management practices are implemented to assess and manage risks associated with external vendors. Mitigation Strategy: Conduct regular assessments and audits of third-party services and their security practices."},
        {"check": "Compliance with Regulations", "isSafe": True, "detail": "Compliance with relevant regulations and standards is ensured to meet legal and industry requirements. Mitigation Strategy: Keep up-to-date with regulatory changes and adjust policies and procedures accordingly."},
        {"check": "Payment Security", "isSafe": True, "detail": "Payment security measures are in place to protect financial transactions and customer payment information. Mitigation Strategy: Regularly update payment processing systems to address emerging threats and vulnerabilities."},
        {"check": "Customer Data Protection", "isSafe": True, "detail": "Customer data protection policies are enforced to safeguard personal information from unauthorized access. Mitigation Strategy: Implement data encryption and access controls to protect sensitive customer information."},
        {"check": "Disaster Recovery Plan", "isSafe": True, "detail": "A disaster recovery plan is developed and tested to ensure business continuity in case of unexpected events. Mitigation Strategy: Regularly update and test the disaster recovery plan to address new risks and ensure effective response."}
    ],
    "education": [
        {"check": "Student Data Privacy", "isSafe": True, "detail": "Student data privacy measures are implemented to protect personal and educational information from unauthorized access. Mitigation Strategy: Ensure data encryption and access controls are in place to safeguard student information."},
        {"check": "E-learning Platform Security", "isSafe": True, "detail": "Security protocols for e-learning platforms are in place to safeguard online educational content and user interactions. Mitigation Strategy: Regularly update platform security features and perform vulnerability assessments."},
        {"check": "Network Monitoring", "isSafe": False, "detail": "Network monitoring is not properly configured, potentially missing suspicious activities. Mitigation Strategy: Implement comprehensive network monitoring tools to detect and respond to potential threats."},
        {"check": "Device Management", "isSafe": True, "detail": "Device management practices are in place to secure and manage educational devices and resources. Mitigation Strategy: Implement policies for regular updates and security checks on all devices."},
        {"check": "Firewall Configuration", "isSafe": False, "detail": "The firewall is not properly configured, which can leave your network exposed. Mitigation Strategy: Review and configure your firewall settings to block unauthorized access."},
        {"check": "Access Controls", "isSafe": True, "detail": "Access controls are used to manage user permissions and restrict access to sensitive educational data. Mitigation Strategy: Regularly review user permissions and adjust access levels based on role and need."},
        {"check": "Backup and Recovery", "isSafe": True, "detail": "Backup and recovery procedures are established to ensure data integrity and availability in case of loss. Mitigation Strategy: Perform regular backups and periodically test recovery procedures to ensure data can be restored."},
        {"check": "Incident Response Plan", "isSafe": True, "detail": "An incident response plan is in place to address and manage security incidents effectively. Mitigation Strategy: Regularly update the incident response plan and conduct drills to ensure readiness for various types of incidents."},
        {"check": "Third-party Vendor Security", "isSafe": True, "detail": "Security measures for third-party vendors are implemented to manage risks associated with external services and products. Mitigation Strategy: Conduct due diligence and regular security assessments of third-party vendors."},
        {"check": "Compliance with Educational Regulations", "isSafe": True, "detail": "Compliance with educational regulations is maintained to adhere to legal and institutional requirements. Mitigation Strategy: Stay informed about regulatory changes and adjust policies to ensure continuous compliance."},
        {"check": "Software Updates", "isSafe": True, "detail": "Software updates are regularly applied to keep systems secure and up-to-date. Mitigation Strategy: Implement an automated update system to ensure timely application of software patches and updates."},
        {"check": "Antivirus Protection", "isSafe": True, "detail": "Antivirus protection is in place to detect and remove malicious software from educational systems. Mitigation Strategy: Regularly update antivirus definitions and perform scheduled scans to detect and address threats."}
    ],
    "technical": [
        {"check": "Code Repositories", "isSafe": True, "detail": "Code repositories are securely managed to protect source code from unauthorized access. Mitigation Strategy: Implement access controls and regular audits of code repositories."},
        {"check": "Development Environment Security", "isSafe": True, "detail": "The development environment is secured to prevent unauthorized access and code tampering. Mitigation Strategy: Apply security best practices and regularly review the development environment configuration."},
        {"check": "Software Development Life Cycle (SDLC)", "isSafe": True, "detail": "The SDLC process incorporates security measures at each stage to ensure secure software development. Mitigation Strategy: Follow secure coding practices and conduct regular security reviews throughout the SDLC."},
        {"check": "Vulnerability Management", "isSafe": False, "detail": "Vulnerability management practices are not adequately implemented, leaving systems at risk. Mitigation Strategy: Establish a vulnerability management program to identify, assess, and remediate security vulnerabilities."},
        {"check": "Incident Response Procedures", "isSafe": True, "detail": "Incident response procedures are defined to manage and respond to security incidents effectively. Mitigation Strategy: Develop and test incident response plans to ensure a timely and effective response to security events."},
        {"check": "Access Controls for Development Systems", "isSafe": True, "detail": "Access controls are implemented for development systems to restrict unauthorized access. Mitigation Strategy: Regularly review and update access permissions based on user roles and responsibilities."},
        {"check": "Secure Coding Practices", "isSafe": True, "detail": "Secure coding practices are followed to prevent vulnerabilities in software applications. Mitigation Strategy: Train developers on secure coding techniques and conduct code reviews to identify and address security issues."},
        {"check": "Data Encryption", "isSafe": True, "detail": "Data encryption is used to protect sensitive information from unauthorized access. Mitigation Strategy: Implement encryption for data at rest and in transit to ensure data security."},
        {"check": "Network Security", "isSafe": False, "detail": "Network security measures are insufficient, potentially exposing systems to attacks. Mitigation Strategy: Enhance network security with firewalls, intrusion detection systems, and regular security assessments."},
        {"check": "Patch Management", "isSafe": True, "detail": "Patch management practices are in place to address security vulnerabilities through timely updates. Mitigation Strategy: Implement automated patch management systems and regularly apply security patches to all systems."},
        {"check": "Backup and Recovery", "isSafe": True, "detail": "Backup and recovery procedures are established to ensure data availability in case of loss. Mitigation Strategy: Perform regular backups and test recovery processes to ensure data can be restored when needed."},
        {"check": "Compliance with Technical Standards", "isSafe": True, "detail": "Compliance with relevant technical standards and best practices is maintained. Mitigation Strategy: Stay updated on industry standards and integrate them into security policies and procedures."}
    ]
}

class OrganizationPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.selectedIndustry = 'finance'
        self.scanStarted = False
        self.scanResults = []
        self.scanCompleted = False
        self.currentCheckIndex = 0
        self.customizeVisible = False
        self.showRuleSelection = False
        self.additionalRules = []
        self.ruleSet = self.getCisRules()
        self.selectedRules = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Organization Scan")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)

        self.industryComboBox = QComboBox()
        self.industryComboBox.addItem("Finance")
        self.industryComboBox.addItem("Education")
        self.industryComboBox.addItem("Technical")
        self.industryComboBox.currentTextChanged.connect(self.handleIndustryChange)
        layout.addWidget(self.industryComboBox)

        self.scanButton = QPushButton("Start Scan")
        self.scanButton.clicked.connect(self.handleScanClick)
        layout.addWidget(self.scanButton)

        self.exportButton = QPushButton("Export PDF")
        self.exportButton.clicked.connect(self.handleExportPDF)
        self.exportButton.setEnabled(False)
        layout.addWidget(self.exportButton)

        self.customizeButton = QPushButton("Customize")
        self.customizeButton.clicked.connect(self.handleCustomizeClick)
        layout.addWidget(self.customizeButton)

        self.customizePanel = QWidget()
        self.customizeLayout = QVBoxLayout(self.customizePanel)
        self.customizePanel.setVisible(False)
        layout.addWidget(self.customizePanel)

        self.scanResultsArea = QScrollArea()
        self.scanResultsWidget = QWidget()
        self.scanResultsLayout = QVBoxLayout(self.scanResultsWidget)
        self.scanResultsArea.setWidget(self.scanResultsWidget)
        layout.addWidget(self.scanResultsArea)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.performScan)

    def getCisRules(self):
        # Returns all CIS rules initially
        return cis_rules

    def handleIndustryChange(self, industry):
        self.selectedIndustry = industry.lower()
        # Update ruleSet based on industry
        self.ruleSet = industry_checks.get(self.selectedIndustry, [])
        self.resetScanState()

    def resetScanState(self):
        self.scanStarted = False
        self.scanResults = []
        self.scanCompleted = False
        self.currentCheckIndex = 0
        self.scanResultsLayout.update()

    def handleScanClick(self):
        self.resetScanState()
        self.scanStarted = True
        self.scanButton.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.timer.start(1000)  # Start the scan with a delay

    def performScan(self):
        if self.scanStarted and not self.scanCompleted:
            if self.currentCheckIndex < len(self.ruleSet):
                result = self.ruleSet[self.currentCheckIndex]
                self.scanResults.append(result)
                resultLabel = QLabel(f"{result['check']}: {'Safe' if result['isSafe'] else 'Unsafe'}\n{result['detail']}")
                self.scanResultsLayout.addWidget(resultLabel)
                self.currentCheckIndex += 1
            else:
                self.scanCompleted = True
                self.scanStarted = False
                self.timer.stop()
                self.scanButton.setEnabled(True)
                self.exportButton.setEnabled(True)

    def handleExportPDF(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if fileName:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Scan Results", ln=True, align='C')
            for result in self.scanResults:
                pdf.multi_cell(0, 10, f"{result['check']}: {'Safe' if result['isSafe'] else 'Unsafe'}\nDetail: {result['detail']}")
            pdf.output(fileName)

    def handleCustomizeClick(self):
        self.customizeVisible = not self.customizeVisible
        self.customizePanel.setVisible(self.customizeVisible)
        if self.customizeVisible:
            # Clear any existing checkboxes
            for i in reversed(range(self.customizeLayout.count())):
                widget = self.customizeLayout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Add new checkboxes for each rule
            for rule in self.getCisRules():
                checkbox = QCheckBox(rule['check'])
                checkbox.stateChanged.connect(self.handleRuleChange)
                self.customizeLayout.addWidget(checkbox)

    def handleRuleChange(self, state):
        # Handle adding/removing rules from selection
        checkbox = self.sender()
        ruleText = checkbox.text()
        if state == 2:  # Checked
            self.selectedRules.append(ruleText)
        else:  # Unchecked
            if ruleText in self.selectedRules:
                self.selectedRules.remove(ruleText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OrganizationPage()
    ex.show()
    sys.exit(app.exec_())
