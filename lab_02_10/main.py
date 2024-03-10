import sys
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QMessageBox
from design import Ui_MainWindow
from transformation import BirdWidget

def show_msg(str):
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()

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
        try:
            x_mov = float(self.edit_x_mov.text())
            y_mov = float(self.edit_y_mov.text())
        except Exception:
            show_msg("Некорректные координаты для смещения.")
            self.edit_x_mov.setText('0')
            self.edit_y_mov.setText('0')
        else:
            move_point = QPointF(x_mov, y_mov)
            self.bird_widget.moveToPoint(move_point)
            self.edit_x_mov.setText('0')
            self.edit_y_mov.setText('0')

        # Resizing bird
        try:
            x_size = float(self.edit_x_size.text())
            y_size = float(self.edit_y_size.text())
        except Exception:
            self.edit_x_size.setText('1')
            self.edit_y_size.setText('1')
            self.edit_x_center_size.setText('0')
            self.edit_y_center_size.setText('0')
        else:
            if x_size == 0 or y_size == 0:
                show_msg("Данное масштабирование недопустимо.")
                self.edit_x_size.setText('1')
                self.edit_y_size.setText('1')
                self.edit_x_center_size.setText('0')
                self.edit_y_center_size.setText('0')
            else:
                try:
                    x_size_center = float(self.edit_x_center_size.text())
                    y_size_center = float(self.edit_y_center_size.text())
                except Exception:
                    x_size_center = 0
                    y_size_center = 0
                    scale_point = QPointF(x_size_center, y_size_center)
                    self.bird_widget.scaleAll(scale_point, x_size, y_size)
                    self.bird_widget.scale_x *= x_size
                    self.bird_widget.scale_y *= y_size
                    self.edit_x_size.setText('1')
                    self.edit_y_size.setText('1')
                    self.edit_x_center_size.setText('0')
                    self.edit_y_center_size.setText('0')
                    self.bird_widget.update()
                else:
                    scale_point = QPointF(x_size_center, y_size_center)
                    self.bird_widget.scaleAll(scale_point, x_size, y_size)
                    self.bird_widget.scale_x *= x_size
                    self.bird_widget.scale_y *= y_size
                    self.edit_x_size.setText('1')
                    self.edit_y_size.setText('1')
                    self.edit_x_center_size.setText('0')
                    self.edit_y_center_size.setText('0')
                    self.bird_widget.update()

        # Rotating bird
        try:
            angle = float(self.edit_angle.text())
        except Exception:
            self.edit_angle.setText('0')
            self.edit_x_center_spin.setText('0')
            self.edit_y_center_spin.setText('0')
        else:
            try:
                x_rotate = float(self.edit_x_center_spin.text())
                y_rotate = float(self.edit_y_center_spin.text())
            except Exception:
                x_rotate = 0
                y_rotate = 0
                rotate_point = QPointF(x_rotate, y_rotate)
                self.bird_widget.angleAll(rotate_point, angle)
                self.edit_angle.setText('0')
                self.edit_x_center_spin.setText('0')
                self.edit_y_center_spin.setText('0')
                self.bird_widget.update()
            else:
                rotate_point = QPointF(x_rotate, y_rotate)
                self.bird_widget.angleAll(rotate_point, angle)
                self.edit_angle.setText('0')
                self.edit_x_center_spin.setText('0')
                self.edit_y_center_spin.setText('0')
                self.bird_widget.update()



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