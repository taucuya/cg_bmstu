from PyQt5.QtTest import QTest
from PyQt5.QtCore import QPoint, QPointF, QRectF
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QApplication
import time
import json
from main import Window
import pytest
import sys
TestReps = 1

def read_json(file_name):
    with open(file_name, "r") as f:
        json_data = json.load(f)
    return json_data


def tests():
    my_window = Window()
    with open("buf.txt", "w") as f:
        data = read_json("funcs.json")
        print(len(data))
        for test in data:
            clkLine = 0
            string = ''
            for i in range(TestReps):
                my_window.clear()

                my_window.start_x.setValue(data[test]["start_x"])
                my_window.end_x.setValue(data[test]["end_x"])
                my_window.step_x.setValue(data[test]["step_x"])

                my_window.start_z.setValue(data[test]["start_z"])
                my_window.end_z.setValue(data[test]["end_z"])
                my_window.step_z.setValue(data[test]["step_z"])

                my_window.funcComboBox.setCurrentIndex(int(data[test]["funcInd"]))
                my_window.colorComboBox.setCurrentIndex(int(data[test]["colorInd"]))

                start_time = time.time()
                my_window.draw_button.click()
                end_time = time.time()
                clkLine += end_time - start_time
                
            screenshot = my_window.grab()
            screenshot.save(f"./results/{test}.jpeg", format="JPEG")
            with open(f"./results/{test}.txt", "w") as desc:
                desc.write(data[test]["description"])
            string += test + ' ' + str(clkLine * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)

