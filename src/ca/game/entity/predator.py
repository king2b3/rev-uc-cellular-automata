from .individual import Individual
import math

class Predator(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            agression:float):
        super().__init__(positions, energy, speed, sense)
        self.agression = agression

    
    def make_move(self, game:"Game") -> None:
        # move is to attack the nearest prey
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...
    

    def draw(self, surface:"pygame.Surface") -> None:
        # highest energy color = (255,0,0) red
        # lowest energy color = (255,100,0) orange
        red_scale = int(math.floor(100 * (1-self.energy)))
        surface.fill(255,red_scale,0))