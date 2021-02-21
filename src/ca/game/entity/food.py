from .individual import Individual
import math

class Food(Individual):
    def __init__(self, positions:"Position", energy:float):
        super().__init__([positions], energy, 0, 0)

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...

    
    def draw(self, surface:"pygame.Surface") -> None:
        # highest energy color = (0,255,0) Green
        # lowest energy color = (100,255,0) Greenish
        green_scale = int(math.floor(100 * (1-self.energy)))
        surface.fill(green_scale,255,0))