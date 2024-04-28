import pytest
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPoint
from fillWSeed import point_inside_polygon


def test_1():

    expected = True
    polygon = [QPoint(200, 200), QPoint(200, 50), QPoint(50, 50)]
    result = point_inside_polygon(QPoint(100, 80), polygon)
    assert result == expected