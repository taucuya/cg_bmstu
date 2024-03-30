from calc import sign 
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor

def brozenhemNoGrad(point_start: QPointF, point_end: QPointF, color: QColor):
    pointsArray =  []
    I = 100
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

        tg = dy / dx * I
        e = I / 2
        w = I - tg
        x = point_start.x()
        y = point_start.y()

        while x != point_end.x() or y != point_end.y():
            pointsArray.append([QPointF(x, y), color.lighter(round(e))])
            if e < w:
                if flag == 0:
                    x += sx
                else: 
                    y += sy
                e += tg
            elif e >= w:
                x += sx
                y += sy
                e -= w
    return pointsArray