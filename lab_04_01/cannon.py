from PyQt6.QtCore import QPointF
from mirror import mirror, mirror_ellipse

def cannon_circle(center_point, radius):
    pointsArray = []

    border = round(center_point.x() + radius / (2 ** 0.5))

    for x in range(int(center_point.x()), border + 1):
        y = (radius ** 2 - (x - center_point.x()) **2 ) ** 0.5 + center_point.y()
        pointsArray = mirror(pointsArray, QPointF(x, y), center_point)
    return pointsArray

def cannon_ellipse(center_point, axisX, axisY):
    pointsArray = []
    sqr_ax = axisX ** 2
    sqr_ay = axisY ** 2

    border_x = round(center_point.x() + axisX / (1 + sqr_ay / sqr_ax) ** 0.5)
    border_y = round(center_point.y() + axisY / (1 + sqr_ax / sqr_ay) ** 0.5)

    for x in range(int(center_point.x()), border_x + 1):
        y = center_point.y() + (sqr_ax * sqr_ay - (x - center_point.x()) ** 2 * sqr_ay) ** 0.5 / axisX
        pointsArray = mirror_ellipse(pointsArray, QPointF(x, y), center_point)

    for y in range(border_y, int(center_point.y() - 1), -1):
        x = center_point.x() + (sqr_ax * sqr_ay - (y - center_point.y()) ** 2 * sqr_ax) ** 0.5 / axisY
        pointsArray = mirror_ellipse(pointsArray, QPointF(x, y), center_point)
    return pointsArray