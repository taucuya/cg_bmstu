from PyQt6.QtCore import QPoint

def orientation(p, q, r):
    val = (q.y() - p.y()) * (r.x() - q.x()) - (q.x() - p.x()) * (r.y() - q.y())
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def on_segment(p, q, r):
    if (q.x() <= max(p.x(), r.x()) and q.x() >= min(p.x(), r.x()) and
        q.y() <= max(p.y(), r.y()) and q.y() >= min(p.y(), r.y())):
       return True
    return False


def solve9(polygon1, polygon2):
    n = len(polygon1)
    m = len(polygon2)
    intersection = []

    
    polygon1.append(polygon1[0])
    polygon2.append(polygon2[0])

    
    for i in range(n):
        for j in range(m):
            if do_intersect(polygon1[i], polygon1[i + 1], polygon2[j], polygon2[j + 1]):
                intersection_point = find_intersection(polygon1[i], polygon1[i + 1], polygon2[j], polygon2[j + 1])
                intersection.append(intersection_point)
    return intersection


def find_intersection(p1, q1, p2, q2):
    A1 = q1.y() - p1.y()
    B1 = p1.x() - q1.x()
    C1 = A1 * p1.x() + B1 * p1.y()

    A2 = q2.y() - p2.y()
    B2 = p2.x() - q2.x()
    C2 = A2 * p2.x() + B2 * p2.y()

    determinant = A1 * B2 - A2 * B1

    if determinant == 0:
        return None
    else:
        x = (B2 * C1 - B1 * C2) / determinant
        y = (A1 * C2 - A2 * C1) / determinant
        return QPoint(round(x), round(y))
