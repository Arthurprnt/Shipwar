import random

def generatecoord(grid):
    SHIP_COORD = {}
    SHIP_AXE = {}
    # First ship: 5x1
    SHIP_AXE["5x1"] = placeboat(SHIP_COORD, "5x1", grid, 5)
    # Ship: 4x1
    SHIP_AXE["4x1"] = placeboat(SHIP_COORD, "4x1", grid, 4)
    # Ship: 3x1_1
    SHIP_AXE["3x1_1"] = placeboat(SHIP_COORD, "3x1_1", grid, 3)
    # Ship: 3x1_2
    SHIP_AXE["3x1_2"] = placeboat(SHIP_COORD, "3x1_2", grid, 3)
    # Ship: 2x1
    SHIP_AXE["2x1"] = placeboat(SHIP_COORD, "2x1", grid, 2)
    return SHIP_COORD, SHIP_AXE

def aishoot(shotsmade):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    while (x, y) in shotsmade:
        x, y = aishoot(shotsmade)
    return (x, y)

def createshipcoord(size):
    facing = random.randint(1, 2)
    if facing == 1:
        x = random.randint(1, 10-size)
        y = random.randint(1, 10)
        coorlist = [(x, y)]
        for i in range(size-1):
            x = x+1
            coorlist.append((x, y))
        axe = "x"
    else:
        x = random.randint(1, 10)
        y = random.randint(1, 10-size)
        coorlist = [(x, y)]
        for i in range(size-1):
            y = y+1
            coorlist.append((x, y))
        axe = "y"
    return coorlist, axe

def placeboat(shipscoord, name, thegrid, size):
    isplacable = False
    while not isplacable:
        returnedvalues = createshipcoord(size)
        shipscoord[name] = returnedvalues[0]
        if placable(shipscoord[name], thegrid):
            isplacable = True
            for i in shipscoord[name]:
                thegrid[i[1]-1][i[0]-1] = 1
    return returnedvalues[1]

def placable(coord_list, grid_list):
    for i in coord_list:
        if grid_list[i[1]-1][i[0]-1] != 0:
            return False
        for y in range(-1, 2):
            for x in range(-1, 2):
                if 9 >= i[1]+y >= 0 and 9 >= i[0]+x >= 0:
                    if grid_list[i[1]+y-1][i[0]+x-1] != 0:
                        return False
    return True