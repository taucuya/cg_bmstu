from PyQt6.QtCore import Qt, QPoint, QRectF, QPointF, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QMessageBox, QTableWidgetItem
from PyQt6.QtGui import QPen, QColor, QImage, QPixmap
from PyQt6.uic import loadUi
from solve_7 import clip_segments

colors = dict(Красный = "#ff0000", Зеленый = "#00ff00", \
              Синий = "#0000ff", Желтый = "#ffb700", Черный = "#000000")

types = dict(Прямоугольник = 4, Многоугольник = 6, Отрезок = 2)

ui = "./ui/design.ui"
def show_msg(str):
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi(ui, self)

        self.done = False
        self.oneCutter = False
        self.oneCutting = False
        self.scene = QGraphicsScene()
        self.pointCutterArray = []
        self.pointCuttingArray = []
        self.image = QImage(611, 581, QImage.Format.Format_ARGB32_Premultiplied)
        self.scene.addPixmap(QPixmap.fromImage(self.image))
        self.canvas = QGraphicsView(self.scene, self)
        self.canvas.setGeometry(QRect(10, 0, 611, 581))
        self.canvas.mousePressEvent = self.mouseClick
        self.closeCutter.clicked.connect(self.cutterClosing)
        self.closeCutting.clicked.connect(self.cuttingClosing)
        self.buttonClear.clicked.connect(self.clear)
        self.solve.clicked.connect(self.solution)


    def cutterClosing(self):
        pen = QPen()
        color = self.colorCutterComboBox.currentText()
        pen.setColor(QColor(colors[color]))
        type = types[self.cutterComboBox.currentText()]
        if type == 4:
            return
        else:
            self.scene.addLine(self.pointCutterArray[-1].x(), self.pointCutterArray[-1].y(), \
                                       self.pointCutterArray[0].x(), self.pointCutterArray[0].y(), pen)
            self.oneCutter = True
            
    def cuttingClosing(self):
        pen = QPen()
        color = self.colorCuttingComboBox.currentText()
        pen.setColor(QColor(colors[color]))
        type = types[self.cuttingComboBox.currentText()]
        if type == 2:
            return
        else:
            self.scene.addLine(self.pointCuttingArray[-1].x(), self.pointCuttingArray[-1].y(), \
                                    self.pointCuttingArray[0].x(), self.pointCuttingArray[0].y(), pen)
            self.oneCutting = True
        
    def mouseClick(self, event):
        scene_pos = self.canvas.mapToScene(event.pos())
        if event.button() == Qt.MouseButton.LeftButton:
            pen = QPen()
            color = self.colorCuttingComboBox.currentText()
            pen.setColor(QColor(colors[color]))
            type = types[self.cuttingComboBox.currentText()]
            if type == 2:
                if self.done:
                    return
                if len(self.pointCuttingArray) % 2 == 0:
                    self.scene.addLine(scene_pos.x(), scene_pos.y(), scene_pos.x(), scene_pos.y(), pen)
                    self.pointCuttingArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
                else:
                    self.scene.addLine(self.pointCuttingArray[-1].x(), self.pointCuttingArray[-1].y(), \
                                       scene_pos.x(), scene_pos.y(), pen)
                    self.pointCuttingArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
            if type == 6:
                if self.oneCutting:
                    return
                
                if len(self.pointCuttingArray) == 0:
                    self.scene.addLine(scene_pos.x(), scene_pos.y(), scene_pos.x(), scene_pos.y(), pen)
                    self.pointCuttingArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
                else:
                    self.scene.addLine(self.pointCuttingArray[-1].x(), self.pointCuttingArray[-1].y(), \
                                       scene_pos.x(), scene_pos.y(), pen)
                    self.pointCuttingArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
            
        if event.button() == Qt.MouseButton.RightButton:
            pen = QPen()
            color = self.colorCutterComboBox.currentText()
            pen.setColor(QColor(colors[color]))
            type = types[self.cutterComboBox.currentText()]
            if type == 4:
                if len(self.pointCutterArray) == 2:
                    return
                if len(self.pointCutterArray) == 0:
                    self.scene.addLine(scene_pos.x(), scene_pos.y(), scene_pos.x(), scene_pos.y(), pen)
                    self.pointCutterArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
                else:
                    self.scene.addRect(QRectF(QPointF(self.pointCutterArray[0].x(), self.pointCutterArray[0].y()), scene_pos), pen)
                    self.pointCutterArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))

            if type == 6:
                if self.oneCutter:
                    return
                if len(self.pointCutterArray) == 0:
                    self.scene.addLine(scene_pos.x(), scene_pos.y(), scene_pos.x(), scene_pos.y(), pen)
                    self.pointCutterArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))
                else:
                    self.scene.addLine(self.pointCutterArray[-1].x(), self.pointCutterArray[-1].y(), \
                                       scene_pos.x(), scene_pos.y(), pen)
                    self.pointCutterArray.append(QPoint(int(scene_pos.x()), int(scene_pos.y())))

    def clear(self):
        self.pointCutterArray = []
        self.pointCuttingArray = []
        self.scene.clear()
        self.done = False
        self.oneCutter = False
        self.oneCutting = False
    

    def solution(self):
        if self.done:
            self.clear()
            
        pen = QPen()
        pen.setColor(QColor("#02d6f2"))
        clipped_segments = clip_segments(self.pointCuttingArray, self.pointCutterArray)
        if clipped_segments:
            for clipped_segment in clipped_segments:
                self.scene.addLine(clipped_segment[0].x(), clipped_segment[0].y(), \
                                       clipped_segment[1].x(), clipped_segment[1].y(), pen)
        self.done = True
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())