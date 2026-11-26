import ctypes
import os
import sys
import random

if sys.platform == "win32":
    os.environ["QT_QPA_PLATFORM"] = "windows"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "vinig.speedcubeapp.1.0"
    )

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt5.QtCore import QTimer, QElapsedTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QIcon


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


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
    if m == 'U':
        cube.faceMove(x)
        cube.swap(1,2,3,4,0,0,0,0)
        cube.swap(1,2,3,4,1,1,1,1)
        cube.swap(1,2,3,4,2,2,2,2)
    elif m == "U'":
        cube.faceMovePrime(x)
        cube.swap(1,4,3,2,0,0,0,0)
        cube.swap(1,4,3,2,1,1,1,1)
        cube.swap(1,4,3,2,2,2,2,2)
    elif m == 'U2':
        move(cube, 'U', x)
        move(cube, 'U', x)
    elif m == 'D':
        cube.faceMove(x)
        cube.swap(1,4,3,2,4,4,4,4)
        cube.swap(1,4,3,2,5,5,5,5)
        cube.swap(1,4,3,2,6,6,6,6)
    elif m == "D'":
        cube.faceMovePrime(x)
        cube.swap(1,2,3,4,4,4,4,4)
        cube.swap(1,2,3,4,5,5,5,5)
        cube.swap(1,2,3,4,6,6,6,6)
    elif m == 'D2':
        move(cube, 'D', x)
        move(cube, 'D', x)
    elif m == 'R':
        cube.faceMove(x)
        cube.swap(0,2,5,4,2,2,2,6)
        cube.swap(0,2,5,4,3,3,3,7)
        cube.swap(0,2,5,4,4,4,4,0)
    elif m == "R'":
        cube.faceMovePrime(x)
        cube.swap(0,4,5,2,2,6,2,2)
        cube.swap(0,4,5,2,3,7,3,3)
        cube.swap(0,4,5,2,4,0,4,4)
    elif m == 'R2':
        move(cube, 'R', x)
        move(cube, 'R', x)
    elif m == 'L':
        cube.faceMove(x)
        cube.swap(0,4,5,2,6,2,6,6)
        cube.swap(0,4,5,2,7,3,7,7)
        cube.swap(0,4,5,2,0,4,0,0)
    elif m == "L'":
        cube.faceMovePrime(x)
        cube.swap(0,2,5,4,6,6,6,2)
        cube.swap(0,2,5,4,7,7,7,3)
        cube.swap(0,2,5,4,0,0,0,4)
    elif m == 'L2':
        move(cube, 'L', x)
        move(cube, 'L', x)
    elif m == 'F':
        cube.faceMove(x)
        cube.swap(0,1,5,3,4,2,0,6)
        cube.swap(0,1,5,3,5,3,1,7)
        cube.swap(0,1,5,3,6,4,2,0)
    elif m == "F'":
        cube.faceMovePrime(x)
        cube.swap(0,3,5,1,4,6,0,2)
        cube.swap(0,3,5,1,5,7,1,3)
        cube.swap(0,3,5,1,6,0,2,4)
    elif m == 'F2':
        move(cube, 'F', x)
        move(cube, 'F', x)
    elif m == 'B':
        cube.faceMove(x)
        cube.swap(0,3,5,1,0,2,4,6)
        cube.swap(0,3,5,1,1,3,5,7)
        cube.swap(0,3,5,1,2,4,6,0)
    elif m == "B'":
        cube.faceMovePrime(x)
        cube.swap(0,1,5,3,0,6,4,2)
        cube.swap(0,1,5,3,1,7,5,3)
        cube.swap(0,1,5,3,2,0,6,4)
    elif m == 'B2':
        move(cube, 'B', x)
        move(cube, 'B', x)


def scramble(scr, length):
    cube = Cube()
    moves = ['U', 'L', 'F', 'R', 'B', 'D']
    for x in scr:
        move(cube, str(x[0]) + str(x[1]), moves.index(x[0]))
    return cube


def gen_scramble():
    moves = ["U", "D", "F", "B", "R", "L"]
    dir_options = ["", "'", "2"]
    slen = random.randint(25, 28)
    s = valid([[random.choice(moves), random.choice(dir_options)] for x in range(slen)])
    cube = scramble(s, slen)
    return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + "[" + str(slen) + "]", cube


def valid(ar):
    moves = ["U", "D", "F", "B", "R", "L"]
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x - 1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x - 2][0] or ar[x][0] == ar[x - 1][0]:
            ar[x][0] = random.choice(moves)
    return ar


class CubeNetWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cube = Cube()
        self.setMinimumSize(240, 180)
        self.colors = {
            'w': QColor("#ffffff"),
            'o': QColor("#ff8800"),
            'g': QColor("#00cc44"),
            'r': QColor("#ee2222"),
            'b': QColor("#2266ff"),
            'y': QColor("#ffdd00")
        }
        self.centers = ['w', 'o', 'g', 'r', 'b', 'y']
        self.ring_map = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
        self.face_grid = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]

    def set_cube(self, cube):
        self.cube = cube
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        size = 16
        gap = 2
        face_size = (size + gap) * 3 + 4

        offset_x = (self.width() - (face_size * 4)) // 2
        offset_y = (self.height() - (face_size * 3)) // 2

        for f_idx, (gx, gy) in enumerate(self.face_grid):
            fx = offset_x + gx * face_size
            fy = offset_y + gy * face_size

            painter.setBrush(self.colors[self.centers[f_idx]])
            painter.setPen(QColor("#11111b"))
            painter.drawRoundedRect(fx + (size + gap), fy + (size + gap), size, size, 3, 3)

            for s_idx, (sx, sy) in enumerate(self.ring_map):
                color_key = self.cube.cube[f_idx][s_idx]
                painter.setBrush(self.colors[color_key])
                painter.drawRoundedRect(fx + sx * (size + gap), fy + sy * (size + gap), size, size, 3, 3)


class SpeedCubingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._drag_pos = None
        self._was_dragged = False
        self.setWindowIcon(QIcon(resource_path("icon.ico")))

        self.time_label = QLabel("00:00.000", self)
        self.start_button = QPushButton("Start/Stop", self)
        self.scramble_label = QLabel("", self)
        self.new_scramble_button = QPushButton("New Scramble", self)
        self.av_of_5 = QLabel("Ao5:", self)
        self.history_list = QListWidget(self)
        self.cube_net = CubeNetWidget(self)

        self.elapsed_timer = QElapsedTimer()
        self.timer = QTimer(self)
        self.t_has_stop = False
        self.solves = []

        self.initUI()
        self.generate_new_scramble()

    def initUI(self):
        self.setWindowTitle("SPEED CUBE")
        self.setGeometry(100, 100, 800, 480)

        main_layout = QHBoxLayout()
        vbox_left = QVBoxLayout()

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #89b4fa;")
        vbox_left.addWidget(self.time_label)

        self.av_of_5.setAlignment(Qt.AlignCenter)
        self.av_of_5.setStyleSheet("font-size: 24px; font-weight: bold; color: #cdd6f4; margin-bottom: 10px;")
        vbox_left.addWidget(self.av_of_5)

        vbox_left.addWidget(self.start_button)

        self.scramble_label.setAlignment(Qt.AlignCenter)
        self.scramble_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px; color: #cdd6f4;")
        self.scramble_label.setWordWrap(True)
        vbox_left.addWidget(self.scramble_label)

        vbox_left.addWidget(self.new_scramble_button)

        vbox_right = QVBoxLayout()
        sidebar_title = QLabel("Times List", self)
        sidebar_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        vbox_right.addWidget(sidebar_title)
        vbox_right.addWidget(self.history_list)
        vbox_right.addWidget(self.cube_net)

        main_layout.addLayout(vbox_left, 3)
        main_layout.addLayout(vbox_right, 2)
        self.setLayout(main_layout)

        self.start_button.clicked.connect(self.toggle_timer)
        self.new_scramble_button.clicked.connect(self.generate_new_scramble)
        self.timer.timeout.connect(self.update_display)

        self.start_button.setFocusPolicy(Qt.NoFocus)
        self.new_scramble_button.setFocusPolicy(Qt.NoFocus)
        self.history_list.setFocusPolicy(Qt.NoFocus)

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
        elif not self.t_has_stop:
            self.start()
            self.t_has_stop = False
        else:
            self.reset()
            self.t_has_stop = False
            self.generate_new_scramble()

    def start(self):
        if not self.timer.isActive():
            self.elapsed_timer.start()
            self.timer.start(12)

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
            current_solve_time = self.elapsed_timer.elapsed() / 1000.0
            self.solves.append(current_solve_time)
            formatted_time = f"{current_solve_time:.3f}"
            self.time_label.setText(formatted_time)
            self.history_list.addItem(f"{len(self.solves)}. {formatted_time}s")
            self.history_list.scrollToBottom()
            self.update_ao5()

    def reset(self):
        self.time_label.setText("0.000")

    def update_display(self):
        elapsed = self.elapsed_timer.elapsed() / 1000.0
        self.time_label.setText(f"{elapsed:.3f}")

    def generate_new_scramble(self):
        scr_text, cube = gen_scramble()
        self.scramble_label.setText(scr_text)
        self.cube_net.set_cube(cube)

    def update_ao5(self):
        if len(self.solves) >= 5:
            last_5 = sorted(self.solves[-5:])
            ao5 = sum(last_5[1:4]) / 3.0
            self.av_of_5.setText(f"Ao5: {ao5:.3f}s")


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("icon.ico")))
    qss = """
    QWidget {
        background-color: #181825;
        color: #cdd6f4;
        font-family: "Segoe UI", "Helvetica Neue", "Roboto", sans-serif;
    }
    QPushButton {
        background-color: #313244;
        color: #cdd6f4;
        border: 1px solid #45475a;
        border-radius: 8px;
        padding: 10px 18px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #45475a;
        border-color: #89b4fa;
    }
    QPushButton:pressed {
        background-color: #585b70;
    }
    QListWidget {
        background-color: #1e1e2e;
        border: 1px solid #313244;
        border-radius: 8px;
        padding: 6px;
        font-size: 14px;
    }
    QListWidget::item {
        padding: 6px;
        border-bottom: 1px solid #313244;
    }
    """
    app.setStyleSheet(qss)
    

    window = SpeedCubingApp()
    window.show()
    sys.exit(app.exec_())
