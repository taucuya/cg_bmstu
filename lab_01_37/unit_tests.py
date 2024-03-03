import unittest
from PyQt6 import QtGui, QtCore
from calc import *

class TestPrintAngleFunction(unittest.TestCase):

    def test_print_angle_case1(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(0, 0), QtCore.QPointF(1, 1), QtCore.QPointF(2, 0)])
        result = get_triangle_angles(triangle)
        self.assertAlmostEqual(result[0], 45.0, places=5)
        self.assertAlmostEqual(result[1], 90.0, places=5)
        self.assertAlmostEqual(result[2], 45.0, places=5)

    def test_print_angle_case2(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(0, 0), QtCore.QPointF(4, 0), QtCore.QPointF(2, 3)])
        result = get_triangle_angles(triangle)
        self.assertAlmostEqual(round(result[0], 2), 56.31, places=5)
        self.assertAlmostEqual(round(result[1], 2), 56.31, places=5)
        self.assertAlmostEqual(round(result[2], 2), 67.38, places=5)

    def test_print_angle_case3(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(-1, -1), QtCore.QPointF(1, -1), QtCore.QPointF(0, 1)])
        result = get_triangle_angles(triangle)
        self.assertAlmostEqual(round(result[0], 3), 63.435, places=5)
        self.assertAlmostEqual(round(result[1], 3), 63.435, places=5)
        self.assertAlmostEqual(round(result[2], 2), 53.13, places=5)


class TestBisectorSideFunction(unittest.TestCase):

    def test_bisector_side_case1(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(0, 0), QtCore.QPointF(1, 1), QtCore.QPointF(2, 0)])
        result = bisector_side(triangle)
        result = list(result)
        fin = []
        for i in range(len(result)):
            fin.append(round(result[i].x(), 3))
            fin.append(round(result[i].y(), 3))
        self.assertEqual(fin, [1.414, 0.586, 1.0, 0.0, 0.586, 0.586])

    def test_bisector_side_case2(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(0, 0), QtCore.QPointF(4, 0), QtCore.QPointF(2, 3)])
        result = bisector_side(triangle)
        result = list(result)
        fin = []
        for i in range(len(result)):
            fin.append(round(result[i].x(), 3))
            fin.append(round(result[i].y(), 3))
        self.assertEqual(fin, [2.948, 1.578, 1.052, 1.578, 2.0, 0.0])

    def test_bisector_side_case3(self):
        triangle = QtGui.QPolygonF([QtCore.QPointF(-1, -1), QtCore.QPointF(1, -1), QtCore.QPointF(0, 1)])
        result = bisector_side(triangle)
        fin = []
        for i in range(len(result)):
            fin.append(round(result[i].x(), 3))
            fin.append(round(result[i].y(), 3))
        self.assertEqual(fin, [0.528, -0.056, -0.528, -0.056, 0.0, -1.0])


class TestIsTriangle(unittest.TestCase):

    def test_not_degenerate_triangle(self):
        A = (0, 0)
        B = (4, 0)
        C = (2, 3)
        self.assertTrue(isTriangle(A, B, C))

    def test_degenerate_triangle(self):
        A = (0, 0)
        B = (0, 0)
        C = (0, 0)
        self.assertFalse(isTriangle(A, B, C))


if __name__ == '__main__':
    unittest.main()