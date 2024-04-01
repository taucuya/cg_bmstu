from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPen, QColor
from calc import radians, cos, sin

def draw_line(scene: QGraphicsScene, pointsArray: list):
    pen = QPen()
    for p, c in pointsArray:
        pen.setColor(c)
        scene.addEllipse(p.x(), p.y(), 1, 1, pen)

def draw_standart(scene: QGraphicsScene, point_start: QPointF, point_end: QPointF, color: QColor):
    pen = QPen()
    pen.setColor(color)
    scene.addLine(point_start.x(), point_start.y(), point_end.x(), point_end.y(), pen)

def draw_specter(scene: QGraphicsScene, method, point_start: QPointF, point_end: QPointF, length: float, angle: float, color: QColor):
    for i in range(0, 361, int(angle)):
        pointsArray = method(point_start, point_end, color)
        draw_line(scene, pointsArray)
        point_end = QPointF(round(cos(radians(i)) * length), round(sin(radians(i)) * length))


def draw_standart_specter(scene: QGraphicsScene, point_start: QPointF, point_end: QPointF, length: float, angle: float, color: QColor):
    for i in range(0, 361, int(angle)):
        draw_standart(scene, point_start, point_end, color)
        point_end = QPointF(round(cos(radians(i)) * length), round(sin(radians(i)) * length))