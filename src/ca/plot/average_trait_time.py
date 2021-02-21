from .plot import Plot
import matplotlib.pyplot as plt
from .plot_funcs import average_traits
import numpy as np


class AverageTraitTime(Plot):
    def __init__(self):
        self.avgtraits = {}
        #self.avgtraits = [[],[],[]]
        


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

        for key in traits:
            if key not in self.avgtraits:
                self.avgtraits[key] = [[],[],[]]
                self.avgtraits[key][0].append(traits[key][0])
                self.avgtraits[key][1].append(traits[key][1])
                self.avgtraits[key][2].append(traits[key][2])
            else:
                self.avgtraits[key][0].append(traits[key][0])
                self.avgtraits[key][1].append(traits[key][1])
                self.avgtraits[key][2].append(traits[key][2])
        
        # Create the figure before plotting and set all non-variable params
        fig = plt.figure(figsize=(height/96 ,width/96),dpi=120)
        ax = fig.add_axes([0.3,0.2,0.6,0.6])
        ax.set_xlabel('Time Step?')
        ax.set_ylabel('Trait Averages')
        ax.set_title('Traits over Time')
        plt.ylim((0.0,1.0))

        for key in self.avgtraits:
            x_vals_e = np.arange(len(self.avgtraits[key][0]))
            x_vals_sp = np.arange(len(self.avgtraits[key][1]))
            x_vals_se = np.arange(len(self.avgtraits[key][2]))
            ax.plot(x_vals_e, self.avgtraits[key][0], color='red', label=key + '_Energy')
            ax.plot(x_vals_sp, self.avgtraits[key][1], color='green', label=key + '_Speed')
            ax.plot(x_vals_se, self.avgtraits[key][2], color='blue', label=key + '_Sense')
        

        # print("avige",self.avgtraits)

        ax.legend(fontsize=4)
        plt.savefig(file_path,dpi=96)
        plt.close(fig) 

