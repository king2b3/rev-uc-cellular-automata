import abc


class Plot(abc.ABC):
    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError


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

