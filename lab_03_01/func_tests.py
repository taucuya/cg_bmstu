from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import json
import time

from main import Window
import pytest

TestReps = 3


def read_json(file_name):
    with (open(file_name, "r")) as f:
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
                window.clearButton.click()
                QTest.keyClicks(window.startXField, data[test]["x1"])
                QTest.keyClicks(window.startYField, data[test]["y1"])
                QTest.keyClicks(window.endXField, data[test]["x2"])
                QTest.keyClicks(window.endYField, data[test]["y2"])
                start_time = time.time()
                window.lineDrawButton.click()
                end_time = time.time()
                clkLine += end_time - start_time
            screenshot = window.grab()
            screenshot.save(f"./results/{test}_line.jpeg", format="JPEG")
            with open(f"./results/{test}_line.txt", "w") as desc:
                desc.write(data[test]["description1"])
            string += test + ' line ' + str(clkLine * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)
            clkRange = 0
            string = ''
            for i in range(TestReps):
                window.clearButton.click()
                QTest.keyClicks(window.rangeLengthField, data[test]["length"])
                QTest.keyClicks(window.rangeAngleField, data[test]["angle"])
                start_time = time.time()
                window.rangeDrawButton.click()
                end_time = time.time()
                clkRange += end_time - start_time
            screenshot = window.grab()
            screenshot.save(f"./results/{test}_range.jpeg", format="JPEG")
            with open(f"./results/{test}_range.txt", "w") as desc:
                desc.write(data[test]["description2"])
            string += test + ' range ' + str(clkRange * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)
        QTest.keyClicks(window.startXField, '')
        QTest.keyClicks(window.startYField, '')
        QTest.keyClicks(window.endXField, '')
        QTest.keyClicks(window.endYField, '')
        QTest.keyClicks(window.rangeLengthField, '')
        QTest.keyClicks(window.rangeAngleField, '')