from PyQt6.QtCore import QPointF
from math import pi, sin, cos
from mirror import mirror, mirror_ellipse

def param_circle(center_point, radius):
    pointsArray = []
    step = 1 / radius

    i = 0
    loop = pi / 4 + step
    while i <= loop:
        x = center_point.x() + round(radius * cos(i))
        y = center_point.y() + round(radius * sin(i))
        pointsArray = mirror(pointsArray, QPointF(x, y), center_point)
        i += step

    return pointsArray

def param_ellipse(center_point, axisX, axisY):
    pointsArray = []
    if axisX > axisY:
        step = 1 / axisX
    else:
        step = 1 / axisY

    i = 0
    while i <= pi / 2 + step:
        x = center_point.x() + round(axisX * cos(i))
        y = center_point.y() + round(axisY * sin(i))

        pointsArray = mirror_ellipse(pointsArray, QPointF(x, y), center_point)

        i += step
    return pointsArray
