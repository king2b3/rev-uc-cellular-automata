from .entity import Entity

import abc


class Individual(Entity):
    def __init__(self, positions:list, energy:float, speed:float, sense:float):
        super().__init__(positions)
        self.energy = energy
        self.speed = speed
        self.sense = sense


    @abc.abstractmethod
    def make_move(self, game:"Game") -> None:
        ...


    @abc.abstractmethod
    def is_dead(self, game:"Game") -> None:
        ...

