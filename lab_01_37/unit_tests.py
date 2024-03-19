import pytest
from PyQt6 import QtGui, QtCore
from calc import *


def test_print_angle_case1():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(0, 0), QtCore.QPointF(1, 1), QtCore.QPointF(2, 0)])
    result = get_triangle_angles(triangle)
    assert result[0] == pytest.approx(45.0, abs=1e-5)
    assert result[1] == pytest.approx(90.0, abs=1e-5)
    assert result[2] == pytest.approx(45.0, abs=1e-5)


def test_print_angle_case2():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(0, 0), QtCore.QPointF(4, 0), QtCore.QPointF(2, 3)])
    result = get_triangle_angles(triangle)
    assert round(result[0], 2) == pytest.approx(56.31, abs=1e-5)
    assert round(result[1], 2) == pytest.approx(56.31, abs=1e-5)
    assert round(result[2], 2) == pytest.approx(67.38, abs=1e-5)


def test_print_angle_case3():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(-1, -1), QtCore.QPointF(1, -1), QtCore.QPointF(0, 1)])
    result = get_triangle_angles(triangle)
    assert round(result[0], 3) == pytest.approx(63.435, abs=1e-5)
    assert round(result[1], 3) == pytest.approx(63.435, abs=1e-5)
    assert round(result[2], 2) == pytest.approx(53.13, abs=1e-5)


def test_bisector_side_case1():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(0, 0), QtCore.QPointF(1, 1), QtCore.QPointF(2, 0)])
    result = bisector_side(triangle)
    result = list(result)
    fin = []
    for i in range(len(result)):
        fin.append(round(result[i].x(), 3))
        fin.append(round(result[i].y(), 3))
    assert fin == [1.414, 0.586, 1.0, 0.0, 0.586, 0.586]


def test_bisector_side_case2():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(0, 0), QtCore.QPointF(4, 0), QtCore.QPointF(2, 3)])
    result = bisector_side(triangle)
    result = list(result)
    fin = []
    for i in range(len(result)):
        fin.append(round(result[i].x(), 3))
        fin.append(round(result[i].y(), 3))
    assert fin == [2.948, 1.578, 1.052, 1.578, 2.0, 0.0]


def test_bisector_side_case3():
    triangle = QtGui.QPolygonF(
        [QtCore.QPointF(-1, -1), QtCore.QPointF(1, -1), QtCore.QPointF(0, 1)])
    result = bisector_side(triangle)
    fin = []
    for i in range(len(result)):
        fin.append(round(result[i].x(), 3))
        fin.append(round(result[i].y(), 3))
    assert fin == [0.528, -0.056, -0.528, -0.056, 0.0, -1.0]


def test_is_triangle_not_degenerate():
    A = (0, 0)
    B = (4, 0)
    C = (2, 3)
    assert isTriangle(A, B, C)


def test_is_triangle_degenerate():
    A = (0, 0)
    B = (0, 0)
    C = (0, 0)
    assert not isTriangle(A, B, C)
