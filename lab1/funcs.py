from math import *

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

    alpha = degrees(acos((ab[0] * ac[0] + ab[1] * ac[1]) / (mod_ac * mod_ab)))
    betta = degrees(acos((ab[0] * bc[0] + ab[1] * bc[1]) / (mod_bc * mod_ab)))
    gamma = degrees(acos((ac[0] * bc[0] + ac[1] * bc[1]) / (mod_bc * mod_ac)))

    if mod_ab ** 2 > (mod_bc ** 2 + mod_ac ** 2):
        gamma = 180 - alpha - betta

    if mod_ac ** 2 > (mod_ab ** 2 + mod_bc ** 2):
        betta = 180 - alpha - gamma

    if mod_bc ** 2 > (mod_ab ** 2 + mod_ac ** 2):
        alpha = 180 - betta - gamma

    return alpha, betta, gamma
