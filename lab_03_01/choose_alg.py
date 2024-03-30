from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor
from dda import dda
from brozenhemFloat import brozenhemFloat
from brozenhemInt import brozenhemInt
from brozenhemNoGrad import brozenhemNoGrad
from vu import vu
from draw import draw_line, draw_standart, draw_specter, draw_standart_specter

colors = dict(Красный = QColor("#FF0000"), Зеленый = QColor("#00FF00"), Синий = QColor("#0000FF"), Черный = QColor("#000000"), Желтый = QColor("#FFB700"))

def choose(scene: QGraphicsScene, alg: str, color: str, type: str, point_start: QPointF, point_end: QPointF, length: float, angle: float) -> None:

    match alg:
        case "Брезенхем (Целочисленный)":
            if type == "line":
                draw_line(scene, brozenhemInt(point_start, point_end, colors[color]))
            else:
                draw_specter(scene, brozenhemInt, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])
        case "Брезенхем (Вещественный)":
            if type == "line":
                draw_line(scene, brozenhemFloat(point_start, point_end, colors[color]))
            else:
                draw_specter(scene, brozenhemFloat, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])
        case "Брезенхем (С устранением ступенчатости)":
            if type == "line":
                draw_line(scene, brozenhemNoGrad(point_start, point_end, colors[color]))
            else:
                draw_specter(scene, brozenhemNoGrad, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])
        case "Цифровой дифференциальный анализатор":
            if type == "line":
                draw_line(scene, dda(point_start, point_end, colors[color]))
            else:
                draw_specter(scene, dda, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])
        case "Ву":
            if type == "line":
                draw_line(scene, vu(point_start, point_end, colors[color]))
            else:
                draw_specter(scene, vu, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])
        case "Функция стандартной библиотеки":
            if type == "line":
                draw_standart(scene, point_start, point_end, colors[color])
            else:
                draw_standart_specter(scene, QPointF(0, 0), QPointF(length, 0), length, angle, colors[color])

