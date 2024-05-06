import pytest
from PyQt6.QtCore import QPoint, QRect
from solve_7 import cohen_sutherland_clip
from solve_8 import intersection_point
from solve_9 import on_segment

# Предположим, что функция compute_code работает корректно

@pytest.mark.parametrize("start_point, end_point, rect, expected_result", [
    (QPoint(0, 0), QPoint(10, 10), QRect(2, 2, 8, 8), (QPoint(2, 2), QPoint(9, 9))),
    (QPoint(5, 5), QPoint(15, 15), QRect(2, 2, 8, 8), (QPoint(5, 5), QPoint(9, 9))),
    (QPoint(0, 0), QPoint(1, 1), QRect(5, 5, 10, 10), None),
])

def test_cohen_sutherland_clip(start_point, end_point, rect, expected_result):
    assert cohen_sutherland_clip(start_point, end_point, rect) == expected_result


@pytest.mark.parametrize("p1, p2, q1, q2, expected_result", [
    (QPoint(1, 1), QPoint(5, 5), QPoint(2, 3), QPoint(4, 2), QPoint(3, 3)),  # Линии пересекаются внутри отрезков
    (QPoint(1, 1), QPoint(5, 5), QPoint(6, 6), QPoint(8, 8), None),  # Линии параллельны и не пересекаются
    (QPoint(1, 1), QPoint(5, 5), QPoint(3, 0), QPoint(3, 3), QPoint(3, 3)),  # Линии пересекаются, но не внутри отрезковЫ
])
def test_intersection_point(p1, p2, q1, q2, expected_result):
    assert intersection_point(p1, p2, q1, q2) == expected_result


@pytest.mark.parametrize("p, q, r, expected_result", [
    (QPoint(1, 1), QPoint(5, 5), QPoint(3, 3), False),  # Точка r лежит на отрезке pq
    (QPoint(1, 1), QPoint(5, 5), QPoint(6, 6), True),  # Точка r лежит за пределами отрезка pq
    (QPoint(1, 1), QPoint(5, 5), QPoint(1, 5), False),  # Точка r совпадает с конечной точкой p
    (QPoint(1, 1), QPoint(5, 5), QPoint(5, 5), True),  # Точка r совпадает с конечной точкой q
])
def test_on_segment(p, q, r, expected_result):
    assert on_segment(p, q, r) == expected_result
