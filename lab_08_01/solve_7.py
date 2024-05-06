from PyQt6.QtCore import QPoint, QRect

INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(point, rect):
    code = INSIDE
    if point.x() < rect.left():
        code |= LEFT
    elif point.x() > rect.right():
        code |= RIGHT
    if point.y() < rect.top():
        code |= BOTTOM
    elif point.y() > rect.bottom():
        code |= TOP
    return code

def cohen_sutherland_clip(start_point, end_point, rect):
    code1 = compute_code(start_point, rect)
    code2 = compute_code(end_point, rect)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        
        elif code1 & code2 != 0:
            break
        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = start_point.x() + (end_point.x() - start_point.x()) * (rect.bottom() - start_point.y()) / (end_point.y() - start_point.y())
                y = rect.bottom()
            elif code_out & BOTTOM:
                x = start_point.x() + (end_point.x() - start_point.x()) * (rect.top() - start_point.y()) / (end_point.y() - start_point.y())
                y = rect.top()
            elif code_out & RIGHT:
                y = start_point.y() + (end_point.y() - start_point.y()) * (rect.right() - start_point.x()) / (end_point.x() - start_point.x())
                x = rect.right()
            elif code_out & LEFT:
                y = start_point.y() + (end_point.y() - start_point.y()) * (rect.left() - start_point.x()) / (end_point.x() - start_point.x())
                x = rect.left()

            if code_out == code1:
                start_point = QPoint(round(x), round(y))
                code1 = compute_code(start_point, rect)
            else:
                end_point = QPoint(round(x), round(y))
                code2 = compute_code(end_point, rect)

    if accept:
        return start_point, end_point
    else:
        return None

def solve7(segments, rect):
    rect = QRect(rect[0], rect[1])
    clipped_segments = []
    i = 0
    while i < len(segments) - 1:
        start_point, end_point = segments[i], segments[i + 1]
        clipped_segment = cohen_sutherland_clip(start_point, end_point, rect)
        if clipped_segment:
            clipped_segments.append(clipped_segment)
        i += 2
    return clipped_segments