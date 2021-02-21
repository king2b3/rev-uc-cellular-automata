from .plot import Plot
import matplotlib.pyplot as plt
from .plot_funcs import average_traits
import numpy as np


class AverageTraitTime(Plot):
    def __init__(self):
        #self.avgtraits = {}
        self.avgtraits = [[],[],[]]
        


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
        traits = [[1],[1],[1]]
        x_vals = len(self.avgtraits[0])
        """WE FIXING SHIT
        traits = average_traits(game)

        print(traits)

        x_vals_e = np.arange(len(self.avgtraits[0]))
        x_vals_sp = np.arange(len(self.avgtraits[0]))
        x_vals_se = np.arange(len(self.avgtraits[0]))
        """
        fig = plt.figure(figsize=(height/96 ,width/96),dpi=120)
        ax = fig.add_axes([0.3,0.2,0.6,0.6])
        
        ax.set_xlabel('Time Step?')
        ax.set_ylabel('Trait Averages')
        ax.set_title('Traits over Time')
        plt.ylim((0.0,1.0))
        ax.plot(1, 1, color='red', label='ENERGY')
        #ax.plot(x_vals, self.avgtraits[1], color='green', label='SPEED')
        #ax.plot(x_vals, self.avgtraits[2], color='blue', label='SENSE')
        ax.legend()

        # print("avige",self.avgtraits)

        plt.savefig(file_path,dpi=96)
        plt.close(fig) 

