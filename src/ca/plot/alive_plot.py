
from .plot import Plot

class PlotAlive(Plot):
    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError

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

        # Get the information from the game object


    def count_alive(self, game:"Game"):
        raise NotImplementedError   

