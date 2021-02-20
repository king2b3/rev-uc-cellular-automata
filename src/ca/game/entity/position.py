import enum

class DistanceMetric(enum):
    MANHATTAN=0
    EUCLIDIAN=1


class Position():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


    def euclidian_distance(self, other:"Position") -> float:
        raise NotImplemented


    def manhattan_distance(self, other:"Position") -> float:
        raise NotImplemented

