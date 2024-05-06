from PyQt6.QtTest import QTest
from PyQt6.QtCore import QPoint, QPointF, QRectF
from PyQt6.QtGui import QPen, QColor
import json
import time

from main import Window
import pytest

colors = dict([(0, "#ff0000"), (1, "#00ff00"), \
              (2, "#0000ff"), (3, "#ffb700"), (4, "#000000")])

def drawSegments(points, window, pen):
    i = 0
    while i < len(points) - 1:
        window.drawLine(points[i], points[i + 1], pen)
        i += 2

def drawRect(points, window, pen):
    window.scene.addRect(QRectF(QPointF(points[0].x(), points[0].y()), QPointF(points[1].x(), points[1].y())), pen)

def drawPolygon(points, window, pen):
    i = 0
    while i < len(points) - 1:
        window.drawLine(points[i], points[i + 1], pen)
        i += 1
    window.drawLine(points[0], points[-1], pen)

TestReps = 1

def read_json(file_name):
    with open(file_name, "r") as f:
        json_data = json.load(f)
    return json_data
    

@pytest.fixture
def window(qtbot):
    main_window = Window()
    qtbot.addWidget(main_window)

    return main_window


def tests(qtbot, window):
    with open("buf.txt", "w") as f:
        data = read_json("funcs.json")
        for test in data:
            clkLine = 0
            string = ''
            for i in range(TestReps):
                window.clear()
                newCutter = []
                newCutting = []
                for j in data[test]["cutter"]:
                    newCutter.append(QPoint(j[0], j[1]))
                for j in data[test]["cutting"]:
                    newCutting.append(QPoint(j[0], j[1]))

                window.colorCutterComboBox.setCurrentIndex(int(data[test]["color_cutter"]))
                window.colorCuttingComboBox.setCurrentIndex(int(data[test]["color_cutting"]))

                window.cutterComboBox.setCurrentIndex(int(data[test]["type_cutter"]))
                window.cuttingComboBox.setCurrentIndex(int(data[test]["type_cutting"]))
                
                window.pointCutterArray = newCutter
                window.pointCuttingArray = newCutting

                type1 = int(data[test]["type_cutting"])
                type2 = int(data[test]["type_cutter"])

                pen1 = QPen()
                pen1.setColor(QColor(colors[int(data[test]["color_cutter"])]))

                pen2 = QPen()
                pen2.setColor(QColor(colors[int(data[test]["color_cutting"])]))

                if type1 == 0 and type2 == 0:
                    drawRect(newCutter, window, pen1)
                    drawSegments(newCutting, window, pen2)

                elif type1 == 0 and type2 == 1:
                    drawPolygon(newCutter, window, pen1)
                    drawSegments(newCutting, window, pen2)

                elif type1 == 1 and type2 == 1:
                    drawPolygon(newCutter, window, pen1)
                    drawPolygon(newCutting, window, pen2)

                start_time = time.time()
                window.solve.click()
                end_time = time.time()
                clkLine += end_time - start_time
            screenshot = window.grab()
            screenshot.save(f"./results/{test}.jpeg", format="JPEG")
            with open(f"./results/{test}.txt", "w") as desc:
                desc.write(data[test]["description"])
            string += test + ' ' + str(clkLine * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)


