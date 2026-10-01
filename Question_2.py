import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class ExamWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.resize(500, 300)
        
        self.button = QPushButton("Click to Change Color")
        self.button.setFixedSize(200, 30)
        self.button.clicked.connect(self.change_color)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def change_color(self):
        self.button.setStyleSheet("background-color: yellow;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExamWindow()
    window.show()
    sys.exit(app.exec())