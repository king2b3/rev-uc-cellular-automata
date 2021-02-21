from .individual import Individual

class Prey(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            flee:float):
        super().__init__(positions, energy, speed, sense)
        self.flee = flee

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...

    
    def draw(self, surface:"pygame.Surface") -> None:
        # highest energy color = (255,0,255) pink
        # lowest energy color = (255,0,155) pinkish
        pink_scale = 255 - int(math.floor(100 * (1-self.energy)))
        surface.fill(255,0,pink_scale))