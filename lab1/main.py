from PyQt6 import QtCore, QtGui, QtWidgets
from funcs import *
from design import *

EPSILON = 1e-5
FLAG = 0

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
            msg.setText("Нельзя ввести больше 100 точек.")
            msg.exec()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            # Получаем позицию мыши в координатах графика
            pos = self.plot_widget.plotItem.vb.mapSceneToView(event.scenePos())
            # Получаем x и y координаты
            x = pos.x()
            y = pos.y()
            # Добавляем точку с координатами x и y в scatter
            self.scatter.addPoints([f"{x:.2f}"], [f"{y:.2f}"])
            mas.append([float(f"{x:.2f}"), float(f"{y:.2f}")])
            self.tableWidget.setItem(len(mas) - 1, 0, QtWidgets.QTableWidgetItem(str(mas[len(mas) - 1][0])))
            self.tableWidget.setItem(len(mas) - 1, 1, QtWidgets.QTableWidgetItem(str(mas[len(mas) - 1][1])))

    def show_message_box_author(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Об авторе')
        msg.setText("Шатохина Таисия Павловна ИУ7-41Б")
        msg.exec()

    def show_message_box_prog(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('О программе')
        msg.setText("Программа решает задачу поиска треугольника, у которого угол"
                    " между биссектросой и высотой, выходящих из одной вершины максимален. Точки, задаваемые"
                    " на поле и в таблице, автоматически округляются до 2 знаков после запятой. Поэтому"
                    " попытки задать большую точность будут приводить к округлению.")
        msg.exec()

    def addDot(self):
        global FLAG
        if FLAG == 1:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
            FLAG = 0
        if len(mas) > 100:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText("Нельзя ввести больше 100 точек.")
            msg.exec()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            try:
                x = float(self.lineEdit.text())
                y = float(self.lineEdit_2.text())
            except Exception:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText("Неправильно введены координаты.")
                msg.exec()
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
            else:
                if ([x, y] in mas):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText("Такая точка уже есть.")
                    msg.exec()
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                else:
                    mas.append([x, y])
                    self.scatter.addPoints([str(x)], [str(y)])
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.tableWidget.setItem(len(mas) - 1, 0, QtWidgets.QTableWidgetItem(f"{mas[-1][0]:.2f}"))
                    self.tableWidget.setItem(len(mas) - 1, 1, QtWidgets.QTableWidgetItem(f"{mas[-1][1]:.2f}"))
    def delDot(self):
        try:
            x = float(self.lineEdit.text())
            y = float(self.lineEdit_2.text())
        except Exception:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText("Неправильно введены координаты.")
            msg.exec()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            ind = -100
            for j in range(len(mas) - 1):
                print(self.tableWidget, self.tableWidget.item(j, 1))
                if self.tableWidget.item(j, 0) == x and self.tableWidget.item(j, 0) == y:
                    ind = j
            print(ind)
            for i in range(ind, len(mas) - 1):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{mas[i + 1][0]:.2f}"))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(f"{mas[i + 1][1]:.2f}"))
            mas.pop(ind)
            self.tableWidget.setItem(len(mas), 0, QtWidgets.QTableWidgetItem(''))
            self.tableWidget.setItem(len(mas), 1, QtWidgets.QTableWidgetItem(''))
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.scatter.clear()
            for i in mas:
                self.scatter.addPoints([str(i[0])], [str(i[1])])
            if ind == -100:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText("Такой точки нет.")
                msg.exec()
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')

    def delAll(self):
        for i in range(len(mas)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(''))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(''))
        del mas[:]
        self.scatter.setData()
        self.plot_widget.removeItem(self.tr)
        self.plot_widget.removeItem(self.bis)
        self.plot_widget.removeItem(self.height)

    def result(self):
        global FLAG
        if FLAG == 1:
            self.plot_widget.removeItem(self.tr)
            self.plot_widget.removeItem(self.bis)
            self.plot_widget.removeItem(self.height)
            FLAG = 0
        mx = 0
        mx_ = 0
        triangle = []
        mx_ind = 0
        if len(mas) < 3:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText("Недостаточно точек для решения задачи.")
            msg.exec()
        else:
            for i in range(len(mas) - 2):
                for j in range(i + 1, len(mas) - 1):
                    for k in range(j + 1, len(mas)):
                        if (mas[j][0] - mas[i][0]) * (mas[k][1] - mas[i][1]) - (mas[j][1] - mas[i][1]) * \
                                (mas[k][0] - mas[i][0]) != 0:
                            triangle.append([mas[i], mas[j], mas[k]])
        if len(triangle) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText("Невозможно создать треугольник.")
            msg.exec()
        else:
            res = [0, 0, 0]
            for i in range(len(triangle)):
                alpha, betta, gamma = printAngle(triangle[i][0], triangle[i][1], triangle[i][2])
                n_a, n_b, n_c = calculate_angles_between_bisectors_and_heights(alpha, betta, gamma)
                print()
                if mx < (n_a + EPSILON) or mx < (n_b + EPSILON) or mx < (n_c + EPSILON):
                    mx_ind = i
                    res[0] = n_a
                    res[1] = n_b
                    res[2] = n_c
                    mx = max(n_a, n_b, n_c)
                    mx_ = res.index(max(n_a, n_b, n_c))
            x_arr = []
            y_arr = []

            for i in triangle[mx_ind]:
                x_arr.append(i[0])
                y_arr.append(i[1])
            x_arr.append(triangle[mx_ind][0][0])
            y_arr.append(triangle[mx_ind][0][1])

            self.tr = self.plot_widget.plot(x_arr, y_arr, pen='b')

            A = (x_arr[0], y_arr[0])
            B = (x_arr[1], y_arr[1])
            C = (x_arr[2], y_arr[2])
            point1 = [0, 0]
            point2 = [0, 0]
            point3 = [0, 0]

            point1[0], point1[1], point2[0], point2[1], point3[0], point3[1] = bisector_side(A[0], A[1], B[0], B[1],
                                                                                             C[0], C[1])

            if mx_ == 2:
                xb = [C[0], point3[0]]
                yb = [C[1], point3[1]]
                x_h, y_h = altitude_side(A[0], A[1], B[0], B[1], C[0], C[1])
                xh = [C[0], x_h]
                yh = [C[1], y_h]

            elif mx_ == 0:
                xb = [A[0], point1[0]]
                yb = [A[1], point1[1]]
                x_h, y_h = altitude_side(B[0], B[1], C[0], C[1], A[0], A[1])
                xh = [A[0], x_h]
                yh = [A[1], y_h]

            elif mx_ == 1:
                xb = [B[0], point2[0]]
                yb = [B[1], point2[1]]
                x_h, y_h = altitude_side(C[0], C[1], A[0], A[1], B[0], B[1])
                xh = [B[0], x_h]
                yh = [B[1], y_h]
            self.bis = self.plot_widget.plot(xb, yb, pen='g')
            self.height = self.plot_widget.plot(xh, yh, pen='r')

            FLAG = 1


if __name__ == "__main__":
    import sys
    mas = []
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
