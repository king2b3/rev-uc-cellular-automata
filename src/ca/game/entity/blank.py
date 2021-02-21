from .individual import Individual

class Blank(Individual):
    def __init__(self, positions:"Position"):
        super().__init__([positions], 0, 0, 0)

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...

    
    def draw(self, surface:"pygame.Surface") -> None:
        # blank cell. white color
        surface.fill(255,255,255))