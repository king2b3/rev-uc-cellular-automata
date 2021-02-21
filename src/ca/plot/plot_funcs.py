from ..game.entity.individual import Individual


def average_traits(game:"Game"):
    # Search grid 
    # [energy, speed, sense]
    totals = [[0],[0],[0]]
    num_individuals = 0
    for x in range(len(game.grid)):
        for y in range(len(game.grid[x])):
            if isinstance(game.grid[x][y], Individual):
                num_individuals += 1
                totals[0][0] += game.grid[x][y].energy
                totals[1][0] += game.grid[x][y].speed
                totals[2][0] += game.grid[x][y].sense
    traits = totals.copy()
    for t in range(len(totals)):
        traits[t][0] = totals[t][0]/3       
        
    return traits

