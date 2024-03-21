import pytest
from PyQt6.QtCore import QPointF, Qt
from transformation import rotate_point


def test_rotate_point_90_degrees():
    expected = QPointF(0, 1)

    result = rotate_point(QPointF(1, 0), QPointF(0, 0), 90)

    assert result == expected


def test_rotate_point_180_degrees():
    expected = QPointF(-1, 0)

    result = rotate_point(QPointF(1, 0), QPointF(0, 0), 180)

    assert result == expected


def test_rotate_point_270_degrees():
    expected = QPointF(0, -1)

    result = rotate_point(QPointF(1, 0), QPointF(0, 0), 270)

    assert result == expected

def test_rotate_point_360_degrees():
    expected = QPointF(1, 0)

    result = rotate_point(QPointF(1, 0), QPointF(0, 0), 360)
    assert result == expected