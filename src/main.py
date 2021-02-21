#!/usr/bin/env python3
"""The main file for our Cellar Automata project"""

import argparse
import pygame
import os
import time

from ca.game.entity.conway import blinker_horizontal
from ca.game import Game, UpdateMode, BoundaryType
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
    parser.add_argument("-sbu", "--seconds_between_updates",
            default=0.5, type=lambda s: abs(float(s)),
            help="The number of seconds between each update of the game")
    def string_to_boundary_type(s:str):
        s = s.uppper()
        if s == "PERIODIC":
            return BoundaryType.PERIODIC
        elif s == "HARD":
            return BoundaryType.HARD
        else:
            raise ValueError(f"Unknown boundary condition: {s}")
    parser.add_argument("-b", "--boundary_type",
            default=BoundaryType.PERIODIC, type=string_to_boundary_type,
            help="The type of boundary condition to use.")
    args = parser.parse_args(args=args)
    return args


def main(seconds_between_updates:float=0.5,
        boundary_type:BoundaryType=BoundaryType.PERIODIC) -> int:
    """Main function.

    Parameters
    ----------
    seconds_between_updates: float=0.5
        The number of seconds between each update of the game.

    boundary_type: BoundaryType=PERIODIC
        The type of boundary condition to use.

    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    game = Game(UpdateMode.ASYNCHRONOUS, blinker_horizontal(),
            BoundaryType.PERIODIC)
    window = Window(game, 
            [AlivePlot(), AverageTraits(), AverageTraitTime(), None], 
            "", 600, 1200)

    time_since_last_update = time.perf_counter()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
        window.draw()
        if time.perf_counter() - time_since_last_update\
                >= seconds_between_updates:
            time_since_last_update = time.perf_counter()
            window.update()

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

