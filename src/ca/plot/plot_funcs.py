from ..game.entity.individual import Individual


def average_traits(game:"Game"):
    # Search grid 
    # [energy, speed, sense]
    totals = {}
    num_individuals = {}

    for x in range(len(game.grid)):
        for y in range(len(game.grid[x])):
            if game.grid[x][y] is None:
                ...
            else:
                occupant_name = game.grid[x][y].__class__.__name__
                # Check if dead or alive
                if game.grid[x][y].is_dead(game):
                    deadname = "Dead_" + occupant_name
                    if deadname not in occupant_name:
                        totals[deadname] = [[0],[0],[0]]
                        num_individuals[deadname] = [0]
                    else:
                        totals[deadname][0] += game.grid[x][y].energy
                        totals[deadname][1] += game.grid[x][y].speed
                        totals[deadname][2] += game.grid[x][y].sense
                        num_individuals[deadname][0] += 1
                else:
                    if occupant_name not in totals:
                        totals[occupant_name] = [[0],[0],[0]]
                        num_individuals[occupant_name] = [0]
                    else:
                        totals[occupant_name][0] += game.grid[x][y].energy
                        totals[occupant_name][1] += game.grid[x][y].speed
                        totals[occupant_name][2] += game.grid[x][y].sense
                        num_individuals[occupant_name][0] += 1

    traits = totals.copy()
    for t in totals:
        traits[t][0] = totals[t][0]/3       
        
    return traits


