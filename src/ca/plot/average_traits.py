import matplotlib.pyplot as plt

from .plot import Plot
from .plot_funcs import average_traits
from ..game.entity.individual import Individual


class AverageTraits(Plot):
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
        traits = average_traits(game)

        # Get the information from the game object
        # game.drawinggrid -> dict of dict of entities
        # entity at (x,y)
        rows = ['Energy', 'Speed', 'Sense']
        cols = ['Average Values']

        fig = plt.figure(linewidth=2,
                tight_layout={'pad':1}
                )

        the_table = plt.table(cellText=traits,
                            rowLabels=rows,
                            rowLoc='right',
                            colLabels=cols,
                            colWidths=[0.3],
                            loc='center')
        the_table.scale(1, 1.5)# Hide axes
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)# Hide axes border
        plt.box(on=None)

        plt.savefig(file_path, dpi=150, facecolor='w', edgecolor='w',
                orientation='portrait', transparent=False, frameon=None)
        
