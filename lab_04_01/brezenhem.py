from mirror import mirror, mirror_ellipse 
from PyQt6.QtCore import QPointF

def brezenhem_circle(center_point, radius):
    pointsArray = []
    x = 0
    y = radius
    delta = 2 * (1 - radius)

    pointsArray = mirror(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

    while x < y:
        if delta <= 0:
            delta_temp = 2 * (delta + y) - 1
            x += 1
            if delta_temp >= 0:
                delta += 2 * (x - y + 1)
                y -= 1
            else:
                delta += 2 * x + 1

        else:
            delta_temp = 2 * (delta - x) - 1
            y -= 1
            if delta_temp < 0:
                delta += 2 * (x - y + 1)
                x += 1
            else:
                delta -= 2 * y - 1

        pointsArray = mirror(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

    return pointsArray

def brezenhem_ellipse(center_point, axisX, axisY):
    pointsArray = []
    x = 0
    y = axisY
    delta = axisY**2 - axisX**2 * (2 * axisY + 1)

    pointsArray = mirror_ellipse(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

    while y > 0:
        if delta <= 0:
            delta_temp = 2 * delta + axisX ** 2 * (2 * y - 1)
            x += 1
            delta += axisY ** 2 * (2 * x + 1)
            if delta_temp >= 0:
                y -= 1
                delta += axisX ** 2 * (-2 * y + 1)

        else:
            delta_temp = 2 * delta + axisY ** 2 * (-2 * x - 1)
            y -= 1
            delta += axisX ** 2 * (-2 * y + 1)
            if delta_temp < 0:
                x += 1
                delta += axisY ** 2 * (2 * x + 1)

        pointsArray = mirror_ellipse(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

    return pointsArray