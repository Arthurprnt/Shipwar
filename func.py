import pygame
import random
from imports import *

def addcase(caselist, coordcaselist, image, x, y, nb_x, nb_y):
    """
    Add a case to the list of cases that need to be display every loop execution
    """
    caselist.append(image)
    caselist[-1].multiplesize(1.5, X)
    caselist[-1].set_defaultpos(x, y)
    coordcaselist.append((nb_x, nb_y))

def aishoot(shotsmade, touchedshots, list_pos, diff):
    """
    Return a case to be shoot choosed by the ia
    """
    if len(shotsmade)!=0  and len(touchedshots)/len(shotsmade) < 0.30 and diff > 1:
        possible_shoots = []
        for i in list_pos.keys():
            for y in list_pos[i]:
                if not(y in shotsmade):
                    possible_shoots.append(y)
        rng = random.randint(0, len(possible_shoots)-1)
        x = possible_shoots[rng][0]
        y = possible_shoots[rng][1]
    elif shotsmade != [] and shotsmade[-1] in touchedshots and touchedshots[-1][0] <= 9 and diff > 0:
        x = touchedshots[-1][0] + 1
        y = touchedshots[-1][1]
        while (x, y) in shotsmade:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
    elif len(shotsmade)>=2 and shotsmade[-2] in touchedshots and touchedshots[-1][1] <= 9 and diff > 0:
        x = touchedshots[-1][0]
        y = touchedshots[-1][1] + 1
        while (x, y) in shotsmade:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
    elif len(shotsmade)>=3 and shotsmade[-3] in touchedshots and touchedshots[-1][0] >= 0 and diff > 0:
        x = touchedshots[-1][0] - 1
        y = touchedshots[-1][1]
        while (x, y) in shotsmade:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
    elif len(shotsmade)>=4 and shotsmade[-4] in touchedshots and touchedshots[-1][1] >= 0 and diff > 0:
        x = touchedshots[-1][0]
        y = touchedshots[-1][1] - 1
        while (x, y) in shotsmade:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
    else:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        while (x, y) in shotsmade:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
    return (x, y)

def checkshipstats(listshipcoord, touchedcoord):
    """
    Check if the ship is just touched or if it's totally sunk
    """
    txt = "touché"
    for ship in listshipcoord:
        for coord in listshipcoord[ship]:
            if coord == touchedcoord:
                listshipcoord[ship].pop(listshipcoord[ship].index(coord))
                if listshipcoord[ship] == []:
                    txt = "coulé"
    return txt

def cleargride(playerlist, listship, shipcoord):
    """
    Reset a grid and the list of ship's coord
    """
    playerlist = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in listship:
        i.clicked = False
        clickedship = ""
        if i.axe == "y":
            i.image = pygame.transform.rotate(i.image, 90)
        i.axe = "x"
        i.set_pos(i.default_pos[0], i.default_pos[1])
        if i.name in shipcoord.keys():
            del shipcoord[i.name]
    return playerlist, clickedship

def createshipcoord(size):
    """
    Return random coord for a ship
    """
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

def generatecoord(grid):
    """
    Return the list of all the coord of the ships
    """
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

def placable(coord_list, grid_list):
    """
    Check if the ship can be place on the grid
    """
    for i in coord_list:
        if grid_list[i[1]-1][i[0]-1] != 0:
            return False
        for y in range(-1, 2):
            for x in range(-1, 2):
                if 9 >= i[1]+y-1 >= 0 and 9 >= i[0]+x-1 >= 0:
                    if grid_list[i[1]+y-1][i[0]+x-1] != 0:
                        return False
    return True

def placeboat(shipscoord, name, thegrid, size):
    """
    Place a ship on a grid
    """
    isplacable = False
    while not isplacable:
        returnedvalues = createshipcoord(size)
        shipscoord[name] = returnedvalues[0]
        if placable(shipscoord[name], thegrid):
            isplacable = True
            for i in shipscoord[name]:
                thegrid[i[1]-1][i[0]-1] = 1
    return returnedvalues[1]

def updatecases(emptycase, touchedcase, screen):
    """
    Display every cases generated
    """
    for i in emptycase:
        screen.blit(i.image, i.position)
    for i in touchedcase:
        screen.blit(i.image, i.position)