from PyQt6.QtCore import QCoreApplication, QEventLoop
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QPen, QColor, QPixmap, QPainter

def filling(scene, color, pointArray, mid_x, flag, image):
    for i in range(len(pointArray) - 1):
        fillByEdges(scene, color, pointArray[i], pointArray[i + 1], mid_x, flag, image)
    fillByEdges(scene, color, pointArray[-1], pointArray[0], mid_x, flag, image)

def fillByEdges(scene, color, start, end, mid_x, flag, image):
        painter = QPainter()
        pixmap = QPixmap(int(scene.width()), int(scene.height()))
        pixmap.fill(QColor('white'))

        painter.begin(pixmap)
        scene.render(painter)
        painter.end()

        image = pixmap.toImage()
        if start.y() == end.y():
            return
        if start.y() > end.y():
            start, end = end, start

        dx = (end.x() - start.x()) / (end.y() - start.y())
        dy = 1

        x = start.x(); y = start.y()
        if flag == 0:
            fillWNSleep(scene, color, x, y, end, mid_x, dx, dy, image)
        else:
            fillWSleep(scene, color, x, y, end, mid_x, dx, dy, image)

def fillWNSleep(scene, color, x, y, end, mid_x, dx, dy, image):
    while y < end.y():
        if x < mid_x:
            for j in range(round(x) + 1, mid_x):
                revColor(scene, j, round(y), color, image)
        elif x >= mid_x:
            for j in range(mid_x, round(x) + 1):
                revColor(scene, j, round(y), color, image)
        x += dx; y += dy

def fillWSleep(scene, color, x, y, end, mid_x, dx, dy, image):
    while y < end.y():
        if x < mid_x:
            for j in range(round(x) + 1, mid_x):
                revColor(scene, j, round(y), color, image)
        elif x >= mid_x:
            for j in range(mid_x, round(x) + 1):
                revColor(scene, j, round(y), color, image)
        x += dx; y += dy
        QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.AllEvents)

def revColor(scene, x, y, color, image):
    pixel_color = QColor(image.pixelColor(x, y).name())
    pen = QPen()
    if pixel_color == color:
        pen.setColor(QColor('white'))
    elif pixel_color == QColor('white'):
        pen.setColor(color)
    scene.addLine(x, y, x, y, pen)
