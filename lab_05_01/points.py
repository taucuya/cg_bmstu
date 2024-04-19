from PyQt6.QtCore import QPoint

def check_points(pointArray: list) -> bool:
    if len(pointArray) <= 2:
        return False
    return True

def makeMid(pointArray: list) -> tuple:
    pointLeft = min(pointArray, key=lambda p: p.x())
    pointRight = max(pointArray, key=lambda p: p.x())
    x = (pointRight.x() + pointLeft.x()) // 2
    point_up = max(pointArray, key=lambda p: p.y())
    point_down = min (pointArray, key=lambda p: p.y())
    mid_line = [QPoint(x, point_up.y()), QPoint(x, point_down.y())]
    return mid_line
    
    
