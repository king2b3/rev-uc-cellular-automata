from enum import Enum
import math


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


    def __eq__(self, other:"Position") -> bool:
        if self.x != other.x:
            return False
        elif self.y != other.y:
            return False
        else:
            return True


    def distance(self, other:"Position", metric:DistanceMetric,
        boundary_type:BoundaryType, max_position:"Position"=None) -> float:
        if metric == metric.EUCLIDIAN:
            return self.euclidian_distance(other, boundary_type,
                    max_position)
        elif metric == metric.MANHATTAN:
            return self.manhattan_distance(other, boundary_type,
                    max_position)
        else:
            raise ValueError(f"Unknown metric enum: {metric.name}")


    def euclidian_distance(self, other:"Position", 
            boundary_type:BoundaryType, max_position:"Position"=None) -> float:
        """Calculate the euclidian distance between two points.
        
        Parameters
        ----------
        other: Position
            The position to calculate the distance from

        BoundaryType: BoundaryType
            The boundary type to calculate the distance in.

        max_position: Position
            The maximum x and y axis values. Used in calculating the
            periodic boundaries.
        """
        # Compute the deltas
        delta_x = abs(self.x - other.x)
        delta_y = abs(self.y - other.y)

        # Do extra work if it's Periodic distance
        if boundary_type == BoundaryType.PERIODIC:
            if delta_x > max_position.x - delta_x:
                delta_x = max_position.x - delta_x
            if delta_y > max_position.y - delta_y:
                delta_y = max_position.y - delta_y
        elif boundary_type == BoundaryType.HARD:
            pass
        else:
            raise ValueError(f"Unknown boundary enum: "\
                    f"{boundary_type.name}")

        # Return the distance
        return math.sqrt(pow(delta_x,2) + pow(delta_y,2))


    def manhattan_distance(self, other:"Position", 
            boundary_type:BoundaryType, max_position:"Position"=None) -> float:
        """Calculate the manhattan distance between two points.
        
        Parameters
        ----------
        other: Position
            The position to calculate the distance from

        BoundaryType: BoundaryType
            The boundary type to calculate the distance in.

        max_position: Position
            The maximum x and y axis values. Used in calculating the
            periodic boundaries.
        """
        if boundary_type == BoundaryType.HARD:
            return abs(self.x - other.x) + abs(self.y - other.y)
        elif boundary_type == BoundaryType.PERIODIC:
            raise NotImplementedError
        else:
            raise ValueError(f"Unknown boundary enum: "\
                    f"{boundary_type.name}")

