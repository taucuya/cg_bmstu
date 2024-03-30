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

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi(ui, self)

        transform = QTransform()
        transform.scale(1, -1)
        self.scene = QGraphicsScene()
        self.canvas = QGraphicsView(self.scene, self)
        self.canvas.setGeometry(QRect(250, 10, 861, 731))
        self.canvas.setTransform(transform)

        self.button_author.clicked.connect(self.show_message_box_author)
        self.button_prog.clicked.connect(self.show_message_box_prog)
        self.lineDrawButton.clicked.connect(self.choose_line_algorithm)
        self.rangeDrawButton.clicked.connect(self.choose_range_algorithm)
        self.clearButton.clicked.connect(self.clear_all)


    def show_message_box_author(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('Об авторе')
        msg.setText("Шатохина Таисия Павловна ИУ7-41Б")
        msg.exec()

    def show_message_box_prog(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('О программе')
        msg.setText(".") # Напиши описание программы
        msg.exec()  
    
    def choose_line_algorithm(self) -> None:
        alg = self.lineAlgorithmComboBox.currentText()
        color = self.lineColorComboBox.currentText()
        if (not isFloat(self.startXField.text())) or (not isFloat(self.startYField.text())) \
            or (not isFloat(self.endXField.text())) or (not isFloat(self.endYField.text())):
            show_msg("Некорректные координаты точки.")
        else:
            x_start = float(self.startXField.text())
            y_start = float(self.startYField.text())
            x_end = float(self.endXField.text())
            y_end = float(self.endYField.text())
            start_point = QPointF(x_start, y_start)
            end_point = QPointF(x_end, y_end)
            
            choose(self.scene, alg, color, "line", start_point, end_point, None, None)

        self.startXField.setText('0')
        self.startYField.setText('0')
        self.endXField.setText('0')
        self.endYField.setText('0')

    def choose_range_algorithm(self) -> None:
        alg = self.rangeAlgorithmComboBox.currentText()
        color = self.rangeColorComboBox.currentText()
        if (not isFloat(self.rangeLengthField.text())) or (not isFloat(self.rangeAngleField.text())):
            show_msg("Некорректные длина отрезка или угол рассеивания.")
        else:
            length = float(self.rangeLengthField.text())
            angle = float(self.rangeAngleField.text())

            choose(self.scene, alg, color, "spect", None, None, length, angle)

        self.rangeLengthField.setText('0')
        self.rangeAngleField.setText('0')

    def clear_all(self) -> None:
        self.scene.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())