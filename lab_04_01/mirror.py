from PyQt6.QtCore import QPointF

def mirror(arr, cur_point, center_point):
    arr.append(cur_point)
    arr.append(QPointF(2*center_point.x()-cur_point.x(), cur_point.y()))
    arr.append(QPointF(cur_point.x(), 2*center_point.y()-cur_point.y()))
    arr.append(QPointF(2*center_point.x()-cur_point.x(), 2*center_point.y()-cur_point.y()))
    arr.append(QPointF(cur_point.y() + center_point.x() - center_point.y(), cur_point.x() + center_point.y() - center_point.x()))
    arr.append(QPointF(-cur_point.y() + center_point.x() + center_point.y(), cur_point.x() + center_point.y() - center_point.x()))
    arr.append(QPointF(cur_point.y() + center_point.x() - center_point.y(), -cur_point.x() + center_point.y() + center_point.x()))
    arr.append(QPointF(-cur_point.y() + center_point.x() + center_point.y(), -cur_point.x() + center_point.y() + center_point.x()))
    return arr

def mirror_ellipse(arr, cur_point, center_point):

    arr.append(QPointF(cur_point.x(), cur_point.y()))
    arr.append(QPointF(2 * center_point.x() - cur_point.x(), cur_point.y()))
    arr.append(QPointF(cur_point.x(), 2*center_point.y()-cur_point.y()))
    arr.append(QPointF(2*center_point.x()-cur_point.x(), 2*center_point.y()-cur_point.y()))
    return arr