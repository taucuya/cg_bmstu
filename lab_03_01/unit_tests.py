import pytest
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPointF
from dda import dda
from brozenhemInt import brozenhemInt
from brozenhemFloat import brozenhemFloat
from brozenhemNoGrad import brozenhemNoGrad
from vu import vu


def test_dda():

    expected = [QPointF(1, 1), QPointF(2, 2), QPointF(3, 3)]

    temp = dda(QPointF(0, 0), QPointF(2, 2), QColor("#ffffff"))
    result = []
    for i in temp:
        result.append(i[0])
    assert result == expected

def test_brozenhemInt():

    expected = [QPointF(), QPointF(1, 1)]

    temp = brozenhemInt(QPointF(0, 0), QPointF(2, 2), QColor("#ffffff"))
    result = []
    for i in temp:
        result.append(i[0])
    assert result == expected

def test_brozenhemFloat():

    expected = [QPointF(), QPointF(1, 1)]

    temp = brozenhemFloat(QPointF(0, 0), QPointF(2, 2), QColor("#ffffff"))
    result = []
    for i in temp:
        result.append(i[0])
    assert result == expected

def test_brozenhemNoGrad():

    expected = [QPointF(), QPointF(1, 1)]

    temp = brozenhemNoGrad(QPointF(0, 0), QPointF(2, 2), QColor("#ffffff"))
    result = []
    for i in temp:
        result.append(i[0])
    assert result == expected

def test_vu():

    expected = [QPointF(1, 1), QPointF(1, 2), QPointF(2, 2), QPointF(2, 3)]

    temp = vu(QPointF(0, 0), QPointF(2, 2), QColor("#ffffff"))
    result = []
    for i in temp:
        result.append(i[0])
    assert result == expected