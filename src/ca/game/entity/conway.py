from .individual import Individual
from .position import DistanceMetric, Position

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
        # Select the color based on living status
        if self.living:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
            
        # Fill the surface with the color!
        surface.fill(color)


####### Initial Formations #######

def glider() -> dict:
    """ 3x3 Basic glider"""
    temp = {
        0  : {
                0 : Conway(Position(0,0),True), 
                1 : Conway(Position(0,1),True), 
                2 : Conway(Position(0,2),True)
              },
        1  : {
                0 : Conway(Position(1,0),False), 
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
    """ 4x3 Ship """
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
