from PyQt6.QtCore import Qt, QPointF, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QMessageBox
from PyQt6.QtGui import QTransform
from PyQt6.uic import loadUi
from choose_alg import choose

ui = "./ui/design.ui"

def isFloat(str: str) -> bool:
    try:
        float(str)
    except Exception:
        return False
    else:
        return True

def show_msg(str):
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()

def readAmountStep(amount, step):
    if (not isFloat(step)) or (not amount.isdigit()):
        show_msg("Некорректные данные для спектра")
        return
    return int(amount), float(step)
    


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi(ui, self)

        transform = QTransform()
        transform.scale(1, -1)
        self.scene = QGraphicsScene()
        self.canvas = QGraphicsView(self.scene, self)
        self.canvas.setGeometry(QRect(260, 10, 800, 690))
        self.canvas.setTransform(transform)
        self.button_author.clicked.connect(self.show_message_box_author)
        self.button_prog.clicked.connect(self.show_message_box_prog)
        self.figureDrawButton.clicked.connect(lambda: self.choose_algorithm("simple"))
        self.rangeDrawButton.clicked.connect(lambda: self.choose_algorithm('range'))
        self.clearButton.clicked.connect(self.clear_all)


    def show_message_box_author(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('Об авторе')
        msg.setText("Шатохина Таисия Павловна ИУ7-41Б")
        msg.exec()

    def show_message_box_prog(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('О программе')
        msg.setText("Программа рисует окружность и эллипс с помощью 5 различных способов. \
                    Также есть возможность нарисовать их спектры.")
        msg.exec()  
    
    def choose_algorithm(self, prob: str) -> None:
        alg = self.algorithmComboBox.currentText()
        color = self.colorComboBox.currentText()
        if (not isFloat(self.centerXField.text())) or (not isFloat(self.centerYField.text())):
            show_msg('Некорректно введен центр фигуры.')
            return
        else:
            x_center = float(self.centerXField.text())
            y_center = float(self.centerYField.text())
            center_point = QPointF(x_center, y_center)
            
        
        type = self.figureTypeComboBox.currentText()
        if (type == 'Окружность'):            
            if (not isFloat(self.radiusField.text())):
                show_msg("Некорректный радиус для окружности.")
            else:
                radius = float(self.radiusField.text())
                if prob == 'simple':
                    choose(self.scene, alg, color, "circle", center_point, radius=radius)
                else:
                    amount, step = readAmountStep(self.amountField.text(), self.stepField.text())
                    choose(self.scene, alg, color, "circle_range", center_point, radius=radius, amount=amount, step=step)

        elif (type == 'Эллипс'):            
            if (not isFloat(self.axisXField.text()) or (not isFloat(self.axisYField.text()))):
                show_msg("Некорректные полуоси для эллипса.")
            else:
                axis_x = float(self.axisXField.text())
                axis_y = float(self.axisYField.text())
                if prob == 'simple':
                    choose(self.scene, alg, color, "ellipse", center_point, axisX=axis_x, axisY=axis_y)
                else:
                    amount, step = readAmountStep(self.amountField.text(), self.stepField.text())
                    choose(self.scene, alg, color, "ellipse_range", center_point, axisX=axis_x, axisY=axis_y, amount=amount, step=step)

        self.centerXField.setText('0')
        self.centerYField.setText('0')
        self.radiusField.setText('1')
        self.axisXField.setText('1')
        self.axisYField.setText('1')
        self.amountField.setText('1')
        self.stepField.setText('1')

    def clear_all(self) -> None:
        self.scene.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())