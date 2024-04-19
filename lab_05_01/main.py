from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QMessageBox, QTableWidgetItem
from PyQt6.QtGui import QTransform, QPen, QColor, QImage, QPixmap
from PyQt6.uic import loadUi
from points import check_points, makeMid
from fillWPartion import filling

colors = dict(Красный = QColor("#FF0000"), Зеленый = QColor("#00FF00"), \
              Синий = QColor("#0000FF"), Желтый = QColor("#FFB700"), Черный = QColor("black"))

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

        self.scene = QGraphicsScene()
        self.pointArray = []
        self.image = QImage(611, 581, QImage.Format.Format_ARGB32_Premultiplied)
        self.scene.addPixmap(QPixmap.fromImage(self.image))
        self.canvas = QGraphicsView(self.scene, self)
        self.canvas.setGeometry(QRect(10, 0, 611, 581))
        self.canvas.mousePressEvent = self.mouseClick
        self.button_clear.clicked.connect(self.clear)
        self.paint.clicked.connect(self.fillFigure)
        self.got = False

        
    def mouseClick(self, event):
        if self.got:
            self.clear()
            self.got = False
        if event.button() == Qt.MouseButton.RightButton:
            pen = QPen()
            color = self.colorComboBox.currentText()
            pen.setColor(colors[color])
            if len(self.pointArray) > 2:
                self.scene.addLine(self.pointArray[-1].x(), self.pointArray[-1].y(), self.pointArray[0].x(), self.pointArray[0].y(), pen)
        if event.button() == Qt.MouseButton.LeftButton:
            scene_pos = self.canvas.mapToScene(event.pos())
            self.addPoint(QPoint(int(scene_pos.x()), int(scene_pos.y())))

    def clear(self):
        self.pointArray = []
        self.table.setRowCount(0)
        self.scene.clear()
    
    def addPoint(self, point):
        if point not in self.pointArray:
            self.pointArray.append(point)
            pen = QPen()
            color = self.colorComboBox.currentText()
            pen.setColor(colors[color])
            pen.setWidth(1)
            self.scene.addEllipse(point.x(), point.y(), 1, 1, pen)
            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)
            self.table.setItem(rowPosition, 0, QTableWidgetItem(str(point.x())))
            self.table.setItem(rowPosition, 1, QTableWidgetItem(str(point.y())))
            if len(self.pointArray) > 1:
                self.scene.addLine(self.pointArray[rowPosition - 1].x(), self.pointArray[rowPosition - 1].y(), self.pointArray[rowPosition].x(), self.pointArray[rowPosition].y(), pen)
    def fillFigure(self):
        self.got = True
        flag = self.delay.isChecked()

        if not check_points(self.pointArray):
            show_msg('Введено некорректное число точек.')
            self.clear()
            return
        color = self.colorComboBox.currentText()
        mid = makeMid(self.pointArray)
        filling(self.scene, colors[color], self.pointArray, mid[0].x(), flag, self.image)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())