from collections import defaultdict
import copy
from enum import Enum
import math
import pygame

from .entity.individual import Individual
from .entity.position import Position


class UpdateMode(Enum):
    SYNCHRONOUS=0
    ASYNCHRONOUS=1


class GameMode(Enum):
    CONWAY=0


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


    @property
    def grid(self):
        """The exposed grid for use in drawing and such"""
        return self._drawing_grid


    def surface_pos_to_grid_pos(self, surface:"pygame.Surface",
            surf_pos:Position) -> None:
        # Determine the cell sizes
        cell_width = surface.get_width() / len(self._drawing_grid)
        cell_height = surface.get_height() / len(self._drawing_grid)

        grid_pos = Position(
                math.floor(surf_pos.x/cell_width),
                math.floor(surf_pos.y/cell_height)
                )

        if grid_pos.x >= len(self._drawing_grid):
            return None
        elif grid_pos.y >= len(self._drawing_grid):
            return None
        else:
            return grid_pos


    def draw(self, surface:"pygame.Surface") -> None:
        # Determine the cell sizes
        cell_width = surface.get_width() / len(self._drawing_grid)
        cell_height = surface.get_height() / len(self._drawing_grid)

        # Draw the cells
        for x in self._drawing_grid:
            for y in self._drawing_grid[x]:
                cell_surface = surface.subsurface(
                        pygame.Rect(
                            (x*cell_width, y*cell_height),
                            (cell_width, cell_height)))
                self._drawing_grid[x][y].draw(cell_surface)


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
            iter<Entity>
        """
        recorded_positions = []
        max_position = Position(len(self.grid), len(self.grid))
        for x in range(math.floor(position.x-radius),
                math.ceil(position.x+radius)):
            for y in range(math.floor(position.y-radius),
                math.ceil(position.y+radius)):
                if x < 0:
                    x = x + len(self.grid)
                elif x >= len(self.grid):
                    x = len(self.grid) - x

                if y < 0:
                    y = y + len(self.grid)
                elif y >= len(self.grid):
                    y = len(self.grid) - y

                if Position(x,y) not in recorded_positions:
                    entity = self.grid[x][y]
                    for pos in entity.positions:
                        dist = position.distance(pos, metric, self.boundary_type, max_position)
                        if  dist <= radius and dist != 0:
                            yield entity
                    recorded_positions.extend(entity.positions)


    def update(self) -> None:
        if self.update_mode == UpdateMode.ASYNCHRONOUS:
            self.asynchronous_update()
        else:
            self.synchronus_update()


    def asynchronous_update(self) -> None:
        """Perform an update with asynchronusly, as in we first make
        a copy of the grid of entities and perform updates with that
        information.
        """
        # Make a copy of the drawing grid to the working grid
        self._working_grid = copy.deepcopy(self._drawing_grid)
        updated = defaultdict(lambda: defaultdict(lambda: False))

        # Go through each entity, asking it to make a move.
        for x in self._drawing_grid:
            for y in self._drawing_grid[x]:
                # Has it already been updated?
                if not updated[x][y]:
                    # Is an individual?
                    if isinstance(self._drawing_grid[x][y], Individual):
                        self._working_grid[x][y].make_move(self)
                        # Mark every position of this individual
                        # as updated
                        for pos in self._working_grid[x][y].positions:
                            updated[pos.x][pos.y] = True

        # Copy the working grid to drawing grid.
        self._drawing_grid = copy.deepcopy(self._working_grid)


    def synchronus_update(self) -> None:
        """Perform an update with synchronusly, as in we update the
        grid as we go through it
        """
        raise NotImplementedError

    
    def insert_entities(self, grid:dict, insert_point:"Position", 
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
        self._working_grid = copy.deepcopy(self._drawing_grid)
        for x in grid:
            for y in grid[x]:
                insert_x = insert_point.x + x
                insert_y = insert_point.y + y
                if self._working_grid[insert_x][insert_y] is not None and \
                    check_collision:
                    print(f"Can not insert, collision at x:{insert_x},"
                        f"y:{insert_y}")
                    return False
                # Save the new entity
                self._working_grid[insert_x][insert_y] = grid[x][y]
                self._working_grid[insert_x][insert_y].positions.remove(
                        Position(x,y))
                self._working_grid[insert_x][insert_y].positions.append(
                    Position(insert_x,insert_y))
        self._drawing_grid = copy.deepcopy(self._working_grid)


    def delete_entity(self, position: "Position") -> None:
        """Delete the entity that exists within that position"""
        entity = self.grid[position.x][position.y]
        for pos in entity.positions:
            self.grid[pos.x][pos.y] = None

