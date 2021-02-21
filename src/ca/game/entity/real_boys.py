from .individual import Individual
import math
import random

class Real_Boys(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            agression:float, flee:float):
        super().__init__(positions, energy, speed, sense)
        self.agression = agression
        self.flee = flee

    
    def make_move(self, game:"Game") -> None:
        moves = []
        for neigh in game.neighbors(self.positions, DistanceMetric.EUCLIDIAN, self.sense):
            if is_food(game):
                new_energy = neigh.energy + self.energy_used(game, neigh.position)

            elif is_predator(game):
                # how far do they need to move to remain safe
                ...

            elif is_prey(game):
                new_energy = neigh.energy + self.energy_used(game, neigh.position)

            else:
                # is a blank cell
                new_energy = self.energy_used(game, neigh.position)
            
            #append neigh and energy to tuple
        # preform the move that is the highest rated
    
    
    def energy_used(self, game:"Game", pos:list) -> float:
        """ Returns the energy used to make a move"""
        # need to come up with an equation to use here
        ...
    
    
    def is_food(self, game:"Game") -> None:
        ...


    def is_prey(self, game:"Game") -> None:
        ...


    def is_predator(self, game:"Game") -> None:
        ...


    def is_dead(self, game:"Game") -> None:
        ...


    def attack(self, game:"Game") -> None:
        ...

    
    def chase(self, game:"Game") -> None:
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