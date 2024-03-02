from math import *
from PyQt6 import QtWidgets
EPSILON = 1e-5

# Функция для вычисления координат точки пересечения двух прямых по их уравнениям
def intersection(a1, b1, c1, a2, b2, c2):
    # Проверяем, что прямые не параллельны
    if a1 * b2 - a2 * b1 != 0:
        x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
        y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
        return x, y
    else:
        return None


# Функция для вычисления координат точки пересечения высоты и стороны треугольника
def altitude_side(x1, y1, x2, y2, x3, y3):
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    # Находим коэффициенты уравнения высоты, проходящей через вершину (x3, y3) и перпендикулярной стороне
    a1 = b
    b1 = -a
    c1 = a * y3 - b * x3
    # Находим координаты точки пересечения высоты и стороны
    return intersection(a, b, c, a1, b1, c1)


# Функция для вычисления координат точки пересечения биссектрисы и стороны треугольника
def bisector_side(xa, ya, xb, yb, xc, yc):
    ab = hypot(xb - xa, yb - ya)
    bc = hypot(xc - xb, yc - yb)
    ca = hypot(xc - xa, yc - ya)

    x_a = (ab * xc + ca * xb) / (ab + ca)
    y_a = (ab * yc + ca * yb) / (ab + ca)

    x_b = (ab * xc + bc * xa) / (ab + bc)
    y_b = (ab * yc + bc * ya) / (ab + bc)

    x_c = (ca * xb + bc * xa) / (ca + bc)
    y_c = (ca * yb + bc * ya) / (ca + bc)
    return x_a, y_a, x_b, y_b, x_c, y_c


def typoy(alpha, beta, gamma):
    theta_a = (alpha / 2) - 90 + max(beta, gamma)
    theta_b = alpha - 90 + (beta / 2)
    theta_c = alpha - 90 + (gamma / 2)
    return theta_a, theta_b, theta_c


def pryamoy(alpha, beta, gamma):
    theta_a = (alpha / 2) - 90 + max(beta, gamma)
    theta_b = beta / 2
    theta_c = gamma / 2
    return theta_a, theta_b, theta_c


def ostry(alpha, beta, gamma):
    theta_a = (alpha / 2) - 90 + max(beta, gamma)
    theta_b = (beta / 2) - 90 + max(alpha, gamma)
    theta_c = (gamma / 2) - 90 + max(beta, alpha)
    return theta_a, theta_b, theta_c


# определяем функцию, которая принимает углы треугольника в градусах и длины сторон
def calculate_angles_between_bisectors_and_heights(alpha, beta, gamma):
    if alpha > 90:
        theta_a, theta_b, theta_c = typoy(alpha, beta, gamma)
    elif beta > 90:
        theta_b, theta_a, theta_c = typoy(beta, alpha, gamma)
    elif gamma > 90:
        theta_c, theta_a, theta_b = typoy(gamma, alpha, beta)
    elif alpha == 90:
        theta_a, theta_b, theta_c = pryamoy(alpha, beta, gamma)
    elif beta == 90:
        theta_b, theta_a, theta_c = pryamoy(beta, alpha, gamma)
    elif gamma == 90:
        theta_c, theta_a, theta_b = pryamoy(gamma, alpha, beta)
    else:
        theta_a, theta_b, theta_c = ostry(gamma, alpha, beta)
    return theta_a, theta_b, theta_c


def printAngle(A, B, C):
    ab = [abs(A[0] - B[0]), abs(A[1] - B[1])]
    bc = [abs(C[0] - B[0]), abs(C[1] - B[1])]
    ac = [abs(A[0] - C[0]), abs(A[1] - C[1])]

    mod_ab = (ab[0] ** 2 + ab[1] ** 2) ** 0.5
    mod_bc = (bc[0] ** 2 + bc[1] ** 2) ** 0.5
    mod_ac = (ac[0] ** 2 + ac[1] ** 2) ** 0.5

    alpha = degrees(acos((mod_ac ** 2 + mod_ab ** 2 - mod_bc ** 2) / (2 * mod_ac * mod_ab)))
    betta = degrees(acos((mod_bc ** 2 + mod_ab ** 2 - mod_ac ** 2) / (2 * mod_bc * mod_ab)))
    gamma = 180 - alpha - betta

    if mod_ab ** 2 >= (mod_bc ** 2 + mod_ac ** 2):
        gamma = 180 - alpha - betta

    if mod_ac ** 2 >= (mod_ab ** 2 + mod_bc ** 2):
        betta = 180 - alpha - gamma

    if mod_bc ** 2 >= (mod_ab ** 2 + mod_ac ** 2):
        alpha = 180 - betta - gamma

    return alpha, betta, gamma


def res(triangle):
    x_arr = []
    y_arr = []
    mx_, mx_ind = findMax(triangle)

    for i in triangle[mx_ind]:
        x_arr.append(i[0])
        y_arr.append(i[1])
    x_arr.append(triangle[mx_ind][0][0])
    y_arr.append(triangle[mx_ind][0][1])

    A = (x_arr[0], y_arr[0])
    B = (x_arr[1], y_arr[1])
    C = (x_arr[2], y_arr[2])
    point1 = [0, 0]
    point2 = [0, 0]
    point3 = [0, 0]

    point1[0], point1[1], point2[0], point2[1], point3[0], point3[1] = bisector_side(A[0], A[1], B[0], B[1],
                                                                                     C[0], C[1])
    xb, yb, xh, yh = formBisHeight(mx_, A, B, C, point1, point2, point3)

    return x_arr, y_arr, xb, yb, xh, yh

def find_triangles(mas):
    triangle = []
    for i in range(len(mas) - 2):
        for j in range(i + 1, len(mas) - 1):
            for k in range(j + 1, len(mas)):
                if not isTriangle(mas[i], mas[j], mas[k]):
                    continue
                triangle.append([mas[i], mas[j], mas[k]])
    return triangle

def isTriangle(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) != 0

def show_msg(str):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(str)
    msg.exec()

def findMax(triangle):
    mx = 0
    res = [0, 0, 0]
    for i in range(len(triangle)):
        alpha, betta, gamma = printAngle(triangle[i][0], triangle[i][1], triangle[i][2])
        n_a, n_b, n_c = calculate_angles_between_bisectors_and_heights(alpha, betta, gamma)
        if mx < (n_a + EPSILON) or mx < (n_b + EPSILON) or mx < (n_c + EPSILON):
            mx_ind = i
            res[0] = n_a
            res[1] = n_b
            res[2] = n_c
            mx = max(n_a, n_b, n_c)
            mx_ = res.index(max(n_a, n_b, n_c))
    return mx_, mx_ind

def formBisHeight(mx_, A, B, C, point1, point2, point3):
    if mx_ == 2:
        xb = [C[0], point3[0]]
        yb = [C[1], point3[1]]
        x_h, y_h = altitude_side(A[0], A[1], B[0], B[1], C[0], C[1])
        xh = [C[0], x_h]
        yh = [C[1], y_h]

    elif mx_ == 0:
        xb = [A[0], point1[0]]
        yb = [A[1], point1[1]]
        x_h, y_h = altitude_side(B[0], B[1], C[0], C[1], A[0], A[1])
        xh = [A[0], x_h]
        yh = [A[1], y_h]

    elif mx_ == 1:
        xb = [B[0], point2[0]]
        yb = [B[1], point2[1]]
        x_h, y_h = altitude_side(C[0], C[1], A[0], A[1], B[0], B[1])
        xh = [B[0], x_h]
        yh = [B[1], y_h]

    return xb, yb, xh, yh