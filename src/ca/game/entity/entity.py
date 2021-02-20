import abc


class Entity(abc.ABC):
    def __init__(self, positions:list):
        """
        Parameters
        ----------
        positions: list<Position>
        """
        self.positions = positions


    def size(self) -> int:
        return len(positions)


    @abc.abstractmethod
    def draw(self, surface:"pygame.Surface") -> None:
       ...

