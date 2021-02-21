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

        celldata = []
        rows = []
        
        for key in traits:
            tempdata = traits[key]
            celldata.append([tempdata[0]])
            celldata.append([tempdata[1]])
            celldata.append([tempdata[2]])
            rows.append(key + '_Energy')
            rows.append(key + '_Speed')
            rows.append(key + '_Sense')

        cols = ['Average Values']

        # Table plot params
        xmin = 0.35; xmax = 0.65
        ymin = 0.15; ymax = 0.75
        
        fig = plt.figure(figsize=(height/96 ,width/96), linewidth=2, dpi=96)
        ax = fig.add_axes([xmin,ymin,xmax,ymax])
        ax.table(cellText=celldata,
                            rowLabels=rows,
                            rowLoc='right',
                            colLabels=cols,
                            colWidths=[0.4],
                            loc='center',
                            fontsize=12)
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)# Hide axes border
        plt.box(on=None)

        plt.savefig(file_path, dpi = 120)
        plt.close(fig)
