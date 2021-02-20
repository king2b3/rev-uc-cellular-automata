
from .plot import Plot
from matplotlib import pyplot

class PlotAverage(Plot):
    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError
    
    def average_traits(self, game:"Game"):
        # Search grid 
        traits = [0,0,0]
        for x in range(len(game.grid)):
            for y in range(len(game.grid[x])):
                if game.grid[x][y] is not None:
                    # Check if dead or alive
                    if game.grid[x][y].is_dead():
                        traits[1] += 1
                    else:
                        traits[0] += 1
                else:
                    traits[2] += 1
                
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

         



     
