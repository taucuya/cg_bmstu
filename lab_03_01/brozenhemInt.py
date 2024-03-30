from calc import sign
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor

def brozenhemInt(point_start: QPointF, point_end: QPointF, color: QColor):
    pointsArray = []
    if point_start == point_end:
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

        e = 2 * dy - dx
        x = point_start.x()
        y = point_start.y()

        while x != point_end.x() or y != point_end.y():
            pointsArray.append([QPointF(x, y), color])
            if e >= 0:
                if flag == 1:
                    x += sx
                else: 
                    y += sy
                e -= 2 * dx
            if e <= 0:
                if flag == 0:
                    x += sx
                else: 
                    y += sy
                e += 2 * dy
    return pointsArray