from .individual import Individual
from .position import Position
import math
import random
from .errors import UnknownCellType
# entity types to compare 
from .predator import Predator
from .prey import Prey
from .food import Food
from .blank import Blank

class Real_Boys(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            agression:float):
        super().__init__(positions, energy, speed, sense)
        self.agression = agression
        #self.flee = 1 - agression

    
    def make_move(self, game:"Game", min_pred_distance:int=5) -> None:
        moves = []
        for neigh in game.neighbors(self.positions, DistanceMetric.EUCLIDIAN, self.sense):
            if isinstance(neigh,Blank):
                new_energy = self.energy - self.energy_used(game, neigh.position)
            
            elif isinstance(neigh,Real_Boys):
                # check if they are large or smaller
                if neigh.size() > self.size():
                    new_energy = self.flee(game, neigh)
                else:
                    new_energy = self.energy + neigh.energy - \
                            self.energy_used(game, neigh.position)
            
            elif isinstance(neigh,Prey) or isinstance(neigh,Food):
                new_energy = self.energy + neigh.energy - \
                        self.energy_used(game, neigh.position)
                
            elif isinstance(neigh,Predator):
                new_energy = self.flee(game, neigh)

            else:
                raise UnknownCellType(neigh)
            
            moves.append((neigh.position,new_energy))
        # perform the move with the minimum energy needed
    
    
    def flee(self, game="Game", predator:"neighbor") -> float:
        # calculate the distance the two entities are from each other
        new_x = self.position[0].x - predator.position[0].x
        new_y = self.position[0].y - predator.position[0].y
        
        # find direction prey should go
        if new_x < 0:
            # needs to move in the negative x direction
            new_x -= min_pred_distance
        else:
            new_x += min_pred_distance
        if new_y < 0:
            # needs to move in the negative y direction
            new_y -= min_pred_distance
        else:
            new_y += min_pred_distance
        
        # check if the new location is out of bounds
        grid_len = len(game.grid)
        if new_x < 0:
            # out of bounds left
            new_x = grid_len - new_x
        elif new_x > grid_len:
            # out of bounds right
            new_x -= grid_len
        if new_y < 0:
            # out of bounds bottom
            new_y = grid_len - new_y
        elif new_y > grid_len:
            # out of bounds top
            new_y -= grid_len

        temp_postion = Position(new_x, new_y)
        return (self.energy - self.energy_used(game, temp_postion))

    
    def energy_used(self, game:"Game", pos:list) -> float:
        """ Returns the energy used to make a move"""
        # need to come up with an equation to use here
        """
        figure out s1, s2, s3
        energy = speed*s1 + sense*s2 + size*s3
        """
        ...
    

    def is_dead(self, game:"Game") -> None:
        ...
    

    def mutate(self, mut_size:float=0.1, mut_chance:float=0.2) -> None:
        """Each trait has a chance to be mutated.

        Parameters
        ----------
        mut_size: float
            The percentage of itself the trait can increase of decrease with the mutation
                ie. a 10% rate for a trait with value of 20 means a +/- 2 change is possible

        mut_chance: float
            Chance that any given trait mutates
        """
        for trait in [self.speed, self.sense, self.agression, self.flee]:
            r = random.random
            if r < mut_chance:
                trait += (-1)*random.choice([1,-1])*(trait*mut_size))
    

    def draw(self, surface:"pygame.Surface") -> None:
        # highest energy color = (0,0,255) Blue
        # lowest energy color = (100,0,255) Purpleish
        blue_scale = int(math.floor(100 * (1-self.energy)))
        surface.fill((blue_scale,0,255))