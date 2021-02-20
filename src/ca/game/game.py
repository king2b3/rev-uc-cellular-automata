import copy
import enum


class UpdateMode(enum):
    SYNCHRONOUS=0
    ASYNCHRONOUS=1


class Game():
    def __init__(self, update_mode:UpdateMode, grid:dict):
        """
        Parameters
        ----------
        update_mode: UpdateMode
            Rather the update mode is synchronous or asynchronous

        grid: dict<dict<Entity>>
            The x,y plane of entities.
            The top layer of dicts is the x plane, the inner dicts
            are the y plane.
        """
        self.update_mode = update_mode
        self._drawing_grid = grid
        self._working_grid = copy.deepcopy(grid)


    def update_grid(self) -> None:
        self._drawing_grid = copy.deepcopy(self._working_grid)


    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplemented


    def neighbors(self, position:"Position", metric:"DistanceMetric",\
            radius:float) -> iter:
        """Returns an iterable of the  neighbors within the given radius using 
        the given metric.

        Parameters
        ----------
        position: Position
            The position to center the search of neighbors on.

        metric: DistanceMetric
            The distance metric to use.

        radius: float
            The radius to search in.

        Returns
        -------
            iter<Tuple<Position, Entity>>
        """
        raise NotImplemented


    def asynchronous_update(self) -> None:
        """Perform an update with asynchronusly, as in we first make
        a copy of the grid of entities and perform updates with that
        information.
        """
        raise NotImplemented


    def synchronus_update(self) -> None:
        """Perform an update with synchronusly, as in we update the
        grid as we go through it
        """
        raise NotImplemented

