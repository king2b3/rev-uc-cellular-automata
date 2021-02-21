from .individual import Individual

class Real_Boys(Individual):
    def __init__(self, positions:"Position", energy:float, speed:float, sense:float,
            agression:float, flee:float):
        super().__init__(positions, energy, speed, sense)
        self.agression = agression
        self.flee = flee

    
    def make_move(self, game:"Game") -> None:
        ...

    
    def is_dead(self, game:"Game") -> None:
        ...
    

    def attack(self, game:"Game") -> None:
        ...

    
    def chase(self, game:"Game") -> None:
        ...
    

    def mutate(self, game:"Game") -> None:
        ...