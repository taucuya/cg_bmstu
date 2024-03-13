from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QMessageBox
from design import Ui_MainWindow
from transformation import BirdWidget

def show_msg(str):
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()

def isFloat(str: str) -> bool:
    try:
        float(str)
    except Exception:
        return False
    else:
        return True


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.button_author.clicked.connect(self.show_message_box_author)
        self.button_prog.clicked.connect(self.show_message_box_prog)
        self.bird_widget = BirdWidget()
        self.scene.addWidget(self.bird_widget)
        self.button_transform.clicked.connect(self.transform)
        self.button_reset.clicked.connect(self.reset)


    def transform(self) -> None:
        # Moving bird
        cnt = 0
        if (isFloat(self.edit_x_mov.text()) and isFloat(self.edit_y_mov.text())):
            x_mov = float(self.edit_x_mov.text())
            y_mov = float(self.edit_y_mov.text())
            move_point = QPointF(x_mov, y_mov)
            self.bird_widget.moveToPoint(move_point)
        else: cnt += 1;
        self.edit_x_mov.setText('')
        self.edit_y_mov.setText('')

        # Resizing bird
        if isFloat(self.edit_size.text()):
            size = float(self.edit_size.text())
            if size == 0:
                show_msg("Данное масштабирование недопустимо.")
            else:
                if (isFloat(self.edit_x_center_size.text()) and isFloat(self.edit_y_center_size.text())):
                    x_size_center = float(self.edit_x_center_size.text())
                    y_size_center = float(self.edit_y_center_size.text())
                    scale_point = QPointF(x_size_center, y_size_center)
                else: scale_point = QPointF(0, 0);
                self.bird_widget.scaleAll(scale_point, size, size)
                self.bird_widget.scale_x *= size
                self.bird_widget.scale_y *= size
        else: cnt += 1;

        # Rotating bird
        if isFloat(self.edit_angle.text()):
            angle = float(self.edit_angle.text())
            if (isFloat(self.edit_x_center_spin.text() and isFloat(self.edit_y_center_spin.text()))):
                x_rotate = float(self.edit_x_center_spin.text())
                y_rotate = float(self.edit_y_center_spin.text())
                rotate_point = QPointF(x_rotate, y_rotate)
            else: rotate_point = QPointF(0, 0);
            self.bird_widget.angleAll(rotate_point, angle)
        else: cnt += 1;

        if cnt == 3:
            show_msg("Картинка не будет изменена.")
        self.clearInputFields()
        self.bird_widget.update()

    def clearInputFields(self):
        fields = [self.edit_x_mov, self.edit_y_mov, self.edit_size, self.edit_x_center_size,
                      self.edit_y_center_size, self.edit_angle, self.edit_x_center_spin, self.edit_y_center_spin]

        for i in fields:
            i.setText('')

    def reset(self) -> None:
        self.bird_widget.reset()
        self.bird_widget.update()

    def show_message_box_author(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('Об авторе')
        msg.setText("Шатохина Таисия Павловна ИУ7-41Б")
        msg.exec()

    def show_message_box_prog(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('О программе')
        msg.setText("Программа решает задачу перемещения, масштабирования и поворота рисунка.")
        msg.exec()




if __name__ == "__main__":
    import sys
    mas = []
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())