from .plot import Plot
import matplotlib.pyplot as plt
import numpy as np
from ..game.entity.individual import Individual


class AlivePlot(Plot):
    def count_alive(self, game:"Game") -> tuple:
        """Get the information from the game object
        Search grid
        alive = [number of living cells, number of dead cells, number of 
        empty cells]
        """
        test = {'None': [0]}
        for x in range(len(game.grid)):
            for y in range(len(game.grid[x])):
                if game.grid[x][y] is None:
                    test['None'] += 1
                else:
                    occupant_name = game.grid[x][y].__class__.__name__
                    if occupant_name in test:
                        # Check if dead or alive
                        if game.grid[x][y].is_dead(game):
                            test[occupant_name][1] += 1
                        else:
                            test[occupant_name][0] += 1
                    else:
                        # Check if dead or alive
                        test[occupant_name] = [0,0]
                        if game.grid[x][y].is_dead(game):
                            test[occupant_name][1] += 1
                        else:
                            test[occupant_name][0] += 1
                
        return test   


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

        living = self.count_alive(game)
        # print(living)

        #Plotting Parameters
        barwidth = 0.1
        xmin = 0.2; xmax = 0.75
        ymin = 0.15; ymax = 0.75
        labels = ['Alive', 'Dead', 'None']
        x_vals = np.arange(len(labels))

        unique_entities = len(living)
        barwidth = (xmax - xmin) / len(living)

        #Set Up Figure
        fig = plt.figure(figsize=(height/96 ,width/96), dpi=96)
        ax = fig.add_axes([xmin,ymin,xmax,ymax])

        key_index = 0
        for key in living:
           #plot living[key] with a check for None Type
            if living[key] == 'None':
                ax.bar(x_vals[-1] + barwidth/unique_entities, living[key], barwidth, label="Empty Desolate Wasteland")
            else:
                
                ax.bar(x_vals[0:2] + ((key_index-1) - (int((unique_entities-1)/2)))*barwidth/unique_entities, living[key], barwidth, label="Something")
                key_index+=1

        ax.set_ylabel('Total')
        ax.set_title('Population Totals')
        ax.set_xticks(x_vals)
        ax.set(xlim=(-0.5, len(labels)-0.5))
        ax.set_xticklabels(labels)
        #fig = plt.figure()
        #ax = plt.bar(np.arange(len(living)),living,0.35)
        # Add some text for labels, title and custom x-axis tick labels, etc.
        # ax.set_xlabel('X Label')
        
        ax.legend()

        plt.savefig(file_path, dpi=96)
        plt.close(fig)

