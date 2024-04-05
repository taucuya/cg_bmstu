from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPen, QColor

def draw_simple(scene: QGraphicsScene, pointsArray: list, color: QColor):
    pen = QPen()
    for p in pointsArray:
        pen.setColor(color)
        scene.addEllipse(p.x(), p.y(), 1, 1, pen)

def draw_standart(scene: QGraphicsScene, center_point: QPointF, axisX: float, axisY: float, color: QColor):
    pen = QPen()
    pen.setColor(color)
    pen.setWidth(2)
    scene.addEllipse(0, 0, 1, 1, pen)
    scene.addEllipse(center_point.x() - axisX, center_point.y() - axisY, axisX * 2, axisY * 2, pen)

def draw_standart_specter(scene: QGraphicsScene, center_point: QPointF, axisX: float, axisY: float, color: QColor, amount: int, step: float):
    pen = QPen()
    pen.setColor(color)
    scene.addEllipse(0, 0, 1, 1, pen)
    for _ in range(amount):
        draw_standart(scene, center_point, axisX, axisY, color)
        axisX += step
        axisY += step

    
def draw_circle_specter(scene, alg, center_point, radius, amount, step, color):
    pen = QPen()
    pen.setColor(color)
    scene.addEllipse(0, 0, 1, 1, pen)
    for _ in range(amount):
        draw_simple(scene, alg(center_point, radius), color)
        radius += step

def draw_ellipse_specter(scene, alg, center_point, axisX, axisY, amount, step, color):
    pen = QPen()
    pen.setColor(color)
    scene.addEllipse(0, 0, 1, 1, pen)
    for _ in range(amount):
        draw_simple(scene, alg(center_point, axisX, axisY), color)
        axisX += step
        axisY += step