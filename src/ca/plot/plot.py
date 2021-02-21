import abc
import os
import pygame


class Plot(abc.ABC):
    def draw(self, game:"Game", surface:"pygame.Surface", plot_dir:str) -> None:
        # Make the temporary image file path
        file_path = os.path.join(plot_dir, f"{self.__class__.__name__}.png")
        # Plot the data
        self.plot(game, file_path, surface.get_height(), 
                surface.get_width())
        # Draw the plot image
        surface.blit(pygame.image.load(file_path), (0,0))


    @abc.abstractmethod
    def plot(self, game:"Game", file_path:str, height:int, width:int)\
            -> None:
        """Plot the game information saving the plot to the given
        file path

        Parameters
        ----------
        game: Game
            The object that holds all information about the simulation.
        file_path: str
            The file path to save the plot to.
        """
        ...

