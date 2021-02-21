
from .plot import Plot
import matplotlib.pyplot as plt

class PlotAverage(Plot):

    def __init__(self):
        self.avgtraits = []

    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError
    
    def average_traits(self, game:"Game"):
        # Search grid 
        # [energy, speed, sense]
        totals = [[0],[0],[0]]
        num_individuals = 0
        for x in range(len(game.grid)):
            for y in range(len(game.grid[x])):
                if isinstance(game.grid[x][y], Individual):
                    num_individuals += 1
                    totals[0][0] += game.grid[x][y].energy
                    totals[1][0] += game.grid[x][y].speed
                    totals[2][0] += game.grid[x][y].sense
        traits = totals.copy()
        for t in range(len(totals)):
            traits[t][0] = totals[t][0]/3       
        self.avgtraits[0].append(traits[0][0])
        self.avgtraits[1].append(traits[1][0])
        self.avgtraits[2].append(traits[2][0])
            
        return traits   

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
        traits = self.average_traits(game)
        '''
        rows = []
        cols = []
        the_table = plt.table(cellText=traits,
                      rowLabels=rows,
                      colLabels=columns)
        '''
        # Get the information from the game object
        # game.drawinggrid -> dict of dict of entities
        # entity at (x,y)
        rows = ['Energy', 'Speed', 'Sense']
        cols = ['Average Values']
        #the_table = plt.table(cellText=traits)
        #plt.show()

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
        
        plt.savefig(file_path, dpi=150, facecolor='w', edgecolor='w', orientation='portrait', transparent=False, frameon=None)

        return
        
