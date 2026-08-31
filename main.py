import os
os.environ["QT_QPA_PLATFORM"] = "windows"
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QElapsedTimer, Qt


class Cube:
    def __init__(self):
        self.cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], 
                     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 
                     ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], 
                     ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], 
                     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 
                     ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]

    def faceMove(self, x):
        self.cube[x][0], self.cube[x][6], self.cube[x][4], self.cube[x][2] = self.cube[x][6], self.cube[x][4], self.cube[x][2], self.cube[x][0]
        self.cube[x][1], self.cube[x][7], self.cube[x][5], self.cube[x][3] = self.cube[x][7], self.cube[x][5], self.cube[x][3], self.cube[x][1]

    def faceMovePrime(self, x):
        self.cube[x][0], self.cube[x][2], self.cube[x][4], self.cube[x][6] = self.cube[x][2], self.cube[x][4], self.cube[x][6], self.cube[x][0]
        self.cube[x][1], self.cube[x][3], self.cube[x][5], self.cube[x][7] = self.cube[x][3], self.cube[x][5], self.cube[x][7], self.cube[x][1]

    def swap(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.cube[x1][y1], self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4] = self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4], self.cube[x1][y1]


def move(cube, m, x):
    if(m == 'U'):
        cube.faceMove(x)
        cube.swap(1,2,3,4,0,0,0,0)
        cube.swap(1,2,3,4,1,1,1,1)
        cube.swap(1,2,3,4,2,2,2,2)
    elif(m == "U'"):
        cube.faceMovePrime(x)
        cube.swap(1,4,3,2,0,0,0,0)
        cube.swap(1,4,3,2,1,1,1,1)
        cube.swap(1,4,3,2,2,2,2,2)
    elif(m == 'U2'):
        move(cube, 'U', x)
        move(cube, 'U', x)
    elif(m == 'D'):
        cube.faceMove(x)
        cube.swap(1,4,3,2,4,4,4,4)
        cube.swap(1,4,3,2,5,5,5,5)
        cube.swap(1,4,3,2,6,6,6,6)
    elif(m == "D'"):
        cube.faceMovePrime(x)
        cube.swap(1,2,3,4,4,4,4,4)
        cube.swap(1,2,3,4,5,5,5,5)
        cube.swap(1,2,3,4,6,6,6,6)
    elif(m == 'D2'):
        move(cube, 'D', x)
        move(cube, 'D', x)
    elif(m == 'R'):
        cube.faceMove(x)
        cube.swap(0,2,5,4,2,2,2,6)
        cube.swap(0,2,5,4,3,3,3,7)
        cube.swap(0,2,5,4,4,4,4,0)
    elif(m == "R'"):
        cube.faceMovePrime(x)
        cube.swap(0,4,5,2,2,6,2,2)
        cube.swap(0,4,5,2,3,7,3,3)
        cube.swap(0,4,5,2,4,0,4,4)
    elif(m == 'R2'):
        move(cube, 'R', x)
        move(cube, 'R', x)
    elif(m == 'L'):
        cube.faceMove(x)
        cube.swap(0,4,5,2,6,2,6,6)
        cube.swap(0,4,5,2,7,3,7,7)
        cube.swap(0,4,5,2,0,4,0,0)
    elif(m == "L'"):
        cube.faceMovePrime(x)
        cube.swap(0,2,5,4,6,6,6,2)
        cube.swap(0,2,5,4,7,7,7,3)
        cube.swap(0,2,5,4,0,0,0,4)
    elif(m == 'L2'):
        move(cube, 'L', x)
        move(cube, 'L', x)
    elif(m == 'F'):
        cube.faceMove(x)
        cube.swap(0,1,5,3,4,2,0,6)
        cube.swap(0,1,5,3,5,3,1,7)
        cube.swap(0,1,5,3,6,4,2,0)
    elif(m == "F'"):
        cube.faceMovePrime(x)
        cube.swap(0,3,5,1,4,6,0,2)
        cube.swap(0,3,5,1,5,7,1,3)
        cube.swap(0,3,5,1,6,0,2,4)
    elif(m == 'F2'):
        move(cube, 'F', x)
        move(cube, 'F', x)
    elif(m == 'B'):
        cube.faceMove(x)
        cube.swap(0,3,5,1,0,2,4,6)
        cube.swap(0,3,5,1,1,3,5,7)
        cube.swap(0,3,5,1,2,4,6,0)
    elif(m == "B'"):
        cube.faceMovePrime(x)
        cube.swap(0,1,5,3,0,6,4,2)
        cube.swap(0,1,5,3,1,7,5,3)
        cube.swap(0,1,5,3,2,0,6,4)
    elif(m == 'B2'):
        move(cube, 'B', x)
        move(cube, 'B', x)


def scramble(scr, length):
    cube = Cube()
    moves = ['U', 'L', 'F', 'R', 'B', 'D']
    for x in scr:
        move(cube, str(x[0])+str(x[1]), moves.index(x[0]))


def gen_scramble():
    moves = ["U", "D", "F", "B", "R", "L"]
    dir_options = ["", "'", "2"]
    slen = random.randint(25, 28)
    
    s = valid([[random.choice(moves), random.choice(dir_options)] for x in range(slen)])
    scramble(s, slen)
    
    return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + "[" + str(slen) + "]"


def valid(ar):
    moves = ["U", "D", "F", "B", "R", "L"]
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar


class SpeedCubingApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.time_label = QLabel("00:00:00.000", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        
        self.scramble_label = QLabel("R U' F2 B D' L2...[27]", self)
        self.new_scramble_button = QPushButton("New Scramble", self)
        
        self.elapsed_timer = QElapsedTimer()
        self.timer = QTimer(self)
        self.elapsed_saved = 0 
        self.t_has_stop = False
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SPEED CUBE")
        self.setGeometry(100, 100, 600, 300)
        
        vbox = QVBoxLayout()
        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 60px; font-weight: bold;")
        vbox.addWidget(self.time_label)
        
        hbox_timer = QHBoxLayout()
        hbox_timer.addWidget(self.start_button)
        hbox_timer.addWidget(self.stop_button)
        hbox_timer.addWidget(self.reset_button)
        vbox.addLayout(hbox_timer)
        
        self.scramble_label.setAlignment(Qt.AlignCenter)
        self.scramble_label.setStyleSheet("font-size: 14px; font-weight: bold; padding: 10px;")
        vbox.addWidget(self.scramble_label)
        
        vbox.addWidget(self.new_scramble_button)
        
        self.setLayout(vbox)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.new_scramble_button.clicked.connect(self.generate_new_scramble)
        self.timer.timeout.connect(self.update_display)

        self.start_button.setFocusPolicy(Qt.NoFocus)
        self.stop_button.setFocusPolicy(Qt.NoFocus)
        self.reset_button.setFocusPolicy(Qt.NoFocus)
        self.new_scramble_button.setFocusPolicy(Qt.NoFocus)

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

    def generate_new_scramble(self):
        scramble_text = gen_scramble()
        self.scramble_label.setText(scramble_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    speed_cubing = SpeedCubingApp()
    speed_cubing.show()
    sys.exit(app.exec_())
