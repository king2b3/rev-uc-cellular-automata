import pygame
import tempfile


class Window():
    def __init__(self, game:"Game", plots:list, frame_dir:str,
            height:int, width:int):
        """
        Parameters
        ----------
        game: Game
            The game to run/display.

        plots: list<Plot>
            The list of plots to display.
        frame_dir: str
            The directory to save each frame drawn on the PyGame
            screen.
        height: int
            The height of the PyGame window.
        width: int
            The width of the PyGame window.
        """
        # Save the members
        self.game = game
        self.plots = plots
        self.frame_dir = frame_dir
        self._plot_dir_handle = tempfile.\
                TemporaryDirectory(prefix="celluar_automat_plots_")

        # Initialize PyGame
        pygame.init()
        # Set up surfaces
        half_width = width//2
        self._main_surface = pygame.display.set_mode((width, height))
        self._game_subsurface = self._main_surface.subsurface(
                pygame.Rect((0,0), (half_width, height)))
        self._plot_subsurface = self._main_surface.subsurface(
                pygame.Rect((half_width,0), (half_width, height)))
        # Setup the font
        self._cursor_font_size = int(self._plot_subsurface.get_height()/16)
        self._cursor_font = pygame.font.SysFont(None, 
                self._cursor_font_size)


    def draw(self, cursor_name:str):
        # Black out the screen
        self._main_surface.fill((0,0,0))

        # Draw the game board
        self.game.draw(self._game_subsurface)

        # Draw each plot
        if len(self.plots) > 0:
            if len(self.plots) % 2 != 0:
                raise ValueError("Number of plots must be an even number")

            plot_width = self._plot_subsurface.get_width() \
                    / (len(self.plots)//2)
            plot_height = self._plot_subsurface.get_height() \
                    / (len(self.plots)//2)
            plot_number = 0
            for x in range(len(self.plots)//2):
                for y in range(len(self.plots)//2):
                    # Get the plot
                    plot = self.plots[plot_number]
                    plot_number += 1
                    # Prepare the surface
                    plot_surface = self._plot_subsurface.subsurface(
                            pygame.Rect(
                                (x*plot_width, y*plot_height),
                                (plot_width, plot_height)))
                    if plot is None:
                        # Display cursor information
                        cursor_label = self._cursor_font.render(
                                "Cursor Type:", True, (255, 255, 255))
                        plot_surface.blit(cursor_label, 
                                (0, plot_height//4))
                        cur_name = self._cursor_font.render(
                                cursor_name, True, (255, 255, 255))
                        plot_surface.blit(cur_name, 
                                (0, plot_height//3))
                    else:
                        # Draw the plot
                        plot.draw(self.game, plot_surface, 
                                self._plot_dir_handle.name)

        # Tell PyGame the screen has been updated
        pygame.display.update()


    def update(self):
        self.game.update()

