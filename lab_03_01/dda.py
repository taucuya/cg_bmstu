from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor

def dda(point_start: QPointF, point_end: QPointF, color: QColor):
    pointArray = []
    if point_start == point_end:
        pointArray.append([QPointF(round(point_start.x()), round(point_start.y())), color])
    else:
        dx = abs(point_start.x() - point_end.x())
        dy = abs(point_start.y() - point_end.y())

        length = max(dx , dy)

        dx = (point_end.x() - point_start.x()) / length
        dy = (point_end.y() - point_start.y()) / length

        x = point_start.x()
        y = point_start.y()

        for i in range(int(length) + 1):
            x += dx
            y += dy
            pointArray.append([QPointF(round(x), round(y)), color])

    return pointArray