import os
os.environ["QT_QPA_PLATFORM"] = "windows"
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QElapsedTimer, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00.000", self)
        self.start_button = QPushButton("Start Cubin", self)
        self.stop_button = QPushButton("Stop Cubin", self)
        self.reset_button = QPushButton("Back to zero", self)
        
        self.elapsed_timer = QElapsedTimer()
        self.timer = QTimer(self)
        self.elapsed_saved = 0 
        
        self.t_has_stop = False
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SPEED CUBE")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

        self.start_button.setFocusPolicy(Qt.NoFocus)
        self.stop_button.setFocusPolicy(Qt.NoFocus)
        self.reset_button.setFocusPolicy(Qt.NoFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.toggle_timer()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.toggle_timer()


    def toggle_timer(self):
        if self.timer.isActive():
            self.stop()
            self.t_has_stop = True
        elif self.t_has_stop == False:
            self.start()
            self.t_has_stop = False
        elif self.t_has_stop == True:
            self.reset()
            self.t_has_stop = False

    def start(self):
        if not self.timer.isActive():
            self.elapsed_timer.start()
            self.timer.start(12) 

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
            self.elapsed_saved += self.elapsed_timer.elapsed()

    def reset(self):
        self.timer.stop()
        self.elapsed_saved = 0
        self.time_label.setText("00:00:00.000")

    def update_display(self):
        total_ms = self.elapsed_saved + self.elapsed_timer.elapsed()
        
        hours = total_ms // 3600000
        minutes = (total_ms % 3600000) // 60000
        seconds = (total_ms % 60000) // 1000
        milliseconds = total_ms % 1000
        
        self.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
