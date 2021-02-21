import abc
import pygame
import tempfile


class Plot(abc.ABC):
    def draw(self, game:"Game", surface:"pygame.Surface") -> None:
        # Make the temporary image file path
        fid, file_path = tempfile.mkstemp(".png")
        # Plot the data
        self.plot(game, file_path)
        # Draw the plot image
        surface.blit(pygame.image.load(file_path))


    @abc.abstractmethod
    def plot(self, game:"Game", file_path:str) -> None:
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

