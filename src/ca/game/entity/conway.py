from .individual import Individual
from .position import DistanceMetric, Position


class Conway(Individual):
    def __init__(self, position:"Position", living:bool):
        super().__init__([position], 0, 0, 0)
        self.living = living


    def make_move(self, game:"Game") -> None:
        living_neighbors = 0
        for neigh in game.neighbors(self.positions[0], 
                DistanceMetric.EUCLIDIAN, 1.5):
            if not neigh.is_dead(game):
                living_neighbors += 1
        

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
        # Select the color based on living status
        if self.living:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
            
        # Fill the surface with the color!
        surface.fill(color)


####### Initial Formations #######

####### Stationary #######

def block(x,y) -> dict:
    """ 4x4 block """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),False),
                3 : Conway(Position(0,3),False)
             },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),True), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),False)
             },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
             },
        3  : {
                0 : Conway(Position(3,0),False), 
                1 : Conway(Position(3,1),False), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),False)
             }
    }
    return temp


def tub() -> dict:
    """ 3x3 Tub """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),False)
             },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True)
             },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),False)
             }
    }
    return temp


def boat() -> dict:
    """ 3x3 Boat """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True)
              },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),False)
              }
    }
    return temp


def snake() -> dict:
    """ 4x2 Sanake """
    temp = {
        0  : {
                0 : Conway(Position(0,0),True), 
                1 : Conway(Position(0,1),True),
                2 : Conway(Position(0,1),False),
                3 : Conway(Position(0,1),True)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False),
                2 : Conway(Position(1,1),True),
                3 : Conway(Position(1,1),True)
              }
    }
    return temp


def ship() -> dict:
    """ 3x3 Ship """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),False)
              }
    }
    return temp


def aircraft_carrier() -> dict:
    """ 4x3 Aircraft Carrier """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),True)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),True)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),False),
                3 : Conway(Position(2,3),True)
              }
    }
    return temp


def beehive() -> dict:
    """ 4x3 Beehive """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),False)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),False),
                3 : Conway(Position(1,3),True)
              },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
              }
    }
    return temp


def barge() -> dict:
    """ 4x4 Barge """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),False)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),True), 
                2 : Conway(Position(1,2),False),
                3 : Conway(Position(1,3),True)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
              },
        3  : {
                0 : Conway(Position(3,0),False), 
                1 : Conway(Position(3,1),True), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),False)
              }
    }
    return temp


def python() -> dict:
    """ 3x5 Python """
    temp = {
        0  : {
                0 : Conway(Position(0,0),True), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),False),
                3 : Conway(Position(0,3),False),
                4 : Conway(Position(0,4),False)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),False),
                4 : Conway(Position(0,4),True)
              },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),False),
                3 : Conway(Position(2,3),True),
                4 : Conway(Position(0,4),True)
              }
    }
    return temp


def long_boat() -> dict:
    """ 4x4 Long Boat """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),True)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),True), 
                2 : Conway(Position(1,2),False),
                3 : Conway(Position(1,3),True)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
              },
        3  : {
                0 : Conway(Position(3,0),False), 
                1 : Conway(Position(3,1),True), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),False)
              }
    }
    return temp


def fishhook() -> dict:
    """ 4x4 Fishhook """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),True)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),False)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
              },
        3  : {
                0 : Conway(Position(3,0),True), 
                1 : Conway(Position(3,1),True), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),False)
              }
    }
    return temp


def loaf() -> dict:
    """ 4x4 Loaf """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),False)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),False),
                3 : Conway(Position(1,3),True)
              },
        2  : {
                0 : Conway(Position(2,0),True), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),True),
                3 : Conway(Position(2,3),False)
              },
        3  : {
                0 : Conway(Position(3,0),False), 
                1 : Conway(Position(3,1),True), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),False)
              }
    }
    return temp


def human() -> dict:
    """ 9x7 Human """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),True),
                3 : Conway(Position(0,3),False),
                4 : Conway(Position(0,4),True),
                5 : Conway(Position(0,5),False),
                6 : Conway(Position(0,6),False)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),False),
                4 : Conway(Position(1,4),True),
                5 : Conway(Position(1,5),False),
                6 : Conway(Position(1,6),False)
              },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),False),
                3 : Conway(Position(2,3),True),
                4 : Conway(Position(2,4),False),
                5 : Conway(Position(2,5),False),
                6 : Conway(Position(2,6),True)
              },
        3  : {
                0 : Conway(Position(3,0),False), 
                1 : Conway(Position(3,1),True), 
                2 : Conway(Position(3,2),False),
                3 : Conway(Position(3,3),True),
                4 : Conway(Position(3,4),False),
                5 : Conway(Position(3,5),True),
                6 : Conway(Position(3,6),False)
             },
        4  : {
                0 : Conway(Position(4,0),True), 
                1 : Conway(Position(4,1),False), 
                2 : Conway(Position(4,2),True),
                3 : Conway(Position(4,3),True),
                4 : Conway(Position(4,4),True),
                5 : Conway(Position(4,5),False),
                6 : Conway(Position(4,6),False)
              },
        5  : {
                0 : Conway(Position(5,0),False), 
                1 : Conway(Position(5,1),False), 
                2 : Conway(Position(5,2),False),
                3 : Conway(Position(5,3),True),
                4 : Conway(Position(5,4),False),
                5 : Conway(Position(5,5),False),
                6 : Conway(Position(5,6),False)
              },
        6  : {
                0 : Conway(Position(6,0),False), 
                1 : Conway(Position(6,1),False), 
                2 : Conway(Position(6,2),True),
                3 : Conway(Position(6,3),False),
                4 : Conway(Position(6,4),True),
                5 : Conway(Position(6,5),False),
                6 : Conway(Position(6,6),False)
              },
        7  : {
                0 : Conway(Position(7,0),False), 
                1 : Conway(Position(7,1),False), 
                2 : Conway(Position(7,2),True),
                3 : Conway(Position(7,3),False),
                4 : Conway(Position(7,4),True),
                5 : Conway(Position(7,5),False),
                6 : Conway(Position(7,6),False)
              },
        8  : {
                0 : Conway(Position(8,0),False), 
                1 : Conway(Position(8,1),False), 
                2 : Conway(Position(8,2),True),
                3 : Conway(Position(8,3),True),
                4 : Conway(Position(8,4),True),
                5 : Conway(Position(8,5),False),
                6 : Conway(Position(8,6),False)
              }
    }
    return temp


####### Movement #######

def glider() -> dict:
    """ 3x5 Glider """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),False),
                3 : Conway(Position(0,3),False),
                4 : Conway(Position(0,4),False)
              },
        1  : {
                0 : Conway(Position(1,0),True), 
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True),
                3 : Conway(Position(1,3),False),
                4 : Conway(Position(0,4),True)
              },
        2  : {
                0 : Conway(Position(2,0),False), 
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),False),
                3 : Conway(Position(2,3),True),
                4 : Conway(Position(0,4),True)
              }
    }
    return temp

def blinker_horizontal() -> dict:
    """ 5x5 Blinker Horizontal """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False),
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),False), 
                3 : Conway(Position(0,3),False),
                4 : Conway(Position(0,4),False),
              },
        
        1  : {
                0 : Conway(Position(1,0),False),
                1 : Conway(Position(1,1),False), 
                2 : Conway(Position(1,2),True), 
                3 : Conway(Position(1,3),False),
                4 : Conway(Position(1,4),False),
              },
        2  : {
                0 : Conway(Position(2,0),False),
                1 : Conway(Position(2,1),False), 
                2 : Conway(Position(2,2),True), 
                3 : Conway(Position(2,3),False),
                4 : Conway(Position(2,4),False)
              },
        3  : {
                0 : Conway(Position(3,0),False),
                1 : Conway(Position(3,1),False), 
                2 : Conway(Position(3,2),True), 
                3 : Conway(Position(3,3),False),
                4 : Conway(Position(3,4),False),
              },
        4  : {
                0 : Conway(Position(4,0),False),
                1 : Conway(Position(4,1),False), 
                2 : Conway(Position(4,2),False), 
                3 : Conway(Position(4,3),False),
                4 : Conway(Position(4,4),False),
              },
    }
    return temp

def blinker_vertical() -> dict:
    """ 5x5 Blinker Vertical """
    temp = {
        0  : {
                0 : Conway(Position(0,0),False),
                1 : Conway(Position(0,1),False), 
                2 : Conway(Position(0,2),False), 
                3 : Conway(Position(0,3),False),
                4 : Conway(Position(0,4),False),
              },
        
        1  : {
                0 : Conway(Position(1,0),False),
                1 : Conway(Position(1,0),False), 
                2 : Conway(Position(1,1),False), 
                3 : Conway(Position(1,2),False),
                4 : Conway(Position(1,0),False),
              },
        2  : {
                0 : Conway(Position(2,0),False),
                1 : Conway(Position(2,1),True), 
                2 : Conway(Position(2,2),True), 
                3 : Conway(Position(2,3),True),
                4 : Conway(Position(2,4),False)
              },
        3  : {
                0 : Conway(Position(3,0),False),
                1 : Conway(Position(3,1),False), 
                2 : Conway(Position(3,2),False), 
                3 : Conway(Position(3,3),False),
                4 : Conway(Position(3,4),False),
              },
        4  : {
                0 : Conway(Position(4,0),False),
                1 : Conway(Position(4,1),False), 
                2 : Conway(Position(4,2),False), 
                3 : Conway(Position(4,3),False),
                4 : Conway(Position(4,4),False),
              },
    }
    return temp


def repeater_tetris() -> dict:
    """ Repeating shape that looks like a tetris shape"""
    temp = {
        0  : {
                0 : Conway(Position(0,0),True), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
                1 : Conway(Position(1,1),True), 
                2 : Conway(Position(1,2),False)
              }
    }
    return temp