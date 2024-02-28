import unittest
from funcs import *

class TestPrintAngleFunction(unittest.TestCase):

    def test_print_angle_case1(self):
        result = printAngle((0, 0), (1, 1), (2, 0))
        self.assertAlmostEqual(result[0], 45.0, places=6)
        self.assertAlmostEqual(result[1], 90.0, places=6)
        self.assertAlmostEqual(result[2], 45.0, places=6)

    def test_print_angle_case2(self):
        result = printAngle((0, 0), (4, 0), (2, 3))
        self.assertAlmostEqual(round(result[0], 2), 56.31, places=6)
        self.assertAlmostEqual(round(result[1], 2), 56.31, places=6)
        self.assertAlmostEqual(round(result[2], 2), 67.38, places=6)

    def test_print_angle_case3(self):
        result = printAngle((-1, -1), (1, -1), (0, 1))
        self.assertAlmostEqual(round(result[0], 3), 63.435, places=6)
        self.assertAlmostEqual(round(result[1], 3), 63.435, places=6)
        self.assertAlmostEqual(round(result[2], 2), 53.13, places=6)


class TestBisectorSideFunction(unittest.TestCase):

    def test_bisector_side_case1(self):
        result = bisector_side(0, 0, 1, 1, 2, 0)
        result = list(result)
        for i in range(len(result)):
            result[i] = round(result[i], 3)
        self.assertEqual(result, [1.414, 0.586, 1.0, 0.0, 0.586, 0.586])

    def test_bisector_side_case2(self):
        result = bisector_side(0, 0, 4, 0, 2, 3)
        result = list(result)
        for i in range(len(result)):
            result[i] = round(result[i], 3)
        self.assertEqual(result, [2.948, 1.578, 1.052, 1.578, 2.0, 0.0])

    def test_bisector_side_case3(self):
        result = bisector_side(-1, -1, 1, -1, 0, 1)
        result = list(result)
        for i in range(len(result)):
            result[i] = round(result[i], 3)
        self.assertEqual(result, [0.528, -0.056, -0.528, -0.056, 0.0, -1.0])


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