from .individual import Individual
from .position import DistanceMetric

class Conway(Individual):
    def __init__(self, position:"Position", living:bool):
        super().__init__([position], 0, 0, 0)
        self.living = living


    def make_move(self, game:"Game") -> None:
        living_neighbors = sum(sum(x.state for x in n.values()) for n in game.neighbors(self.position, 1, DistanceMetric.MANHATTAN).values())    
        if self.living:
            if living_neighbors == 2 or living_neighbors == 3:
                self.living = True
            else:
                self.living = False
        else:
            if living_neighbors == 3:
                self.living = True


    def is_dead(self, game:"Game") -> None:
        return not self.living


    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError

####### Initial Formations #######

def glider() -> dict:
    ...


def block() -> dict:
    ...


def light_weight_ship() -> dict:
    ...


def middle_weight_ship() -> dict:
    ...


def heavy_weight_ship() -> dict:
    ...


def bee_hive() -> dict:
    ...


def boat() -> dict:
    ...


def tub() -> dict:
    ...


def blinker() -> dict:
    ...


def toad() -> dict:
    ...


def beacon() -> dict:
    ...


def pulsar() -> dict:
    ...


def penta_decathlon() -> dict:
    ...
