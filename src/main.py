#!/usr/bin/env python3
"""The main file for our Cellar Automata project"""

import argparse
import PIL
import pygame
import os
import tempfile
import time

from ca.game.entity.conway import Conway,\
        next_formation as conway_next_formation
from ca.game.entity import Position
from ca.game import Game, UpdateMode, BoundaryType, GameMode
from ca.plot import AlivePlot, AverageTraits, AverageTraitTime
from ca.window import Window


def parse_arguments(args=None) -> None:
    """Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="Not much here yet, just wait a day.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-sf", "--save_file",
            default="save.gif",
            help="The name to save a gif of the simulation to")
    parser.add_argument("-sbu", "--seconds_between_updates",
            default=0.5, type=lambda s: abs(float(s)),
            help="The number of seconds between each update of the game")
    def string_to_boundary_type(s:str):
        s = s.upper()
        if s == "PERIODIC":
            return BoundaryType.PERIODIC
        elif s == "HARD":
            return BoundaryType.HARD
        else:
            raise ValueError(f"Unknown boundary condition: {s}")
    parser.add_argument("-b", "--boundary_type",
            default=BoundaryType.PERIODIC, type=string_to_boundary_type,
            help="The type of boundary condition to use.")
    def string_to_update_mode(s:str):
        s = s.upper()
        if s == "ASYNCHRONOUS":
            return UpdateMode.ASYNCHRONOUS
        elif s == "SYNCHRONOUS":
            return UpdateMode.SYNCHRONOUS
        else:
            raise ValueError(f"Unknown update mode: {s}")
    parser.add_argument("-u", "--update_mode",
            default=UpdateMode.ASYNCHRONOUS,
            type=string_to_update_mode,
            help="The type of update mode to use.")
    def string_to_gamemode(s:str):
        s = s.upper()
        if s == "CONWAY":
            return GameMode.CONWAY
        else:
            raise ValueError(f"Unknown game mode: {s}")
    parser.add_argument("-gm", "--game_mode",
            default=GameMode.CONWAY, type=string_to_gamemode,
            help="The type of game mode to use.")
    args = parser.parse_args(args=args)
    return args


def main(save_file:str, seconds_between_updates:float=0.5,
        boundary_type:BoundaryType=BoundaryType.PERIODIC,
        update_mode:UpdateMode=UpdateMode.ASYNCHRONOUS,
        game_mode:GameMode=GameMode.CONWAY) -> int:
    """Main function.

    Parameters
    ----------
    seconds_between_updates: float=0.5
        The number of seconds between each update of the game.

    boundary_type: BoundaryType=PERIODIC
        The type of boundary condition to use.

    update_mode: UpdateMode=ASYNCHRONOUS
        The type of update mode to use.

    game_mode: GameMode=CONWAY
        The type of game mode to use.

    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    if game_mode == GameMode.CONWAY:
        # Make an "empty grid" of dead conway cells
        width = height = 50
        grid = {}
        for x in range(width):
            grid[x] = {}
            for y in range(height):
                grid[x][y] = Conway(Position(x,y), False)

        # Give it that dead grid
        game = Game(update_mode, grid, boundary_type)
        formation_generator = conway_next_formation()
        cursor = next(formation_generator)
    else:
        raise(f"WHAT HAVE YOU DONE. {game_mode.name} IS NOT KNOWN")

    frame_dir_handle = tempfile.\
            TemporaryDirectory(prefix="celluar_automat_frames_")
    window = Window(game, 
            [AlivePlot(), AverageTraits(), AverageTraitTime(), None], 
            frame_dir_handle.name, 600, 1200)


    started = False
    time_since_last_update = time.perf_counter()
    window.draw(cursor[0], True)
    do_gui = True
    while do_gui:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_gui = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    do_gui = False
                elif event.key == pygame.K_RETURN:
                    started = not started
                elif event.key == pygame.K_SPACE:
                    cursor = next(formation_generator)
                elif event.key == pygame.K_c:
                    if game_mode == GameMode.CONWAY:
                        grid = {}
                        for x in range(len(game.grid)):
                            grid[x] = {}
                            for y in range(len(game.grid[0])):
                                grid[x][y] = Conway(Position(x,y), False)
                        game.insert_entities(grid, Position(0,0), False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = Position(
                            pygame.mouse.get_pos()[0],
                            pygame.mouse.get_pos()[1])
                    grid_pos = game.surface_pos_to_grid_pos(
                            window._game_subsurface,
                            click_pos)
                    if game_mode == GameMode.CONWAY:
                        if grid_pos is not None:
                            game.insert_entities(cursor[1](), grid_pos, False)

        window.draw(cursor[0], started)
        if time.perf_counter() - time_since_last_update\
                >= seconds_between_updates and started:
            time_since_last_update = time.perf_counter()
            window.update()

    # Save that gif
    if save_file is not None:
        # Opening up every frame and keeping them open will
        # result in too many files being open.
        def frames_iter():
            for root, dirs, files in os.walk(frame_dir_handle.name,
                    topdown=False):
                for image in sorted(files):
                    yield PIL.Image.open(os.path.join(root, image))
        it = frames_iter()
        first = next(it)
        first.save(save_file,
                   save_all=True,
                   append_images=it,
                   duration=10,
                   loop=0)

    # Return success code
    return 0


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    args = parse_arguments()
    try:
        exit(main(**vars(args)))
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        exit(-1)

