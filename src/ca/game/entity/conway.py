from .individual import Individual


class Conway(Individual):
    def __init__(self, position:"Position", living:bool):
        super().__init__([position], 0, 0, 0)
        self.living = living


    def make_move(self, game:"Game") -> None:
        raise NotImplementedError


    def is_dead(self, game:"Game") -> None:
        return self.living


    def draw(self, surface:"pygame.Surface") -> None:
        raise NotImplementedError
