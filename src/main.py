#!/usr/bin/env python3
"""The main file for our Cellar Automata project"""

import argparse
import pygame
import os

from ca.game.entity.conway import boat
from ca.game import Game, UpdateMode, BoundaryType
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
    args = parser.parse_args(args=args)
    return args


def main() -> int:
    """Main function.

    Parameters
    ----------

    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    game = Game(UpdateMode.ASYNCHRONOUS, boat(), BoundaryType.PERIODIC)
    window = Window(game, [], "", 600, 1200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
        window.draw()
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

