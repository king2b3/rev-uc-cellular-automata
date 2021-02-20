from enum import Enum


class DistanceMetric(Enum):
    MANHATTAN=0
    EUCLIDIAN=1


class BoundaryType(Enum):
    HARD=0
    PERIODIC=1


class Position():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


    def euclidian_distance(self, other:"Position", 
            boundary_type:BoundaryType) -> float:
        raise NotImplementedError


    def manhattan_distance(self, other:"Position", 
            boundary_type:BoundaryType) -> float:
        raise NotImplementedError

