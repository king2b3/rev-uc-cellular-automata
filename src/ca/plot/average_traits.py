
from .plot import Plot
import matplotlib.pyplot as plt

class PlotAverage(Plot):
    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError
    
    def average_traits(self, game:"Game"):
        # Search grid 
        # [energy, speed, sense]
        totals = [0,0,0]
        num_individuals = 0
        for x in range(len(game.grid)):
            for y in range(len(game.grid[x])):
                if isinstance(game.grid[x][y], Individual):
                    num_individuals += 1
                    totals[0] += game.grid[x][y].energy
                    totals[1] += game.grid[x][y].speed
                    totals[2] += game.grid[x][y].sense
        
        traits = totals / num_individuals            
                
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

        
        # Get the information from the game object
        # game.drawinggrid -> dict of dict of entities
        # entity at (x,y)


        ...
