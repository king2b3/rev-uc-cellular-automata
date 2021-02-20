class Window():
    def __init__(self, game:"Game", plots:list):
        """
        Parameters
        ----------
        game: Game
            The game to run/display.

        plots: list<Plot>
            The list of plots to display.
        """


    def draw(self):
        raise NotImplementedError


    def update(self):
        raise NotImplementedError

