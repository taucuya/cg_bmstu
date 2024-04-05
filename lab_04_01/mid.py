from mirror import mirror, mirror_ellipse
from PyQt6.QtCore import QPointF

def mid_circle(center_point, radius):
    pointsArray = []
    x = radius
    y = 0

    pointsArray = mirror(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)
    delta = 1 - radius

    while x > y:
        y += 1
        if delta > 0:
            x -= 1
            delta -= 2 * x - 2
        delta += 2 * y + 3
        pointsArray = mirror(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

    return pointsArray


def mid_ellipse(center_point, axisX, axisY):
    pointsArray = []
    x = 0
    y = axisY

    delta = axisY ** 2 - axisX ** 2 * axisY + 0.25 * axisX * axisX
    dx = 2 * axisY ** 2 * x
    dy = 2 * axisX ** 2 * y

    while dx < dy:
        pointsArray = mirror_ellipse(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

        x += 1
        dx += 2 * axisY ** 2

        if delta >= 0:
            y -= 1
            dy -= 2 * axisX ** 2
            delta -= dy

        delta += dx + axisY ** 2

    delta = axisY ** 2 * (x + 0.5) ** 2 + axisX ** 2 * (y - 1) ** 2 - axisX ** 2 * axisY ** 2

    while y >= 0:
        pointsArray = mirror_ellipse(pointsArray, QPointF(x + center_point.x(), y + center_point.y()), center_point)

        y -= 1
        dy -= 2 * axisX**2

        if delta <= 0:
            x += 1
            dx += 2 * axisY**2
            delta += dx

        delta -= dy - axisX**2

    return pointsArray