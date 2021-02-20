import copy
import enum


class UpdateMode(enum):
    SYNCHRONOUS=0
    ASYNCHRONOUS=1


class Game():
    def __init__(self, update_mode:UpdateMode, grid:dict, 
            boundary_type:"BoundaryType"):
        """
        Parameters
        ----------
        update_mode: UpdateMode
            Rather the update mode is synchronous or asynchronous

        grid: dict<dict<Entity>>
            The x,y plane of entities.
            The top layer of dicts is the x plane, the inner dicts
            are the y plane.

        boundary_type: BoundaryType
            Rather the boundary is periodic or hard af.
        """
        self.update_mode = update_mode
        self.boundary_type = boundary_type
        self._drawing_grid = grid
        self._working_grid = copy.deepcopy(grid)


    def update_grid(self) -> None:
        self._drawing_grid = copy.deepcopy(self._working_grid)


    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError


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
        raise NotImplementedError


    def asynchronous_update(self) -> None:
        """Perform an update with asynchronusly, as in we first make
        a copy of the grid of entities and perform updates with that
        information.
        """
        raise NotImplementedError


    def synchronus_update(self) -> None:
        """Perform an update with synchronusly, as in we update the
        grid as we go through it
        """
        raise NotImplementedError

    
    def insert_entities(grid:dict, insert_point:Position, 
            check_collision:bool=True) -> None:
        """Insert a mini grid of entities described with relative
        positions to the grid at the specified insert point.

        Parameters
        ----------
        grid: dict<dict<Tuple<Position, Entity>>
            The grid of entities described in a relative position
            to be added to the big grid.
        insert_point: Position
            The insert point to add to the grid.
            Note that it assumes this is the bottom left, as the
            bottom left is origin for all grids.
        check_collision: bool = True
            Rather we are concerned about collisions when inserting.
            Default is to only allow inserting the new entities if that
            grid space is completely devoid.
        """
        raise NotImplementedError


    def delete_entity(position: "Position") -> None:
        """Delete the entity that exists within that position"""
        raise NotImplementedError
