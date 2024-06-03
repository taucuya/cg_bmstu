from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QFont
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QMessageBox, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QEventLoop, QPoint, QRectF
from PyQt5.uic import loadUi
import sys
from functions import *
from math import radians

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

ui = "./ui/design.ui"

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi(ui, self)

        self.create_scene()
        self.set_start_data()

        self.angle_x_temp = 0
        self.angle_y_temp = 0
        self.angle_z_temp = 0

        self.scale_k_temp = 20

        self.scene_height = 700
        self.scene_width = 700

        self.low_horizon = []
        self.high_horizon = []

        self.rotate_but_x.clicked.connect(self.rotate_x)
        self.rotate_but_y.clicked.connect(self.rotate_y)
        self.rotate_but_z.clicked.connect(self.rotate_z)

        self.scale_button.clicked.connect(self.scale)

        self.draw_button.clicked.connect(self.draw_surface)
        self.exit_button.clicked.connect(self.exit)
        self.clear_button.clicked.connect(self.clear)

    def draw_surface(self):
        self.clear()
        self.draw()

    def draw(self):
        if self.start_x.value() > self.end_x.value():
            return
        if self.start_z.value() > self.end_z.value():
            return

        start_x = self.start_x.value()
        end_x = self.end_x.value()
        step_x = self.step_x.value()

        start_z = self.start_z.value()
        end_z = self.end_z.value()
        step_z = self.step_z.value()

        f = self.get_function()

        self.low_horizon = [self.scene_height for _ in range(self.scene_width)]
        self.high_horizon = [0 for _ in range(self.scene_width)]

        z = end_z

        x_left = -1
        y_left = -1
        x_right = -1
        y_right = -1

        while z >= start_z:
            x_last = start_x
            y_last = f(x_last, z)

            x_last, y_last, z_buf = self.transform(x_last, y_last, z)

            if x_left != -1:
                if self.is_visible(x_left, y_left) and self.is_visible(x_last, y_last):
                    self.draw_line(x_last, y_last, x_left, y_left)
                self.horizon(x_last, y_last, x_left, y_left)

            x_left = x_last
            y_left = y_last

            prev_visibility = self.is_visible(x_last, y_last)
            x = start_x

            while x <= end_x:
                y = f(x, z)

                x_curr, y_curr, z_buf = self.transform(x, y, z)
                curr_visibility = self.is_visible(x_curr, y_curr)

                if prev_visibility == curr_visibility:
                    if curr_visibility: # Если точка видима
                        self.draw_line(x_last, y_last, x_curr, y_curr)
                        self.horizon(x_last, y_last, x_curr, y_curr)
                else:
                    if not curr_visibility: # Если точка невидима
                        if prev_visibility == 1: # Точка выше верхнего горизонта
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.high_horizon)
                        else: # Точка ниже нижнего горизонта
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.low_horizon)

                        self.draw_line(x_last, y_last, x_inter, y_inter)
                        self.horizon(x_last, y_last, x_inter, y_inter)

                    elif curr_visibility == 1: # Если точка видима и выше верхнего горизонта
                        if not prev_visibility: # Если предыдущая точка невидима
                            # Нахождение точки пересечения и отрисовка от точки пересения до текущей точки
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.high_horizon)

                            self.draw_line(x_inter, y_inter, x_curr, y_curr)
                            self.horizon(x_inter, y_inter, x_curr, y_curr)

                        else: # Если предыдущая точка видима
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.low_horizon)

                            self.draw_line(x_last, y_last, x_inter, y_inter)
                            self.horizon(x_last, y_last, x_inter, y_inter)
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.high_horizon)

                            self.draw_line(x_inter, y_inter, x_curr, y_curr)
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                    else: # Если текущая точка видима и ниже нижнего горизонта
                        if not prev_visibility:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.low_horizon)

                            self.draw_line(x_inter, y_inter, x_curr, y_curr)
                            self.horizon(x_inter, y_inter, x_curr, y_curr)
                        else:
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.high_horizon)

                            self.draw_line(x_last, y_last, x_inter, y_inter)
                            self.horizon(x_last, y_last, x_inter, y_inter)
                            x_inter, y_inter = self.intersection(x_last, y_last, x_curr, y_curr, self.low_horizon)
                            self.draw_line(x_inter, y_inter, x_curr, y_curr)
                            self.horizon(x_inter, y_inter, x_curr, y_curr)

                prev_visibility = curr_visibility
                x_last = x_curr
                y_last = y_curr
                x += step_x

            if x_right != -1:
                self.draw_line(x_right, y_right, x_curr, y_curr)
                self.horizon(x_right, y_right, x_curr, y_curr)
            x_right = x_curr
            y_right = y_curr

            z -= step_z

    def horizon(self, x1, y1, x2, y2):
        if x2 == x1:
            if x2 >= self.scene_width:
                return
            self.high_horizon[x2] = max(self.high_horizon[x2], y2)
            self.low_horizon[x2] = min(self.low_horizon[x2], y2)
        else:
            m = (y2 - y1) / (x2 - x1)
            for x in range(x1, x2 + 1):
                if x >= self.scene_width:
                    break
                y = round(m * (x - x1) + y1)
                self.high_horizon[x] = max(self.high_horizon[x], y)
                self.low_horizon[x] = min(self.low_horizon[x], y)

    # нахождение точки пересечения прямых, аппроксимирующих предыдущую и текущую кривые
    def intersection(self, x_start, y_start, x_end, y_end, horizon):

        if x_end == x_start:
            if 0 <= x_end < self.scene.width():
                return x_end, horizon[x_end]
            return self.scene.width() - 1, horizon[self.scene.width() - 1]

        k = (y_end - y_start) / (x_end - x_start)
        sy = self.sign(y_start + k - horizon[x_start + 1])
        sc = sy
        y = y_start + k
        x = x_start + 1
        while sc == sy and x < x_end and x < self.scene.width():
            sc = self.sign(y - horizon[x])
            y += k
            x += 1

        return int(round(x)), int(round(y))

    def sign(self, a):
        if a < 0:
            return -1
        if a > 0:
            return 1
        return 0

    def find_intersection(self, x_n, y_n, x_k, y_k, graph):
        #(x_n, y_n), (x_k, y_k) - соседние точки (i-ая и (i+1)-ая)
        dx = x_k - x_n
        if dx == 0: # если точки совпали
            if 0 <= x_k < self.scene.width():
                x_inter = x_k
                y_inter = graph[x_k]
            else:
                x_inter = self.scene.width() - 1
                y_inter = graph[self.scene.width() - 1]
        else:
            dcurY = y_k - y_n
            dprevY = graph[x_k] - graph[x_n]
            m = dcurY / dx
            x_inter = x_n - int((dx * (y_n - graph[x_n]) / (dcurY - dprevY)))
            y_inter = int(m * (x_inter - x_n) + y_n)

        return x_inter, y_inter

    def is_visible(self, x, y):
        x = int(round(x))
        if x < 0 or x >= self.scene_width:
            return 0 # Не принадлежит экранной области - невидимая точка
        if self.low_horizon[x] < y < self.high_horizon[x]:
            return 0 # Находится между двумя горизонтами - невидимая точка
        if y >= self.high_horizon[x]:
            return 1 # Точка выше верхнего горизонта - видимая точка
        return -1 # Точка ниже нижнего горизонта - видимая точка

    def transform(self, x, y, z):

        x, y, z = self.rotation_x(x, y, z, self.angle_x_temp)
        x, y, z = self.rotation_y(x, y, z, self.angle_y_temp)
        x, y, z = self.rotation_z(x, y, z, self.angle_z_temp)

        x = x * self.scale_k.value() + self.scene_width // 2
        y = y * self.scale_k.value() + self.scene_height // 2

        x = int(round(x))
        y = int(round(y))
        z = int(round(z))

        return x, y, z

    def rotation_x(self, x, y, z, angle):
        buf = y
        angle = radians(angle)
        y = cos(angle) * y - sin(angle) * z
        z = cos(angle) * z + sin(angle) * buf
        return x, y, z

    def rotation_y(self, x, y, z, angle):
        buf = x
        angle = radians(angle)
        x = cos(angle) * x - sin(angle) * z
        z = cos(angle) * z + sin(angle) * buf
        return x, y, z

    def rotation_z(self, x, y, z, angle):
        buf = x
        angle = radians(angle)
        x = cos(angle) * x - sin(angle) * y
        y = cos(angle) * y + sin(angle) * buf
        return x, y, z

    def rotate_x(self):
        self.angle_x_temp += self.angle_x.value()
        self.scene.clear()
        self.draw()

    def rotate_y(self):
        self.angle_y_temp += self.angle_y.value()
        self.scene.clear()
        self.draw()

    def rotate_z(self):
        self.angle_z_temp += self.angle_z.value()
        self.scene.clear()
        self.draw()

    def scale(self):
        self.scale_k_temp = self.scale_k.value()
        self.scene.clear()
        self.draw()

    def draw_dot(self, x, y):
        self.scene.addLine(x, y, x, y, self.get_color())

    def draw_line(self, x1, y1, x2, y2):
        self.scene.addLine(x1, y1, x2, y2, self.get_color())

    def set_start_data(self):
        self.start_x.setValue(-10)
        self.end_x.setValue(10)
        self.step_x.setValue(0.2)
        self.start_z.setValue(-10)
        self.end_z.setValue(10)
        self.step_z.setValue(0.2)
        self.angle_x.setValue(5)
        self.angle_y.setValue(5)
        self.angle_z.setValue(5)
        self.scale_k.setValue(10)

    def show_error(self, msg):
        msg_error = QMessageBox()
        msg_error.setIcon(QMessageBox.Critical)
        msg_error.setStandardButtons(QMessageBox.Close)
        msg_error.setWindowTitle("Ошибка ввода данных")
        msg_error.setText(msg)
        msg_error.exec_()

    def get_color(self):
        color = self.colorComboBox.currentText()
        if color == "Черный":
            return QColor(0, 0, 0)
        if color == "Белый":
            return QColor(255, 255, 255)
        if color == "Красный":
            return QColor(255, 0, 0)
        if color == "Зеленый":
            return QColor(0, 255, 0)
        if color == "Синий":
            return QColor(0, 0, 255)
        if color == "Желтый":
            return QColor(255, 255, 0)
        if color == "Розовый":
            return QColor(255, 110, 150)

    def get_function(self):
        index = self.funcComboBox.currentIndex()
        if index == 0:
            return f1
        if index == 1:
            return f2
        if index == 2:
            return f3
        if index == 3:
            return f4
        if index == 4:
            return f5
        if index == 5:
            return f6

    def create_scene(self):
        self.scene = QGraphicsScene()
        graphicView = QGraphicsView(self.scene, self)
        self.pen = QPen(Qt.black, 5)
        self.scene.setSceneRect(0, 0, 700, 700)
        graphicView.setGeometry(0, 0, 690, 690)
        self.scene.setBackgroundBrush(QColor(255, 255, 255))

    def clear(self):
        self.angle_x_temp = 0
        self.angle_y_temp = 0
        self.angle_z_temp = 0
        self.scale_k_temp = 20
        self.scene.clear()

    def exit(self):
        self.close()

# if __name__ == "__main__":
import sys
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()