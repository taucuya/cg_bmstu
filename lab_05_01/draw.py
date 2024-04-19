from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtWidgets import  QGraphicsScene
from PyQt6.QtGui import QPen, QColor, QPainter

def draw_edges(image, pointArray, color):
    p = QPainter()
    p.begin(image)
    p.setPen(QPen(color))
    for i in range(len(pointArray) - 1):
        p.drawLine(pointArray[i].x(), pointArray[i].y(), pointArray[i + 1].x(), pointArray[i + 1].y())
    p.end()