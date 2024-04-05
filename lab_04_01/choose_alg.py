from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor
from cannon import cannon_circle, cannon_ellipse
from param import param_circle, param_ellipse
from brezenhem import brezenhem_circle, brezenhem_ellipse
from mid import mid_circle, mid_ellipse
from draw import draw_simple, draw_standart, draw_standart_specter, draw_circle_specter, draw_ellipse_specter


colors = dict(Красный = QColor("#FF0000"), Зеленый = QColor("#00FF00"), \
              Синий = QColor("#0000FF"), Оранжевый = QColor("#FF9670"), \
              Желтый = QColor("#FFB700"), Голубой = QColor("#3CA0D0"), \
              Фиолетовый = QColor("#9F3ED5"))
algs_circle = {"Каноническое уравнение" : cannon_circle, "Параметрическое уравнение" \
               : param_circle, "Алгоритм Брезенхема" : brezenhem_circle, "Алгоритм  средней точки" : mid_circle}
algs_ellipse = {"Каноническое уравнение" : cannon_ellipse, "Параметрическое уравнение" \
               : param_ellipse, "Алгоритм Брезенхема" : brezenhem_ellipse, "Алгоритм  средней точки" : mid_ellipse}


def choose(scene: QGraphicsScene, alg: str, color: str, type: str, center_point: QPointF, radius: float = 0, \
           axisX: float = 0, axisY: float = 0, amount: int = 0, step: float = 0) -> None:

    if alg == "Функция стандартной библиотеки":
        if type == "circle":
            draw_standart(scene, center_point, radius, radius, colors[color])
        elif type == "ellipse":
            draw_standart(scene, center_point, axisX, axisY, colors[color])
        elif type == "circle_range":
            draw_standart_specter(scene, center_point, radius, radius, colors[color], amount, step)
        elif type == "ellipse_range":
            draw_standart_specter(scene, center_point, axisX, axisY, colors[color], amount, step)

    else:        
        match type:
            case "circle":
                draw_simple(scene, algs_circle[alg](center_point, radius), colors[color])
            case "ellipse":
                draw_simple(scene, algs_ellipse[alg](center_point, axisX, axisY), colors[color])
            case "circle_range":
                draw_circle_specter(scene, algs_circle[alg], center_point, radius, amount, step, colors[color])
            case "ellipse_range":
                draw_ellipse_specter(scene, algs_ellipse[alg], center_point, axisX, axisY, amount, step, colors[color])