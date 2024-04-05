from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import json
import time

from main import Window
import pytest

TestReps = 3

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
                window.clearButton.click()
                window.centerXField.setText('')
                window.centerYField.setText('')
                window.radiusField.setText('')
                window.axisXField.setText('')
                window.axisYField.setText('')
                window.amountField.setText('')
                window.stepField.setText('')
                QTest.keyClicks(window.centerXField, data[test]["x_center"])
                QTest.keyClicks(window.centerYField, data[test]["y_center"])
                window.figureTypeComboBox.setCurrentIndex(int(data[test]["type"]))
                QTest.keyClicks(window.radiusField, data[test]["radius"])
                QTest.keyClicks(window.axisXField, data[test]["axisX"])
                QTest.keyClicks(window.axisYField, data[test]["axisY"])
                window.algorithmComboBox.setCurrentIndex(int(data[test]["alg"]))
                window.colorComboBox.setCurrentIndex(int(data[test]["color"]))
                QTest.keyClicks(window.amountField, data[test]["amount"])
                QTest.keyClicks(window.stepField, data[test]["step"])
                start_time = time.time()
                if data[test]["button_type"] == "1":
                    window.figureDrawButton.click()
                elif data[test]["button_type"] == "0":
                    window.rangeDrawButton.click()
                end_time = time.time()
                clkLine += end_time - start_time
            screenshot = window.grab()
            screenshot.save(f"./results/{test}.jpeg", format="JPEG")
            with open(f"./results/{test}.txt", "w") as desc:
                desc.write(data[test]["description"])
            string += test + ' ' + str(clkLine * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)


