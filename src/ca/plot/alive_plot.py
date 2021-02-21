
from .plot import Plot
import matplotlib.pyplot as plt
import numpy as np

class PlotAlive(Plot):
    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError

    def count_alive(self, game:"Game") -> tuple:
        # Get the information from the game object
        # Search grid
        # alive = [number of living cells, number of dead cells, number of empty cells] 
        alive = [0,0,0]
        for x in range(len(game.grid)):
            for y in range(len(game.grid[x])):
                if isinstance(game.grid[x][y], Individual):
                    # Check if dead or alive
                    if game.grid[x][y].is_dead():
                        alive[1] += 1
                    else:
                        alive[0] += 1
                else:
                    alive[2] += 1
                
        return alive   

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

        living = self.count_alive(game)

        labels = ['Alive', 'Dead', 'None']
        fig, ax = plt.figure()
        rects = ax.bar(np.arange(len(living)),living,0.35)
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Title')
        ax.set_xticks(np.arange(len(living)))
        ax.set_xticklabels(labels)
        ax.legend()

        ...
