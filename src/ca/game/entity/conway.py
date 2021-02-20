from .individual import Individual


class Conway(Individual):
    def __init__(self, position:"Position"):
        super().__init__([position], 0, 0, 0)


    def make_move(self, game:"Game") -> None:
        raise NotImplementedError


    def is_dead(self, game:"Game") -> None:
        raise NotImplementedError


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
