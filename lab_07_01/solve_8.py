from PyQt6.QtCore import QPoint

def intersection_point(p1, p2, q1, q2):
    x1, y1 = p1.x(), p1.y()
    x2, y2 = p2.x(), p2.y()
    x3, y3 = q1.x(), q1.y()
    x4, y4 = q2.x(), q2.y()

    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return None

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d

    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        return QPoint(round(x), round(y))
    else:
        return None

def solve8(lines, polygon):
    N = len(polygon)
    P = [polygon[-1]] + polygon

    clipped_lines = []
    j = 0
    while j < len(lines) - 1:
        t_enter = 0
        t_exit = 1

        for i in range(N):
            edge_start = P[i]
            edge_end = P[i + 1]

            normal = QPoint(edge_end.y() - edge_start.y(), edge_start.x() - edge_end.x())
            direction = QPoint(lines[j + 1].x() - lines[j].x(), lines[j + 1].y() - lines[j].y())
            P1 = QPoint(lines[j].x() - edge_start.x(), lines[j].y() - edge_start.y())

            numerator = normal.x() * P1.x() + normal.y() * P1.y()
            denominator = normal.x() * direction.x() + normal.y() * direction.y()

            if denominator == 0:
                if numerator < 0:
                    t_enter = 1
                    t_exit = 0
                    break
            else:
                t = -numerator / denominator

                if denominator > 0:
                    t_enter = max(t_enter, t)
                else:
                    t_exit = min(t_exit, t)

        if t_enter <= t_exit:
            intersection_start = QPoint(int(lines[j].x() + t_enter * (lines[j + 1].x() - lines[j].x())), int(lines[j].y() + t_enter * (lines[j + 1].y() - lines[j].y())))
            intersection_end = QPoint(int(lines[j].x() + t_exit * (lines[j + 1].x() - lines[j].x())), int(lines[j].y() + t_exit * (lines[j + 1].y() - lines[j].y())))
            clipped_lines.append((intersection_start, intersection_end))
        j += 2

    return clipped_lines

