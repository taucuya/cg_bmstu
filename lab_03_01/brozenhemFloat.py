from calc import sign
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPointF

def brozenhemFloat(point_start: QPointF, point_end: QPointF, color: QColor):
    pointsArray = []
    if (point_start == point_end):
        pointsArray.append([point_start, color])

    else:
        dx = point_end.x() - point_start.x()
        dy = point_end.y() - point_start.y()

        sx = sign(dx)
        sy = sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        if (dy > dx):
            dx, dy = dy, dx
            flag = 1
        else: 
            flag = 0

        tg = dy / dx
        e = tg - 0.5
        x = point_start.x()
        y = point_start.y()

        while x != point_end.x() or y != point_end.y():
            pointsArray.append([QPointF(x, y), color])
            if e >= 0:
                if flag == 1:
                    x += sx
                else: 
                    y += sy
                e -= 1
            if e <= 0:
                if flag == 0:
                    x += sx
                else: 
                    y += sy
                e += tg

    return pointsArray