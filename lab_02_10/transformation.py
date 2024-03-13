from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QMessageBox
from PyQt6.QtGui import QPainterPath, QPainter, QColor, QPen, QTransform, QPolygonF, QVector2D
from PyQt6.QtCore import QPointF, QRectF
from math import cos, sin, radians, pi

class BirdWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.scale_x = 1.0
        self.scale_y = 1.0
        self.angle = 0
        self.body = [QPointF(0, 0), QPointF(0, 40), QPointF(-60, 0)]
        self.head = [QPointF(-60, 40), QPointF(-60, 60), QPointF(-80, 40)]
        self.nose = [QPointF(-70, 45), QPointF(-100, 35), QPointF(-70, 35), QPointF(-70, 45)]
        self.wing = [QPointF(10, -10), QPointF(-10, -10), QPointF(20, -50), QPointF(10, -10)]
        self.tail = [QPointF(50, 5), QPointF(90, 5), QPointF(50, -5), QPointF(50, 5)]
        self.left_leg = [QPointF(-10, -40), QPointF(-20, -65)]
        self.right_leg = [QPointF(10, -40), QPointF(20, -65)]


    def moveToPoint(self, point: QPointF) -> None:
        self.body = plusPoint(self.body, point)
        self.head = plusPoint(self.head, point)
        self.nose = plusPoint(self.nose, point)
        self.wing = plusPoint(self.wing, point)
        self.tail = plusPoint(self.tail, point)
        self.left_leg = plusPoint(self.left_leg, point)
        self.right_leg = plusPoint(self.right_leg, point)
        self.update()

    def scaleAll(self, point: QPointF, x: float, y: float) -> None:
        self.body = scalePoint(self.body, point, x, y)
        self.head = scalePoint(self.head, point, x, y)
        self.nose = scalePoint(self.nose, point, x, y)
        self.wing = scalePoint(self.wing, point, x, y)
        self.tail = scalePoint(self.tail, point, x, y)
        self.left_leg = scalePoint(self.left_leg, point, x, y)
        self.right_leg = scalePoint(self.right_leg, point, x, y)
        self.update()

    def angleAll(self, point: QPointF, angle: float) -> None:
        self.angle += angle
        self.body = updateAnglePoint(self.body, point, angle)
        self.head = updateAnglePoint(self.head, point, angle)
        self.nose = updateAnglePoint(self.nose, point, angle)
        self.wing = updateAnglePoint(self.wing, point, angle)
        self.tail = updateAnglePoint(self.tail, point, angle)
        self.left_leg = updateAnglePoint(self.left_leg, point, angle)
        self.right_leg = updateAnglePoint(self.right_leg, point, angle)
        self.update()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        body_path = QPainterPath()
        points = find_ellipse_points(self.body, self.angle)
        body_path.moveTo(points[0])
        for point in points[1:]:
            body_path.lineTo(point)

        head_path = QPainterPath()
        points = find_ellipse_points(self.head, self.angle)
        head_path.moveTo(points[0])
        for point in points[1:]:
            head_path.lineTo(point)

        nose_path = QPainterPath()
        nose_path.addPolygon(QPolygonF(self.nose))

        wing_path = QPainterPath()
        wing_path.addPolygon(QPolygonF(self.wing))

        tail_path = QPainterPath()
        tail_path.addPolygon(QPolygonF(self.tail))

        left_leg_path = QPainterPath()
        left_leg_path.addPolygon(QPolygonF(self.left_leg))

        right_leg_path = QPainterPath()
        right_leg_path.addPolygon(QPolygonF(self.right_leg))

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(QPen(QColor("black"), 2))
        painter.drawPath(body_path)
        painter.drawPath(head_path)
        painter.drawPath(nose_path)
        painter.drawPath(wing_path)
        painter.drawPath(tail_path)
        painter.drawPath(left_leg_path)
        painter.drawPath(right_leg_path)


    def reset(self) -> None:
        self.scale_x = 1.0
        self.scale_y = 1.0
        self.angle = 0
        self.body = [QPointF(0, 0), QPointF(0, 40), QPointF(-60, 0)]
        self.head = [QPointF(-60, 40), QPointF(-60, 60), QPointF(-80, 40)]
        self.nose = [QPointF(-70, 45), QPointF(-100, 35), QPointF(-70, 35), QPointF(-70, 45)]
        self.wing = [QPointF(10, -10), QPointF(-10, -10), QPointF(20, -50), QPointF(10, -10)]
        self.tail = [QPointF(50, 5), QPointF(90, 5), QPointF(50, -5), QPointF(50, 5)]
        self.left_leg = [QPointF(-10, -40), QPointF(-20, -65)]
        self.right_leg = [QPointF(10, -40), QPointF(20, -65)]

def updateAnglePoint(part: list[QPointF], point: QPointF, angle: float) -> list[QPointF]:
    for i in range(len(part)):
        part[i] = rotate_point(part[i], point, angle)
    return part

def scalePoint(part: list[QPointF], point: QPointF, x: float, y: float) -> list[QPointF]:
    for i in range(len(part)):
        new_x = point.x() + (float(part[i].x()) - point.x()) * x
        new_y = point.y() + (float(part[i].y()) - point.y()) * y
        part[i] = QPointF(new_x, new_y)
    return part


def plusPoint(part: list[QPointF], point: QPointF) -> list[QPointF]:
    for i in range(len(part)):
        part[i] += point
    return part


def rotate_point(point: QPointF, point_center: QPointF, angle_degrees: float) -> QPointF:
    angle_radians = radians(angle_degrees)
    cos_theta = cos(angle_radians)
    sin_theta = sin(angle_radians)
    point -= point_center
    new_x = point.x() * cos_theta - point.y() * sin_theta + point_center.x()
    new_y = point.x() * sin_theta + point.y() * cos_theta + point_center.y()
    return QPointF(new_x, new_y)

def find_ellipse_points(part: list[QPointF], angle: float, num_points: int = 1000) -> list[QPointF]:
    a = QVector2D(part[2] - part[0]).length()
    b = QVector2D(part[1] - part[0]).length()
    points = []

    for i in range(num_points):
        t = 2 * pi * i / num_points
        x = part[0].x() + a * cos(t)
        y = part[0].y() + b * sin(t)
        points.append(rotate_point(QPointF(x, y), part[0], angle))
    return points