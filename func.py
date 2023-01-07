import random

def generatecoord(grid):
    SHIP_COORD = {}
    # First ship: 5x1
    SHIP_COORD["5x1"] = createshipcoord(5)
    for i in SHIP_COORD["5x1"]:
        grid[i[1]-1][i[0]-1] = 1
    # Ship: 4x1
    isplacable = False
    while isplacable == False:
        SHIP_COORD["4x1"] = createshipcoord(4)
        if placable(SHIP_COORD["4x1"], grid) == True:
            isplacable = True
            for i in SHIP_COORD["4x1"]:
                grid[i[1]-1][i[0]-1] = 1
    # Ship: 3x1_1
    isplacable = False
    while isplacable == False:
        SHIP_COORD["3x1_1"] = createshipcoord(3)
        if placable(SHIP_COORD["3x1_1"], grid) == True:
            isplacable = True
            for i in SHIP_COORD["3x1_1"]:
                grid[i[1]-1][i[0]-1] = 1
    # Ship: 3x1_2
    isplacable = False
    while isplacable == False:
        SHIP_COORD["3x1_2"] = createshipcoord(3)
        if placable(SHIP_COORD["3x1_2"], grid) == True:
            isplacable = True
            for i in SHIP_COORD["3x1_2"]:
                grid[i[1] - 1][i[0] - 1] = 1
    # Ship: 2x1
    isplacable = False
    while isplacable == False:
        SHIP_COORD["2x1"] = createshipcoord(2)
        if placable(SHIP_COORD["2x1"], grid) == True:
            isplacable = True
            for i in SHIP_COORD["2x1"]:
                grid[i[1] - 1][i[0] - 1] = 1
    return SHIP_COORD

def aishoot(shotsmade):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    while (x, y) in shotsmade:
        x, y = aishoot(shotsmade)
    return (x, y)

def createshipcoord(size):
    x = random.randint(1, 10-size)
    y = random.randint(1, 10)
    coorlist = [(x, y)]
    for i in range(size-1):
        x = x+1
        coorlist.append((x, y))
    return coorlist

def placable(coord_list, grid_list):
    for i in coord_list:
        if grid_list[i[1]-1][i[0]-1] == 1:
            return False
    return True