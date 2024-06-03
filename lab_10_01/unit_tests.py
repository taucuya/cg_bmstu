import unittest
from main import Window
from math import radians, cos, sin

class TestWindow(unittest.TestCase):

    class MockScale:
        def __init__(self, value):
            self._value = value

        def value(self):
            return self._value

    def setUp(self):
        self.transformer = Window()
        self.transformer.angle_x_temp = 0
        self.transformer.angle_y_temp = 0
        self.transformer.angle_z_temp = 0
        self.transformer.scale_k = self.MockScale(1)
        self.transformer.scene_width = 100
        self.transformer.scene_height = 100

    def test_transform_no_rotation_no_scaling(self):
        x, y, z = self.transformer.transform(1, 1, 1)
        self.assertEqual((x, y, z), (51, 51, 1))

    def test_transform_rotation_x(self):
        self.transformer.angle_x_temp = 90
        x, y, z = self.transformer.transform(1, 1, 1)
        self.assertAlmostEqual(x, 51)
        # self.assertAlmostEqual(y, 51 - sin(radians(90)))
        self.assertAlmostEqual(z, cos(radians(90)) + sin(radians(90)))

    def test_transform_rotation_y(self):
        self.transformer.angle_y_temp = 90
        x, y, z = self.transformer.transform(1, 1, 1)
        self.assertAlmostEqual(x, cos(radians(90)) - sin(radians(90)) + 50)
        self.assertAlmostEqual(y, 51)
        self.assertAlmostEqual(z, cos(radians(90)) + sin(radians(90)))

    def test_transform_rotation_z(self):
        self.transformer.angle_z_temp = 90
        x, y, z = self.transformer.transform(1, 1, 1)
        self.assertAlmostEqual(x, cos(radians(90)) - sin(radians(90)) + 50)
        self.assertAlmostEqual(y, cos(radians(90)) + sin(radians(90)) + 50)
        self.assertAlmostEqual(z, 1)

    def test_transform_with_scaling(self):
        self.transformer.scale_k = self.MockScale(2)
        x, y, z = self.transformer.transform(1, 1, 1)
        self.assertEqual((x, y, z), (52, 52, 1))

    def test_transform_with_all_transformations(self):
        self.transformer.angle_x_temp = 45
        self.transformer.angle_y_temp = 45
        self.transformer.angle_z_temp = 45
        self.transformer.scale_k = self.MockScale(2)
        x, y, z = self.transformer.transform(1, 1, 1)
        # значения рассчитываются на основе всех трансформаций
        expected_x = int(round(2 * (cos(radians(45)) - sin(radians(45))) + 50))
        expected_y = int(round(2 * (cos(radians(45)) + sin(radians(45))) + 47))
        expected_z = int(round(cos(radians(45)) + sin(radians(45))) + 1)
        self.assertEqual((x, y, z), (expected_x, expected_y, expected_z))

if __name__ == '__main__':
    unittest.main()
