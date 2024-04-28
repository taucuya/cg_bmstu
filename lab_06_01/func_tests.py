from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt, QEvent, QCoreApplication, QPoint
import json
import time

from main import Window
import pytest

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
                for j in data[test]["points"]:
                    window.addPoint(QPoint(j[0], j[1]))
                window.colorComboBox.setCurrentIndex(int(data[test]["color_ind"]))
                window.seed = QPoint(data[test]["seed"][0], data[test]["seed"][1])
                start_time = time.time()
                window.paint.click()
                end_time = time.time()
                clkLine += end_time - start_time
            screenshot = window.grab()
            screenshot.save(f"./results/{test}.jpeg", format="JPEG")
            with open(f"./results/{test}.txt", "w") as desc:
                desc.write(data[test]["description"])
            string += test + ' ' + str(clkLine * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)


