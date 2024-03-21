from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
import json
import time

from main import Window
import pytest

TestReps = 3


def read_json(file_name):
    with (open("funcs.json", "r")) as f:
        json_data = json.load(f)
    return json_data
    

@pytest.fixture
def window(qtbot):
    main_window = Window()
    qtbot.addWidget(main_window)

    return main_window


def tests(qtbot, window):
    with open("buf.txt", "w") as f:
        data = read_json("func.json")
        for test in data:
            clk = 0
            for i in range(TestReps):
                string = ''
                window.button_reset.click()
                QTest.keyClicks(window.edit_x_mov, data[test]["x_mov"])
                QTest.keyClicks(window.edit_y_mov, data[test]["y_mov"])
                QTest.keyClicks(window.edit_size, data[test]["size"])
                QTest.keyClicks(window.edit_x_center_size, data[test]["x_center_size"])
                QTest.keyClicks(window.edit_y_center_size, data[test]["y_center_size"])
                QTest.keyClicks(window.edit_angle, data[test]["angle"])
                QTest.keyClicks(window.edit_x_center_spin, data[test]["x_center_spin"])
                QTest.keyClicks(window.edit_y_center_spin, data[test]["y_center_spin"])
                start_time = time.time()
                window.button_transform.click()
                end_time = time.time()
                clk += end_time - start_time
            screenshot = window.Canvas_.grab()
            screenshot.save(f"./results/{test}.jpeg", format="JPEG")
            with open(f"./results/{test}.txt", "w") as desc:
                desc.write(data[test]["description"])

            string += test + ' ' + str(clk * 1000 / TestReps) + ' msec' + '\n'
            f.write(string)