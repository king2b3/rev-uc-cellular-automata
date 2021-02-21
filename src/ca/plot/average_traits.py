import matplotlib.pyplot as plt

from .plot import Plot
from .plot_funcs import average_traits
from ..game.entity.individual import Individual


class AverageTraits(Plot):
    def plot(self, game:"Game", file_path:str, height:int, width:int) -> None:
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

        # Table plot params
        xmin = 0.05; xmax = 0.85
        ymin = 0.15; ymax = 0.75

        fig = plt.figure(figsize=(height/96 ,width/96), linewidth=2, dpi=96)
        ax = fig.add_axes([xmin,ymin,xmax,ymax])
        ax.table(cellText=traits,
                            rowLabels=rows,
                            rowLoc='center',
                            colLabels=cols,
                            colWidths=[0.5],
                            loc='center',
                            fontsize=14)
        #ax.scale(1, 1.5)# Hide axes
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)# Hide axes border
        plt.box(on=None)

        plt.savefig(file_path, dpi = 120)
        plt.close(fig)
