from .individual import Individual

class Food(Individual):
    def __init__(self, positions:"Position", energy:float):
        super().__init__([positions], 0, 0, 0)
        self.energy_level = energy

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...