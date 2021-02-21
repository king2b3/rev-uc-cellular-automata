from .plot import Plot
import matplotlib.pyplot as plt
from .plot_funcs import average_traits
import numpy as np


class AverageTraitTime(Plot):
    def __init__(self):
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
        traits = average_traits(game)
        self.avgtraits[0].append(traits[0][0])
        self.avgtraits[1].append(traits[1][0])
        self.avgtraits[2].append(traits[2][0])

        x_vals = np.arange(len(self.avgtraits[0]))

        fig = plt.figure(figsize=(height/96 ,width/96))
        ax = plt.plot(x_vals, self.avgtraits[0])
        plt.plot(x_vals, self.avgtraits[1])
        plt.plot(x_vals, self.avgtraits[2])

        # print("avige",self.avgtraits)

        plt.savefig(file_path)
        plt.close(fig) 

