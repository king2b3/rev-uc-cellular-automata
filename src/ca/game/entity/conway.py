from .individual import Individual


class Conway(Individual):
    def __init__(self, position:"Position"):
        super().__init__([position], 0, 0, 0)


    def make_move(self, game:"Game") -> None:
        raise NotImplemented


    def is_dead(self, game:"Game") -> None:
        raise NotImplemented


    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplemented
