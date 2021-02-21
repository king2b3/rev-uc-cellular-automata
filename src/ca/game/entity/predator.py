from .individual import Individual

class Predator(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            agression:float):
        super().__init__(positions, energy, speed, sense)
        self.agression = agression

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...
    

    def attack(self, game:"Game") -> None:
        ...

    
    def chase(self, game:"Game") -> None:
        ...