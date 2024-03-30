from PyQt6.QtCore import QPointF
from math import floor
from PyQt6.QtGui import QColor

def vu(point_start: QPointF, point_end: QPointF, color: QColor):
    pointsArray = []
    I = 100
    if point_start == point_end:
        pointsArray.append([point_start, color])

    flag = 0

    if abs(point_end.y() - point_start.y()) > abs(point_end.x() - point_start.x()):
        point_start = QPointF(point_start.y(), point_start.x())
        point_end = QPointF(point_end.y(), point_end.x())
        flag = 1

    if point_start.x() > point_end.x():
        point_start, point_end = point_end, point_start

    dx = point_end.x() - point_start.x()
    dy = point_end.y() - point_start.y()

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    xend = round(point_start.x())
    yend = point_start.y() + tg * (xend - point_start.x())
    xpx1 = xend
    y = yend + tg

    xend = int(point_end.x() + 0.5)
    xpx2 = xend

    if flag:
        for x in range(xpx1, xpx2):
            try:
                pointsArray.append([QPointF(int(y), x + 1), color.lighter(int((I - 1) * (abs(1 - y + int(y)))))])
            except:
                pointsArray.append([QPointF(int(y), x + 1), color])
            pointsArray.append([QPointF(int(y) + 1, x + 1), color.lighter(int((I - 1) * (abs(y - int(y)))))])
            y += tg
    else:
        for x in range(xpx1, xpx2):
            pointsArray.append([QPointF(x + 1, int(y)), color.lighter(round((I - 1) * (abs(1 - y + floor(y)))))])
            pointsArray.append([QPointF(x + 1, int(y) + 1), color.lighter(round((I - 1) * (abs(1 - y + floor(y)))))])
            y += tg

    return pointsArray