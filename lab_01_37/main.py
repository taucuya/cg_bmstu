from calc import *
from design import *

EPSILON = 1e-5
FLAG = 0


def show_msg(str):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()


# Функция принимает треугольник в координатах вершин и возвращает массивы для рисования биссектрисы, высоты для
# треугольника с наибольшим углом между высотой и биссектрисой, также возвращается массив для рисования самого
# этого треугольника
def get_arrays_for_drawing(triangle):
    x_arr = []
    y_arr = []
    mx_ind, mx_triangle = findMax(triangle)

    for i in mx_triangle:
        x_arr.append(i.x())
        y_arr.append(i.y())
    x_arr.append(mx_triangle[0].x())
    y_arr.append(mx_triangle[0].y())

    a, b, c = bisector_side(mx_triangle)
    xb, yb, xh, yh = formBisHeight(mx_ind, mx_triangle, a, b, c)

    return x_arr, y_arr, xb, yb, xh, yh

# Функция принимает точку пересечения биссектрисы и стороны и точки вершин треугольников и возвращает массивы
# для отрисовки для данного случая


def get_arrays(a, A, B, C):
    xb = [A.x(), a.x()]
    yb = [A.y(), a.y()]
    h = height_side_intersection(B, C, A)
    xh = [A.x(), h.x()]
    yh = [A.y(), h.y()]
    return xb, yb, xh, yh

# Функция принимает индекс максимального угла, трегольник в вершинах и 3 вектора для биссектрис и возвращает массивы
# для построения высоты и биссектрисы


def formBisHeight(mx_ind, triangle, a, b, c):
    if mx_ind == 2:
        xb, yb, xh, yh = get_arrays(c, triangle[2], triangle[0], triangle[1])
    elif mx_ind == 0:
        xb, yb, xh, yh = get_arrays(a, triangle[0], triangle[1], triangle[2])
    elif mx_ind == 1:
        xb, yb, xh, yh = get_arrays(b, triangle[1], triangle[2], triangle[0])

    return xb, yb, xh, yh


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.button_author.clicked.connect(self.show_message_box_author)
        self.button_prog.clicked.connect(self.show_message_box_prog)
        self.button_add_dot.clicked.connect(self.addDot)
        self.button_del_dot.clicked.connect(self.delDot)
        self.button_clear.clicked.connect(self.delAll)
        self.button_res.clicked.connect(self.result)
        self.plot_widget.scene().sigMouseClicked.connect(self.on_mouse_press)

    def on_mouse_press(self, event):
        global FLAG
        if FLAG == 1:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
            FLAG = 0
        if len(mas) > 100:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Нельзя ввести больше 100 точек.')
            msg.exec()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            pos = self.plot_widget.plotItem.vb.mapSceneToView(event.scenePos())
            x = pos.x()
            y = pos.y()
            self.scatter.addPoints([f'{x}'], [f'{y}'])
            mas.append([x, y])
            self.tableWidget.setItem(
                len(mas) - 1, 0, QtWidgets.QTableWidgetItem(f'{mas[-1][0]:.2f}'))
            self.tableWidget.setItem(
                len(mas) - 1, 1, QtWidgets.QTableWidgetItem(f'{mas[-1][1]:.2f}'))

    def show_message_box_author(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Об авторе')
        msg.setText('Шатохина Таисия Павловна ИУ7-41Б')
        msg.exec()

    def show_message_box_prog(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('О программе')
        msg.setText('Программа решает задачу поиска треугольника, у которого угол'
                    ' между биссектросой и высотой, выходящих из одной вершины максимален.')
        msg.exec()

    def addDot(self):
        global FLAG
        if FLAG == 1:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
            FLAG = 0
        if len(mas) > 100:
            show_msg('Нельзя ввести больше 100 точек.')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            try:
                x = float(self.lineEdit.text())
                y = float(self.lineEdit_2.text())
            except Exception:
                show_msg('Неправильно введены координаты.')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
            else:
                if ([x, y] in mas):
                    show_msg('Такая точка уже есть.')
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                else:
                    mas.append([x, y])
                    self.scatter.addPoints([str(x)], [str(y)])
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.tableWidget.setItem(
                        len(mas) - 1, 0, QtWidgets.QTableWidgetItem(f'{mas[-1][0]:.2f}'))
                    self.tableWidget.setItem(
                        len(mas) - 1, 1, QtWidgets.QTableWidgetItem(f'{mas[-1][1]:.2f}'))

    def delDot(self):
        try:
            ind = int(self.lineEdit_coords.text())
        except Exception:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Неправильно введен номер точки из таблицы.')
            msg.exec()
            self.lineEdit_coords.setText('')
        else:
            if ind < 1 or ind > len(mas):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Неправильно введен номер точки из таблицы.')
                msg.exec()
                self.lineEdit_coords.setText('')
            else:
                for i in range(ind - 1, len(mas) - 1):
                    self.tableWidget.setItem(
                        i, 0, QtWidgets.QTableWidgetItem(f'{mas[i + 1][0]:.2f}'))
                    self.tableWidget.setItem(
                        i, 1, QtWidgets.QTableWidgetItem(f'{mas[i + 1][1]:.2f}'))
                mas.pop(ind - 1)
                self.tableWidget.setItem(
                    len(mas), 0, QtWidgets.QTableWidgetItem(''))
                self.tableWidget.setItem(
                    len(mas), 1, QtWidgets.QTableWidgetItem(''))
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.scatter.clear()
                for i in mas:
                    self.scatter.addPoints([str(i[0])], [str(i[1])])
                self.lineEdit_coords.setText('')

    def delAll(self):
        global FLAG
        for i in range(len(mas)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(''))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(''))
        del mas[:]
        self.scatter.setData()
        if FLAG:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
        FLAG = 0

    def result(self):
        global FLAG
        triangle = []
        if FLAG == 1:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
            FLAG = 0
        if len(mas) < 3:
            show_msg('Недостаточно точек для решения задачи.')
        else:
            triangle = find_triangles(mas)
        if len(triangle) == 0:
            show_msg('Невозможно создать треугольник.')
        else:
            x_arr, y_arr, xb, yb, xh, yh = get_arrays_for_drawing(triangle)
            self.tr = self.plot_widget.plot(x_arr, y_arr, pen='b')
            self.bis = self.plot_widget.plot(xb, yb, pen='g')
            self.height = self.plot_widget.plot(xh, yh, pen='r')

            FLAG = 1


if __name__ == '__main__':
    import sys
    mas = []
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
