from PyQt6.QtCore import QPointF
from math import sin, cos, radians

def sign(num: float) -> int:
    return 1 if num > 0 else -1 if num < 0 else 0
