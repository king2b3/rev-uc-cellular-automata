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