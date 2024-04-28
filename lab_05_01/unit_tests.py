import pytest
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPoint
from points import makeMid


def test_makeMid():
    pointArray = [QPoint(1, 1), QPoint(2, 4), QPoint(3, 2), QPoint(4, 5)]
    expected_result = [QPoint(2, 5), QPoint(2, 1)]
    assert makeMid(pointArray) == expected_result

    pointArray = [QPoint(1, 2), QPoint(3, 4), QPoint(5, 6)]
    expected_result = [QPoint(3, 6), QPoint(3, 2)]
    assert makeMid(pointArray) == expected_result

    pointArray = [QPoint(10, 10), QPoint(20, 20), QPoint(30, 30)]
    expected_result = [QPoint(20, 30), QPoint(20, 10)]
    assert makeMid(pointArray) == expected_result
