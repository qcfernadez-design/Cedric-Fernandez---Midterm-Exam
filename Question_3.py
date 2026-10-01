import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class MidtermWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Midterm in OOP")
        self.resize(600, 300)
        
        self.label = QLabel("Enter your fullname:")
        self.label.setStyleSheet("color: red;")
        
        self.entry_input = QLineEdit()
        
        self.button = QPushButton("Click to display your fullname")
        self.button.setStyleSheet("color: red;")
        self.button.clicked.connect(self.display_fullname)
        
        self.entry_output = QLineEdit()
        self.entry_output.setReadOnly(True)  
        
        grid = QGridLayout()
        grid.setSpacing(20)
        
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry_input, 0, 1)
        grid.addWidget(self.button, 1, 0)
        grid.addWidget(self.entry_output, 1, 1)
        
        grid.setContentsMargins(50, 80, 50, 80)
        self.setLayout(grid)

    def display_fullname(self):
        text = self.entry_input.text()
        self.entry_output.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MidtermWindow()
    window.show()
    sys.exit(app.exec())