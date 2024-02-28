from PyQt6 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 706)
        self.setFixedSize(self.size())
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 222, 197);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.plot_widget = pg.PlotWidget(parent=self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(380, 40, 661, 571))
        self.scatter = pg.ScatterPlotItem()
        self.plot_widget.addItem(self.scatter)
        self.plot_widget.showGrid(x=True, y=True)
        self.button_add_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_add_dot.setGeometry(QtCore.QRect(10, 110, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_add_dot.setFont(font)
        self.button_add_dot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_add_dot.setObjectName("button_add_dot")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 220, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 341, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.setFont(font)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(15)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(146)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.label_list = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_list.setGeometry(QtCore.QRect(120, 230, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_list.setFont(font)
        self.label_list.setStyleSheet("")
        self.label_list.setObjectName("label_list")
        self.button_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(880, 630, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_clear.setObjectName("button_clear")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 250, 341, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_input_coord = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_input_coord.setGeometry(QtCore.QRect(10, 40, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_input_coord.setFont(font)
        self.label_input_coord.setObjectName("label_input_coord")
        self.label_x = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_x.setGeometry(QtCore.QRect(20, 80, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_y.setGeometry(QtCore.QRect(190, 80, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.button_del_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_del_dot.setGeometry(QtCore.QRect(10, 190, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_del_dot.setFont(font)
        self.button_del_dot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_del_dot.setObjectName("button_del_dot")
        self.button_res = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_res.setGeometry(QtCore.QRect(370, 630, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_res.setFont(font)
        self.button_res.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_res.setObjectName("button_res")
        self.button_author = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_author.setGeometry(QtCore.QRect(10, 10, 111, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_author.setFont(font)
        self.button_author.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.button_author.setAccessibleDescription("")
        self.button_author.setFlat(False)
        self.button_author.setObjectName("button_author")
        self.button_prog = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_prog.setGeometry(QtCore.QRect(130, 10, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_prog.setFont(font)
        self.button_prog.setObjectName("button_prog")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_num = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_num.setGeometry(QtCore.QRect(10, 150, 220, 31))
        self.label_num.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_num.setObjectName("label_5")
        self.lineEdit_coords = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_coords.setGeometry(QtCore.QRect(240, 150, 101, 31))
        self.lineEdit_coords.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "font: 75 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_coords.setObjectName("lineEdit_coords")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.plot_widget.raise_()
        self.button_add_dot.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        self.label_list.raise_()
        self.button_clear.raise_()
        self.line_3.raise_()
        self.label_input_coord.raise_()
        self.label_x.raise_()
        self.label_y.raise_()
        self.button_del_dot.raise_()
        self.button_res.raise_()
        self.button_author.raise_()
        self.button_prog.raise_()
        self.label_num.raise_()
        self.lineEdit_coords.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_add_dot.setText(_translate("MainWindow", "Поставить точку"))
        self.label_list.setText(_translate("MainWindow", "Список точек"))
        self.button_clear.setText(_translate("MainWindow", "Очистить поле"))
        self.label_input_coord.setText(_translate("MainWindow", "Введите координаты точки:"))
        self.label_x.setText(_translate("MainWindow", "X:"))
        self.label_y.setText(_translate("MainWindow", "Y:"))
        self.button_del_dot.setText(_translate("MainWindow", "Удалить точку"))
        self.button_res.setText(_translate("MainWindow", "Решить задачу"))
        self.button_author.setText(_translate("MainWindow", "Об авторе"))
        self.button_prog.setText(_translate("MainWindow", "О программе"))
        self.label_num.setText(_translate("MainWindow", "Номер удаляемой точки:"))