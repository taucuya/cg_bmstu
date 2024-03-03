from math import acos, degrees
from PyQt6 import QtWidgets, QtCore, QtGui

EPSILON = 1e-5

# Функция для вычисления координат точки пересечения двух прямых по их уравнениям
# Получает коэфициенты a, b, c для уравнений прямых и возвращает точку перес ечения этих прямых
def get_intersection_point(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float) -> QtCore.QPointF:
    if a1 * b2 - a2 * b1 == 0:
        return None
    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)

    return QtCore.QPointF(x, y)


# Функция для вычисления координат точки пересечения высоты и стороны треугольника
# Получает точки вершин треугольника и возвращает точку пересечения высоты и стороны
def height_side_intersection(A: QtCore.QPointF, B: QtCore.QPointF, C: QtCore.QPointF) -> QtCore.QPointF:
    a = B.y() - A.y()
    b = A.x() - B.x()
    c = B.x() * A.y() - A.x() * B.y()
    # Находим коэффициенты уравнения высоты, проходящей через вершину С и перпендикулярной стороне
    a1 = b
    b1 = -a
    c1 = a * C.y() - b * C.x()
    # Находим координаты точки пересечения высоты и стороны
    return get_intersection_point(a, b, c, a1, b1, c1)

# Получает 2 точки треугольника и длины прилежаших к ним сторон, возвращает биссектриссу в векторном виде
def getVector(point1: QtCore.QPointF, point2: QtCore.QPointF, a: float, b: float) -> QtGui.QVector2D:
    x = (a * point1.x() + b * point2.x()) / (a + b)
    y = (a * point1.y() + b * point2.y()) / (a + b)

    return QtGui.QVector2D(x, y)

# Получает треугольник в координатах, возвращает три биссектриссы в векторном виде
def bisector_side(triangle: QtGui.QPolygonF) -> tuple:
    ab = QtGui.QVector2D(triangle[0] - triangle[1])
    bc = QtGui.QVector2D(triangle[2] - triangle[1])
    ac = QtGui.QVector2D(triangle[0] - triangle[2])
    ab = ab.length()
    bc = bc.length()
    ac = ac.length()

    a = getVector(triangle[2], triangle[1], ab, ac)
    b = getVector(triangle[2], triangle[0], ab, bc)
    c = getVector(triangle[1], triangle[0], ac, bc)

    return a, b, c

# Принимает три угла треугольника, возвращает углы между биссектриссой и высотой для треугольника с тупым или прямым
# углом
def get_angles_for_obtuse_or_right(alpha: float, beta: float, gamma: float) -> tuple:
    theta_a = (alpha / 2) - 90 + max(beta, gamma)
    theta_b = alpha - 90 + (beta / 2)
    theta_c = alpha - 90 + (gamma / 2)
    return theta_a, theta_b, theta_c

# Принимает три угла треугольника, возвращает углы между биссектриссой и высотой для треугольника, где все углы острые
def get_angle_for_acute(alpha: float, beta: float, gamma: float) -> tuple:
    theta_a = (alpha / 2) - 90 + max(beta, gamma)
    theta_b = (beta / 2) - 90 + max(alpha, gamma)
    theta_c = (gamma / 2) - 90 + max(beta, alpha)
    return theta_a, theta_b, theta_c


# Функция, которая принимает углы треугольника в градусах и возвращает углы между биссектрисой и высотой для каждого
# угла треугольника
def calculate_angles_between_bisectors_and_heights(alpha: float, beta: float, gamma: float) -> tuple:
    if alpha >= 90 - EPSILON:
        theta_a, theta_b, theta_c = get_angles_for_obtuse_or_right(alpha, beta, gamma)
    elif beta >= 90 - EPSILON:
        theta_b, theta_a, theta_c = get_angles_for_obtuse_or_right(beta, alpha, gamma)
    elif gamma >= 90 - EPSILON:
        theta_c, theta_a, theta_b = get_angles_for_obtuse_or_right(gamma, alpha, beta)
    else:
        theta_a, theta_b, theta_c = get_angle_for_acute(gamma, alpha, beta)
    return theta_a, theta_b, theta_c

def check_for_math_err(alpha: float) -> float:
    if alpha > 1:
        alpha = 1
    elif alpha < -1:
        alpha = -1
    return alpha

# Функция принимает треугольник в координатых вершин и возвращает углы треугольника
def get_triangle_angles(triangle: QtGui.QPolygonF) -> tuple:
    ab = QtGui.QVector2D(triangle[0] - triangle[1])
    bc = QtGui.QVector2D(triangle[2] - triangle[1])
    ac = QtGui.QVector2D(triangle[0] - triangle[2])

    mod_ab = ab.length()
    mod_bc = bc.length()
    mod_ac = ac.length()

    alpha = (mod_ac ** 2 + mod_ab ** 2 - mod_bc ** 2) / (2 * mod_ac * mod_ab)
    betta = (mod_bc ** 2 + mod_ab ** 2 - mod_ac ** 2) / (2 * mod_bc * mod_ab)

    alpha = degrees(acos(check_for_math_err(alpha)))
    betta = degrees(acos(check_for_math_err(betta)))
    gamma = 180 - alpha - betta

    if mod_ab ** 2 >= (mod_bc ** 2 + mod_ac ** 2):
        gamma = 180 - alpha - betta

    if mod_ac ** 2 >= (mod_ab ** 2 + mod_bc ** 2):
        betta = 180 - alpha - gamma

    if mod_bc ** 2 >= (mod_ab ** 2 + mod_ac ** 2):
        alpha = 180 - betta - gamma

    return alpha, betta, gamma

# Функция принимает массив всех точек на координатном поле и формирует массив с уникальными треугольниками
def find_triangles(mas: list) -> list:
    triangle = []
    for i in range(len(mas) - 2):
        for j in range(i + 1, len(mas) - 1):
            for k in range(j + 1, len(mas)):
                if isTriangle(mas[i], mas[j], mas[k]):
                    polygon = QtGui.QPolygonF([QtCore.QPointF(mas[i][0], mas[i][1]), QtCore.QPointF(mas[j][0], mas[j][1]),
                                          QtCore.QPointF(mas[k][0], mas[k][1])])
                    triangle.append(polygon)
    return triangle

# Функция проверяет вырожденность треугольника
def isTriangle(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) != 0

# Функция принимает массмв треугольников и возвращает индекс вершины из которой угол между биссектриссой и
# высотой максимален и треугольник с максимальным таким углом
def findMax(triangle: list) -> tuple:
    mx = 0
    res = [0, 0, 0]
    for i in range(len(triangle)):
        alpha, betta, gamma = get_triangle_angles(triangle[i])
        n_a, n_b, n_c = calculate_angles_between_bisectors_and_heights(alpha, betta, gamma)
        if mx < (n_a + EPSILON) or mx < (n_b + EPSILON) or mx < (n_c + EPSILON):
            mx_ind = i
            res[0] = n_a
            res[1] = n_b
            res[2] = n_c
            mx = max(n_a, n_b, n_c)
            mx_ = res.index(max(n_a, n_b, n_c))
    return mx_, triangle[mx_ind]