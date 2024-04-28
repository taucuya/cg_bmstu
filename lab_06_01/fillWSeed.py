from PyQt6.QtGui import QColor, QPen, QPainter, QPixmap
from PyQt6.QtCore import QPoint, QCoreApplication, QEventLoop

def point_inside_polygon(p, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0].x(), polygon[0].y()
    for i in range(n + 1):
        p2x, p2y = polygon[i % n].x(), polygon[i % n].y()
        if p.y() > min(p1y, p2y):
            if p.y() <= max(p1y, p2y):
                if p.x() <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (p.y() - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or p.x() <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def scan(lx, rx, y, s, poly):
    fl = False
    x = lx
    while x < rx:
        if not point_inside_polygon(QPoint(x, y), poly):
            fl = False
        elif not fl:
            if QPoint(x, y) not in s:
                s.append(QPoint(x, y))
            fl = True
        x += 1
    return s

def drawPoint(scene, point, color):
    pen = QPen()
    pen.setColor(QColor(color))
    scene.addLine(point.x(), point.y(), point.x(), point.y(), pen)


def filling(scene, color, pointArray, flag, image, seed):
    
    if not point_inside_polygon(seed, pointArray):
        return 123

    pen = QPen()
    pen.setColor(QColor(color))

    stack = []
    stack.append(seed)

    arr = []

    while stack:
        p = stack.pop()
        x, y = p.x(), p.y()
        lx = x
        while point_inside_polygon(QPoint(lx - 1, y), pointArray) and QPoint(lx - 1, y) not in arr:
            drawPoint(scene, QPoint(lx - 1, y), color)
            arr.append(QPoint(lx - 1, y))
            lx -= 1
        while point_inside_polygon(QPoint(x, y), pointArray) and QPoint(x, y) not in arr:
            drawPoint(scene, QPoint(x, y), color)
            arr.append(QPoint(x, y))
            x += 1
        stack = scan(lx, x - 1, y + 1, stack, pointArray)
        stack = scan(lx, x - 1, y - 1, stack, pointArray)
        if flag:
            QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.AllEvents, 0)
   
        

    
