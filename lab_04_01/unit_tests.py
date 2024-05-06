import pytest
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPointF
from mirror import mirror


def test_mirror():
    center_point = QPointF(0, 0)
    cur_point = QPointF(5, 5)
    expected_result = [
        QPointF(5, 5), 
        QPointF(-5, 5), 
        QPointF(5, -5), 
        QPointF(-5, -5), 
        QPointF(5, 5), 
        QPointF(-5, 5), 
        QPointF(5, -5), 
        QPointF(-5, -5)
    ]
    assert mirror([], cur_point, center_point) == expected_result
